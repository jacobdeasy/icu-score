import argparse, numpy as np, os, pandas as pd

from scipy.optimize import curve_fit
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from saps2 import saps2_risk


def tune_oasis(X, y):
    logreg = LogisticRegression(solver='lbfgs')
    logreg.fit(X[:, None], y)

    b0 = logreg.intercept_[0]
    b1 = logreg.coef_[0, 0]

    return b0, b1


def tune_saps2(X, y):
    popt, pcov = curve_fit(saps2_risk, X, y,
        p0=np.array([-7.7631, 0.0737, 0.9971]))

    return popt


def tune_score(score_name, data, listfile):
    if score_name not in ['oasis', 'saps2']:
        raise Exception('ICU score is not recognized.')

    X_train = pd.read_csv(os.path.join(data, f'train_{score_name}_scores.csv'))
    X_train = X_train['score'].values
    stay_df = pd.read_csv(listfile).sort_values(by=['stay'])
    y_train = stay_df['y_true'].values

    if score_name == 'oasis':
        B = np.zeros((10, 2))
    elif score_name == 'saps2':
        B = np.zeros((10, 3))

    for i in range(10):
        X1, X2, y1, y2 = train_test_split(X_train, y_train,
            test_size=0.1, stratify=y_train, random_state=i)

        if score_name == 'oasis':
            b = tune_oasis(X1, y1)
        elif score_name == 'saps2':
            b = tune_saps2(X1, y1)

        B[i] = np.array(b)

    return B


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tune ICU score.')
    parser.add_argument('score_name', type=str,
                        help='ICU severity score')
    parser.add_argument('data', type=str,
                        help='path to data directory')
    parser.add_argument('listfile', type=str,
                        help='path to listfile')
    parser.add_argument('--coefs', type=str, default='coefs',
                        help='path to coefficients directory')
    args = parser.parse_args()

    if not os.path.exists(args.coefs):
        os.makedirs(args.coefs)

    B = tune_score(args.score_name, args.data, args.listfile)

    if args.score_name == 'oasis':
        B = pd.DataFrame(B, columns=['b0', 'b1'])
    elif args.score_name == 'saps2':
        B = pd.DataFrame(B, columns=['b0', 'b1', 'b2'])
    B.to_csv(os.path.join(args.coefs, args.score_name)+'.csv', index=None)
    print(B)

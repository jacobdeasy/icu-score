import argparse
import numpy
import numpy as np
import os
import pandas as pd

from oasis import *
from saps2 import *


def score_patients(score_name, data, partition, out_dir='scores'):
    """Score a directory of patient timeseries."""
    if score_name not in ['oasis', 'saps2']:
        raise Exception('ICU score name is not recognized.')

    if score_name == 'oasis':
        score_func = oasis_score
    elif score_name == 'saps2':
        score_func = saps2_score

    root = os.path.join(data, partition)
    ts_files = sorted([f for f in os.listdir(root) if f != 'listfile.csv'])
    scores = np.zeros(len(ts_files))

    for i, ts_file in enumerate(ts_files):
        ts = pd.read_csv(os.path.join(root, ts_file), dtype={'icd9': str})

        if ts['Hours'].min() > 24:
            # No info before 24 hours
            score, risk = 0, 0
        else:
            if ts.loc[(0 < ts['Hours']) & (ts['Hours'] < 24)].shape[0] == 0:
                # No info after admission
                ts = ts.loc[ts['Hours'] < 0].iloc[-1, :]
            else:
                ts = ts.loc[(0 < ts['Hours']) & (ts['Hours'] < 24)]

            scores[i] = score_func(ts)

    score_arr = np.stack((np.array(ts_files), scores), axis=1)
    score_df = pd.DataFrame(score_arr, columns=['stay', 'score'])
    score_df.to_csv(
        os.path.join(out_dir, f'{partition}_{score_name}_scores.csv'),
        index=None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Score ICU patients.')
    parser.add_argument('score_name', type=str,
                        help='ICU severity score name')
    parser.add_argument('data', type=str,
                        help='path to patient directory')
    parser.add_argument('--out', type=str, default='scores',
                        help='output directory')
    args = parser.parse_args()

    if not os.path.exists(args.out):
        os.makedirs(args.out)

    score_patients(args.score_name, args.data, 'test')
    score_patients(args.score_name, args.data, 'train')

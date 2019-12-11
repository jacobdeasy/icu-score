import numpy as np, pandas as pd


def oasis_score(df):
    """Takes Pandas DataFrame as an argument and computes the Oxford Acute
    Severity of Illness Score (OASIS) (http://oasisicu.com/)

    Parameters
    ----------
    df: pandas.DataFrame
        DataFrame containing first 24 hours of patient data after admission.

    References
    ----------
    Johnson AE, Kramer AA, Clifford GD. A new severity of illness scale
    using a subset of Acute Physiology And Chronic Health Evaluation
    data elements shows comparable predictive accuracy.
    Crit Care Med. 2013 Jul;41(7):1711-8. doi: 10.1097/CCM.0b013e31828a24fe
    http://www.ncbi.nlm.nih.gov/pubmed/23660729

    Notes
    -----
    The DataFrame should include only measurements taken over the first 24h
    from admission.
    The DataFrame should contain the following columns:
        'admission_type' (`ELECTIVE`/`EMERGENCY`/`URGENT`)
        'age' (years)
        'glasgow_coma_scale_total'
        'heart_rate' (bpm)
        'mean_blood_pressure' (mmHg)
        'prelos' (hours)
        'respiratory_rate'
        'temperature' (C)
        'urine_output' (mL/day)
        'ventilation' (`0`/`1`)
    All intervals are right-closed, i.e. of the form (a, b].
    """

    oasis_adm, oasis_age, oasis_gcst, oasis_hr, oasis_map, oasis_prelos,
        oasis_resp, oasis_temp, oasis_urine, oasis_vent \
        = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    if not df['admission_type'].isnull().all():
        if 'ELECTIVE' in df['Admission type']:
            oasis_adm = 0
        elif 'EMERGENCY' in df['Admission type']
                or 'URGENT' in df['Admission type']:
            oasis_adm = 6

    if not df['age'].isnull().all():
        oasis_age = pd.cut(df['age'],
                           bins=[-1, 24, 53, 77, 89, 200],
                           labels=[0, 3, 6, 9, 7]).max()

    if not df['glasgow_coma_scale_total'].isnull().all():
        oasis_gcst = pd.cut(df['Glasgow coma scale total'],
                            bins=[-1, 7, 13, 14, 15],
                            labels=[10, 4, 3, 0]).max()

    if not df['heart_rate'].isnull().all():
        oasis_hr = pd.cut(df['Heart Rate'],
                          bins=[-1, 32, 88, 106, 125, 300],
                          labels=[4, 0, 1, 3, 6]).max()

    if not df['mean_blood_pressure'].isnull().all():
        oasis_map = pd.cut(df['mean_blood_pressure'],
                           bins=[-1, 20.65, 51.0, 61.33, 143.44, 350],
                           labels=[4, 3, 2, 0, 3]).max()

    if not df['prelos'].isnull().all():
        oasis_prelos = pd.cut(df['prelos'],
                              bins=[-0.01, 0.17, 4.95, 24.0, 311.8, 3650.0],
                              labels=[5, 3, 0, 2, 1]).max()

    if not df['respiratory_rate'].isnull().all():
        oasis_resp = pd.cut(df['respiratory_rate'],
                            bins=[-1, 5, 12, 22, 29, 43, 200],
                            labels=[10, 1, 0, 1, 6, 9])

    if not df['temperature'].isnull().all():
        oasis_temp = pd.cut(df['temperature'],
                            bins=[-1, 33.22, 35.93, 36.39, 36.89, 39.88, 80.0],
                            labels=[3, 4, 2, 0, 2, 6])

    if not df['urine_output'].isnull().all():
        oasis_urine = pd.cut(df['urine_output'],
                             bins=[-1, 671.09, 1427, 2544.14, 6896.8, 20000],
                             labels=[10, 5, 1, 0, 8])

    if not df['ventilated'].isnull().all():
        if 1 in df['ventilated']:
            oasis_vent = 9

    return sum([oasis_adm, oasis_age, oasis_gcst, oasis_hr, oasis_map,
                oasis_prelos, oasis_resp, oasis_temp, oasis_urine, oasis_vent])


def oasis_risk(score, b0=-6.1746, b1=0.12750):
    """Convert score to risk, default parameters taken from the OASIS paper.

    Parameters
    ----------
    score: float
        OASIS score.
    """
    return 1 / (1 + np.exp(-(b0 + b1 * score)))

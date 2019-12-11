import numpy as np, pandas as pd


def saps2_score(df):
    """Takes Pandas DataFrame as an argument and computes the Simplified Acute
    Physiology Score (SAPS) II

    Parameters
    ----------
    df: pandas.DataFrame
        DataFrame containing first 24 hours of patient data after admission.

    References
    ----------
    Le Gall, J. R., Lemeshow, S., & Saulnier, F. (1993). A new simplified acute
    physiology score (SAPS II) based on a European/North American multicenter
    study. Jama, 270(24), 2957-2963.
    https://www.ncbi.nlm.nih.gov/pubmed/8254858

    Notes
    -----
    The DataFrame should include only measurements taken over the first 24h 
    from admission.
    The DataFrame should contain the following columns:
        'admission_type' (ELECTIVE/EMERGENCY/URGENT)
        'age' (years)
        'bicarbonate' (mEq/L)
        'bilirubin' (mg/dL)
        'blood_urea_nitrogen' (mg/dL)
        'glasgow_coma_scale_total'
        'heart_rate' (bpm)
        'icd9' List of all current icd9 diagnoses.
        'potassium' (mEq/L)
        'sodium' (mEq/L)
        'systolic_blood_pressure' (mmHg)
        'temperature' (C)
        'urine_output' (mL/day, total over 24 hours)
        'ventilated' (mmHg/%, PaO2/FiO2)
        'white_blood_cell_count' (10^3/mm^3)
    All intervals are right-closed, i.e. of the form (a, b].
    """

    saps_adm, saps_age, saps_bicarb, saps_bili, saps_bun, saps_gcst, \
        saps_gcsvr, saps_hr, saps_icd9, saps_pot, saps_sbp, saps_sod, \
        saps_temp, saps_urine, saps_wbc \
        = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for val in df['admission_type']:
        if val == 'ELECTIVE':
            saps_adm = np.nanmax([0, saps_adm])
        elif val in ['EMERGENCY', 'URGENT']:
            saps_adm = np.nanmax([6, saps_adm])
        else:
            saps_adm = np.nanmax([np.nan, saps_adm])
    if df['admission_type'].isnull().all():
        saps_adm = 0

    if not df['age'].isnull().all():
        saps_age = pd.cut(df['age'],
                          bins=[-1, 40.0, 60.0, 70.0, 75.0, 80.0, 200],
                          labels=[0, 7, 12, 15, 16, 18]).max()

    if not df['bicarbonate'].isnull().all():
        saps_bicarb = pd.cut(df['bicarbonate'],
                             bins=[-1, 15.0, 20.0, 200.0],
                             labels=[5, 3, 0]).max()

    if not df['bilirubin'].isnull().all():
        saps_bili = pd.cut(df['bilirubin'],
                           bins=[-1, 4.0, 6.0, 40.0],
                           labels=[0, 4, 9]).max()

    if not df['blood_urea_nitrogen'].isnull().all():
        saps_bun = pd.cut(df['blood_urea_nitrogen'],
                          bins=[-1, 28.0, 84.0, 200.0],
                          labels=[0, 6, 10]).max()

    if df['glasgow_coma_scale_total'].isnull().all():
        saps_gcst = pd.cut(df['glasgow_coma_scale_total'],
                           bins=[-1, 5, 8, 10, 13, 15],
                           labels=[26, 13, 7, 5, 0]).max()

    if not df['heart_rate'].isnull().all():
        saps_hr = pd.cut(df['heart_rate'],
                         bins=[-1, 40.0, 70.0, 120.0, 160.0, 300.0],
                         labels=[11, 2, 0, 4, 7]).max()

    if not df['icd9'].isnull().all():
        for codes in df['icd9']:
            codes = pd.Series(codes)

            # HIV AND AIDS
            if codes.between('042', '0449').any():
                saps_icd9 = 17
            # Hematologic malignancy
            elif codes.between('20000', '20238').any() \
                    or codes.between('20240', '20248').any() \
                    or codes.between('20250', '20382').any() \
                    or codes.between('20400', '20522').any() \
                    or codes.between('20580', '20702').any() \
                    or codes.between('20720', '20892').any() \
                    or '2386' in codes \
                    or '2733' in codes:
                saps_icd9 = 10
            # Metastatic cancer
            elif codes.between('1960', '1991').any() \
                    or codes.between('20970', '20975').any() \
                    or '20979' in codes \
                    or '78951' in codes:
                saps_icd9 = 9

    if not df['potassium'].isnull().all():
        saps_pot = pd.cut(df['potassium'],
                          bins=[-1, 3.0, 5.0, 50.0],
                          labels=[3, 0, 3]).max()

    if not df['sodium'].isnull().all():
        saps_sod = pd.cut(df['sodium'],
                          bins=[-1, 125.0, 145.0, 300.0],
                          labels=[5, 0, 1]).max()

    if not df['systolic_blood_pressure'].isnull().all():
        saps_sbp = pd.cut(df['systolic_blood_pressure'],
                          bins=[-1, 70.0, 100.0, 200.0, 500.0],
                          labels=[13, 5, 0, 2]).max()

    if not df['temperature'].isnull().all():
        saps_temp = pd.cut(df['temperature'],
                           bins=[-1, 39.0, np.inf],
                           labels=[0, 3]).max()

    if not df['urine_output'].isnull().all():
        urine = df['urine'].sum()  # Urine measure is over 24 hours.
        if urine_output < 500.0:
            saps_urine = 11
        elif urine_output >= 500.0 and val < 1000.0:
            saps_urine = 4
        elif urine_output >= 1000.0:
            saps_urine = 0

    if not df['ventilated'].isnull().all():
        saps_vent = pd.cut(df['ventilated'],
                           bins=[-1, 100, 200, np.inf],
                           labels=[11, 9, 6])

    if not df['white_blood_cell_count'].isnull().all():
        saps_wbc = pd.cut(df['white_blood_cell_count'],
                          bins=[-1, 1.0, 20.0, 200.0],
                          labels=[12, 0, 3]).max()

    return sum([saps_adm, saps_age, saps_bicarb, saps_bili, saps_bun,
                saps_gcst, saps_gcsvr, saps_hr, saps_icd9, saps_pot,
                saps_sbp, saps_sod, saps_temp, saps_urine, saps_wbc])


def saps2_risk(score, b0=-7.7631, b1=0.0737, b2=0.9971):
    """Convert score to risk, default parameters taken from SAPS II paper.

    Parameters
    ----------
    score: float
        SAPS II score.
    """
    return 1 / (1 + np.exp(-(b0 + b1 * score + b2 * np.log(1 + score))))

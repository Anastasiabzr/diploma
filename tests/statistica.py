import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing


def stat(kod):
    t = pd.read_excel("date.xlsx")

    id_ = str(kod).strip().replace('.', ' ')
    x = 'Date'
    y = 'Average'
    horizon_ = 1
    season_type = 'mul'
    seas_period_ = 5

    df = pd.DataFrame(t)
    df1 = df.loc[df['ID'] == id_]
    DF = df1.drop_duplicates(keep='first', subset='Date')
    DF1 = DF.drop(columns=[1, 'Min', 'ID'], axis=1)

    d_ = DF1['Date'].tolist()
    p = d_[-1]+horizon_
    d_1 = np.append(d_, p)

    z_1 = DF1
    fit1 = ExponentialSmoothing(z_1['Average'], seasonal_periods = seas_period_, trend='add', seasonal=season_type, damped_trend=True).fit()
    fitted_ = fit1.predict(0, len(z_1) + horizon_ - 1)

    Df = np.round(fitted_, 2)
    df_f = pd.DataFrame(Df)

    df_f.columns = ['Average']
    df_f.insert(0, "Date", d_1, False)

    last = df_f['Average'].iloc[-1]
    return last

import pandas as pd
import numpy as np

CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

confirmed = pd.read_csv(CONFIRMED)
deaths = pd.read_csv(DEATHS)
recovered = pd.read_csv(RECOVERED)

confirmed.info()

confirmed.columns

confirmed.index

pl = confirmed['Country/Region'] == 'Poland'
pl = confirmed[pl].transpose()[4:]
pl.columns = ['Confirmed']
pl.index = pl.index.map(pd.to_datetime)

pl.last('W')
pl.loc['2021-12-10':'2021-12-23']


germany = confirmed['Country/Region'] == 'Germany'


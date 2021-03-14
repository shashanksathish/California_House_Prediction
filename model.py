import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

df = pd.read_csv("housing.csv")
le = preprocessing.LabelEncoder()
df['encoded_ocean'] = le.fit_transform(df['ocean_proximity'])

df_notnull = df.dropna()
df_notnull = df_notnull.drop(['longitude', 'latitude', 'ocean_proximity'], axis=1)
df_features = df_notnull[df_notnull.columns[~df_notnull.columns.isin(['median_house_value'])]]
df_predictval = df_notnull['median_house_value']

degree=4
polyreg = make_pipeline(PolynomialFeatures(degree),ElasticNet(random_state=0, alpha = 0.2))
polyreg.fit(df_features,df_predictval)

pickle.dump(polyreg, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
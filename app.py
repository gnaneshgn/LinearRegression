import numpy as np

from sklearn import datasets
from regression.linearmodels import LinearRegression
from sklearn.metrics import r2_score
from regression.logger import logging

X,y=datasets.make_regression(n_samples=200,n_features=1,noise=50)
logging.info("Sample data sets created")

regressor=LinearRegression(1000,0.01)
regressor.fit(X,y)
logging.info("fit applied")
y_pred=regressor.predict(X)
logging.info("predict applied")
print("R2 = {}".format(r2_scre(y_pred)))
logging.info("r2 score printed")
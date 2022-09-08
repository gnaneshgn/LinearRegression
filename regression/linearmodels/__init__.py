from regression.exception import LinearRegressionException
from regression.logger import logging
import numpy as np


class LinearRegression:
    
    def __init__(self,iteration_num=1000,learning_rate=0.01):
        self.lr=learning_rate
        self.itr=iteration_num
        self.weight=None
        self.bias =None


    def fit(self,X,y):
        rows,cols=X.shape
        logging.info("Initalizing weights and bias")
        self.weights=np.zeros(cols)
        self.bias=0
        logging.info("Initalizing gradient descent")
        for i in range(self.itr):
            logging.info("Intialized formula y=mx+c")
            y_pred=np.dot(x,self.weights)+self.bias
            logging.info("Intialized weights w and b")
            dw=(1/rows)*np.dot(X.T,(y_pred-y))
            db=(1/rows)*np.sum(y_pred-y)
            logging.info("Updating weigts and bias")
            self.weights=self.weights-self.lr*dw
            self.bias=self.bias-self.lr*db


    def predict(self,X):
        logging.info("Intialized formula y=mx+c during prediction")
        y_pred=np.dot(X,self.weights)+self.bias
        return y_pred
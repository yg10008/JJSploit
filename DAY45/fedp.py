import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

def load_application_train():
    data=pd.read_csv(r'C:\Users\trilo\Desktop\MLCNCPT\application_train.csv')
    return data 

def titanic():
    data=pd.read_csv(r'C:\Users\trilo\Desktop\MLCNCPT\titanic.csv')
    return data

df=titanic()
print(df.shape)

def outlier_thresholds(dataframe,colomn,q1=0.25,q3=0.75):
    q1=dataframe[colomn].quantile(q1)
    q3=dataframe[colomn].quantile(q3)
    iqr=q3-q1
    low=q1-1.5*iqr
    up=q3+1.5*iqr
    return low,up

def check_outliers(dataframe,colomn):
    low,up=outlier_thresholds(dataframe,colomn)
    if dataframe[(dataframe[colomn]< low) | (dataframe[colomn]>up)].any(axis=None):
        print('outliers exist')
    else:
        print('outliers not exist')

def grab_outliers(dataframe, col_name, outlier_index=False, f = 5):
    low, up = outlier_thresholds(dataframe, col_name)

    if dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].shape[0] > 10:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].head(f))
    else:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))])

    if outlier_index:
        out_index = dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].index
        return out_index

def remove_outliers(dataframe,col_name):
    low,up=outlier_thresholds(dataframe,col_name)
    dataframe_without_outliers=dataframe[~((dataframe[col_name]<low)|(dataframe[col_name]>up))]
    return dataframe_without_outliers

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit


print(outlier_thresholds(df, "Age"))
print(check_outliers(df, "Age"))  
print(check_outliers(df, "Fare")) 
age_index = grab_outliers(df, "Age", True)
print(age_index)

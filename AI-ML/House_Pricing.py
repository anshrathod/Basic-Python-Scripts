import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

pd.options.mode.chained_assignment = None  # default='warn' #To not show a warning shown due to pandas


path1="train.csv"
path2="test.csv"

train_data=pd.read_csv(path1)
test_data=pd.read_csv(path2)




train_data.dropna(subset=["SalePrice"],axis=0,inplace=True)#drop rows with empty value of price


train_data.dropna(subset=["SalePrice"],axis=0,inplace=True) #drop rows with empty value of price


train_y=train_data.SalePrice
train_data.drop(["SalePrice"],axis=1,inplace=True)
train_X=train_data
test_X=test_data


#seperating object columns
columns=train_data.columns
object_cols=[]
for i in columns:
    if train_data[i].dtype==object:
        object_cols.append(i)

#seperating non object columns
non_object_cols=[]

for j in columns:
    if j not in object_cols:
        non_object_cols.append(j)

#good and bad label columns
good_label_cols=[]
bad_label_cols=[]

for j in object_cols:
    if set(train_X[j])==set(test_X[j]):
        good_label_cols.append(j)
    else:
        bad_label_cols.append(j)

#dropping bad labels
train_X.drop(bad_label_cols,axis=1,inplace=True)
test_X.drop(bad_label_cols,axis=1,inplace=True)




#cardinality

low_cardinality=[]
high_cardinality=[]

for p in good_label_cols:
    if train_X[p].nunique()<10:
        low_cardinality.append(p)
    else:
        high_cardinality.append(p)

#one-hot encoding of object columns
encoder=OneHotEncoder(handle_unknown="ignore",sparse=False)
OH_cols_train=pd.DataFrame(encoder.fit_transform(train_X[low_cardinality]))
OH_cols_test=pd.DataFrame(encoder.transform(test_X[low_cardinality]))

OH_cols_train.index=train_X.index
OH_cols_test.index=test_X.index

num_X_train=train_X.drop(low_cardinality,axis=1)
num_X_test=test_X.drop(low_cardinality,axis=1)

OH_train_X_1=pd.concat([num_X_train,OH_cols_train],axis=1)#no inplace to be used
OH_test_X_1=pd.concat([num_X_test,OH_cols_test],axis=1)#no inplace to be used

#dropping high cardinality columns
OH_train_X=OH_train_X_1.drop(high_cardinality,axis=1)#no inplace to be used
OH_test_X=OH_test_X_1.drop(high_cardinality,axis=1)#no inplace to be used


#Simple Imputer
imputer=SimpleImputer(strategy="mean")
imputed_train_X=pd.DataFrame(imputer.fit_transform(OH_train_X))
imputed_test_X=pd.DataFrame(imputer.transform(OH_test_X))

#print(train_y.head)
#print(imputed_train_X.head)
#Found input variables with inconsistent numbers of samples: [2920, 1460]

#model fitting and predictions
model=RandomForestRegressor(n_estimators=100)
model.fit(imputed_train_X,train_y)
predictions=model.predict(imputed_test_X)


#write to csv file
output=pd.DataFrame({"Id":test_data.index,"SalePrice":predictions})
output.to_csv("submission.csv",index=False)


#The score for this code was 16495.85229

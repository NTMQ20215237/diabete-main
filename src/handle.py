import sys
import pandas as pd
import numpy as np

import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

df= pd.read_csv('src/diabetes.csv')

test1File = open('src/test.csv','w')
test1File.write('Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age\n')

# input value into test file 
glu = sys.argv[2]
pregnancy = sys.argv[1]
BloodPresure = sys.argv[6]
Skinthinknss= 35
insulin = sys.argv[5]
BMI = sys.argv[3]
diabetPredictFuntion=0.68
Age= sys.argv[4]
inputS = f"{pregnancy},{glu},{BloodPresure},{Skinthinknss},{insulin},{BMI},{diabetPredictFuntion},{Age}"
test1File.write(inputS)

test1File.close()
test1=pd.read_csv('src/test.csv')
# drop outcome 
X = df.drop("Outcome",axis=1)
y= df["Outcome"]
X_train = X.iloc[:598]
X_test = X.iloc[598:]
y_train = y[:598]
y_test = y[598:]
    # print("X_train Shape: ",X_train.shape)
    # print("X_test Shape: ",X_test.shape)
    # print("y_train Shape: ",y_train.shape)
    # print("y_test Shape: ",y_test.shape)
logistic_regression = LogisticRegression(random_state=0,solver="liblinear").fit(X_train,y_train)

logistic_regression.intercept_

# coef 
logistic_regression.coef_

# start model 
lr_statsmodel = sm.Logit(y_train,X_train).fit()

# prdiction 
y_pred = logistic_regression.predict(X_test)
#  we can buil data and replace X_test by realitic data
results = logistic_regression.predict(test1)
# print(results)

# confuse matrix 
# cm = confusion_matrix(y_test,y_pred)
# print(cm)

# accuracy
accuracies = cross_val_score(estimator=logistic_regression,
                            X=X_train,y=y_train,
                            cv=30)
# we can increase the accuracy of the model by increasing the datatest(max when cv >20)
# accuracy depends on the trained data by the command 
        # print("Average Accuracy: {:.2f} %".format(accuracies.mean()*100))
        # print("Standart Deviation of Accuracies: {:.2f} %".format(accuracies.std()*100))
#  K-Fold Cross Validation

# results2 =pd.DataFrame(logistic_regression.predict_proba(test1),
#                 columns=["Possibility of 0","Possibility of 1"])

# results2["Class"]=[1 if i>0.5 else 0 for i in results2["Possibility of 1"]]
# print(results2)
result3 = logistic_regression.predict_proba(test1)
x= result3[0][1]*100
print(x)



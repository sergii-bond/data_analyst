import numpy
import pandas as pd
import statsmodels.api as sm

#def custom_heuristic(file_path):
'''
You are given a list of Titantic passengers and their associated
information. More information about the data can be seen at the link below:
http://www.kaggle.com/c/titanic-gettingStarted/data

For this exercise, you need to write a custom heuristic that will take
in some combination of the passenger's attributes and predict if the passenger
survived the Titanic diaster.

Can your custom heuristic beat 80% accuracy?

The available attributes are:
Pclass          Passenger Class
                (1 = 1st; 2 = 2nd; 3 = 3rd)
Name            Name
Sex             Sex
Age             Age
SibSp           Number of Siblings/Spouses Aboard
Parch           Number of Parents/Children Aboard
Ticket          Ticket Number
Fare            Passenger Fare
Cabin           Cabin
Embarked        Port of Embarkation
                (C = Cherbourg; Q = Queenstown; S = Southampton)
                
SPECIAL NOTES:
Pclass is a proxy for socioeconomic status (SES)
1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

Age is in years; fractional if age less than one
If the age is estimated, it is in the form xx.5

With respect to the family relation variables (i.e. SibSp and Parch)
some relations were ignored. The following are the definitions used
for SibSp and Parch.

Sibling:  brother, sister, stepbrother, or stepsister of passenger aboard Titanic
Spouse:   husband or wife of passenger aboard Titanic (mistresses and fiancees ignored)
Parent:   mother or father of passenger aboard Titanic
Child:    son, daughter, stepson, or stepdaughter of passenger aboard Titanic

Write your prediction back into the "predictions" dictionary. The
key of the dictionary should be the passenger's id (which can be accessed
via passenger["PassengerId"]) and the associating value should be 1 if the
passenger survvied or 0 otherwise. 

For example, if a passenger is predicted to have survived:
passenger_id = passenger['PassengerId']
predictions[passenger_id] = 1

And if a passenger is predicted to have perished in the disaster:
passenger_id = passenger['PassengerId']
predictions[passenger_id] = 0

You can also look at the Titantic data that you will be working with
at the link below:
https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
'''

predictions = {}
df = pd.read_csv("titanic_data.csv")
df['Survived'] = df['Survived'].astype('category')
del df['Name']
del df["Ticket"]
del df["PassengerId"]
#del df["Cabin"]
df.describe(include = 'all')
df.mode()
df.Survived.value_counts()
df_f = df[df['Sex'] == 'female']
df_f.describe(include = 'all')
df_m = df[df['Sex'] == 'male']
df_m.describe(include = 'all')
df_1 = df[df["Pclass"] == 1]
df_1.head(20)
df_1.describe(include = 'all')
df[(df["Pclass"] == 1) & (df["Sex"] == 'female')].Survived.value_counts()
df_m1 = df[(df["Pclass"] == 1) & (df["Sex"] == 'male')]
df_m1.Survived.value_counts()
df_m1.head(40)
df_m1[(df_m1["Parch"] > 0) & (df_m1["Age"] < 18)].Survived.value_counts()
df_m1.to_csv("titanic_data_m1.csv")
df[(df["Pclass"] == 2) & (df["Sex"] == 'female')].Survived.value_counts()

df_m2 = df[(df["Pclass"] == 2) & (df["Sex"] == 'male')]
df_m2.Survived.value_counts()
df_m2[(df_m2["Parch"] > 0) & (df_m2["Age"] < 18)].Survived.value_counts()
#df[(df["Pclass"] == 1) & (df["Parch"] > 0) & (df["Age"] < 18)].Survived.value_counts()

df_f3 = df[(df["Pclass"] == 3) & (df["Sex"] == 'female')]
df_f3.Survived.value_counts()
df_f3.to_csv("titanic_data_f3.csv")
df_f3[df_f3["Age"] > 40].Survived.value_counts()
#df_f3[(df_f3["Parch"] > 0) & (df_f3["Age"] < 18)].Survived.value_counts()
df_m3 = df[(df["Pclass"] == 3) & (df["Sex"] == 'male')]
df_m3.Survived.value_counts()
df_m3[df_m3["Age"] > 40].Survived.value_counts()
#df_m3[(df_m3["Parch"] > 0) & (df_m3["Age"] < 18)].Survived.value_counts()

for passenger_index, passenger in df.iterrows():
    #
    # your code here
    #
    passenger_id = passenger['PassengerId']
    if (passenger['Sex'] == 'female' and passenger['Pclass'] < 3) or \
        (passenger['Sex'] == 'male' and passenger['Pclass'] < 3 \
            and passenger['Age'] < 18 and passenger['Parch'] > 0):
        predictions[passenger_id] = 1
    else:
        #if (passenger['Sex'] == 'female' and passenger['Pclass'] == 3):
        #    x = np.random.randint(0, 2)
        #    if x == 0:
        #        predictions[passenger_id] = 0
        #    else:
        #        predictions[passenger_id] = 1
        #else:
        predictions[passenger_id] = 0
    if (passenger['Pclass'] == 3 and passenger['Age'] > 40):
        predictions[passenger_id] = 0
#return predictions


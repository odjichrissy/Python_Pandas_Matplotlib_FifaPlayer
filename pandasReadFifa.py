import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
# print(df[['Name','Age','Overall']])

age = df['Age']
skill = df['Overall']

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('Age')
axes.set_ylabel('Skill')
axes.set_title('Age VS Skill')

age1 = []
skill1 = []
age2 = []
skill2 = []
age3 = []
skill3 = []
age4 = []
skill4 = []
age5 = []
skill5 = []
age6 = []
skill6 = []

for i in range(len(age)):
        if age[i]>=30 and skill[i]>=80:
                age1.append(age[i])
                skill1.append(skill[i])
        elif age[i]>=30 and skill[i]<80:
                age2.append(age[i])
                skill2.append(skill[i])
        elif age[i]<30 and age[i]>20 and skill[i]>=80:
                age3.append(age[i])
                skill3.append(skill[i])
        elif age[i]<30 and age[i]>20 and skill[i]<80:
                age4.append(age[i])
                skill4.append(skill[i])
        elif age[i]<=20 and skill[i]>80:
                age5.append(age[i])
                skill5.append(skill[i])
        else:
                age6.append(age[i])
                skill6.append(skill[i])

plt.scatter(age1,skill1, color='b', marker="o")
plt.scatter(age2,skill2, color='g', marker="o")
plt.scatter(age3,skill3, color='r', marker="o")
plt.scatter(age4,skill4, color='c', marker="o")
plt.scatter(age5,skill5, color='m', marker="o")
plt.scatter(age6,skill6, color='y', marker="o")

plt.legend(['Old but good','Old and normal','Mature but good','Mature and bad','Young and good','Young and raw'],loc='upper right')

plt.show()

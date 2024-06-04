import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#importing the dataset 
df=pd.read_csv('C:\\Users\\HP\\Downloads\\heart.csv')
#check the first 5 rows
print(df.head())
#gives the data of bottom 5 rows
print(df.tail())
#to get the column names
print(df.columns.values)
#checking for the null values
print(df.isna().sum())
#concise summary of our dataset
print(df.info())
#plotting the histogram of all numeric values
print(df.hist(bins=50, grid = False, figsize=(20,15)))
plt.show()
#description statistics
print(df.describe())

question=['1.How many people have heart disease and how many doesnt have heart disease?',
          '2.How many people have chest pain and how many doesnt have chest pain?',
          '3.How many people have resting blood pressure and how many doesnt have resting blood pressure?',
          '4.How many people have serum cholestrol and how many doesnt have serum cholestrol',
          '5.How many people have fasting blood sugar and how many doesnt have fasting blood sugar?',
          '6.People of which sex have the most heart disease ?',
          '7.Peope of which sex has which type of chest pain most ?',
          '8.People with which chest pain are most pron to have heart disease ?']

#1.How many people have heart disease and how many doesnt have heart disease?
print(df.target.value_counts())
#plotting bar chart
print(df.target.value_counts().plot(kind='bar',color=["green","yellow"]))
plt.title("1.Heart Disease")
plt.xlabel("1=Heart Disease, 0=No Heart Disease")
plt.ylabel("Amount")
plt.show()
#plotting a pie chart
df.target.value_counts().plot(kind='pie', figsize=(5,6))
plt.legend(["Disease","No disease"])
plt.show()


#0-Female
#1-Male
#0-No disease
#1-Disease
print(df.sex.value_counts())
#plotting a pie chart
df.sex.value_counts().plot(kind='pie', figsize=(5,6))
plt.title("Female and Male ratio")
plt.legend(["Female","Male"])
plt.show()


#2.How many people have chest pain and how many doesnt have chest pain?
print(df.cp.value_counts())
#plotting a bar chart
print(df.cp.value_counts().plot(kind='bar',color=["green","yellow"]))
plt.title("2.Chest Pain")
plt.xlabel("1=normal, 2=medium, 3=danger")
plt.ylabel("Amount")
plt.show()


#3.How many people have resting blood pressure and how many doesnt have resting blood pressure?'
print(df.trestbps.value_counts())
#plotting a bar chart
print(df.trestbps.value_counts().plot(kind='bar',color=["green","yellow"]))
plt.title("3.Resting Blood Pressure")
plt.show()


#4.How many people have cholesterol and how many doesnt have cholesterol?
print(df.chol.value_counts())
#plotting a bar chart
print(df.chol.value_counts().plot(kind='bar',color=["green","yellow"]))
plt.title("4.Cholesterol")
plt.show()

#5.How many people have fasting blood sugar and how many doesnt have fasting blood sugar?
print(df.fbs.value_counts())
#plotting a bar chart
print(df.fbs.value_counts().plot(kind='bar',color=["green","yellow"]))
plt.title("5.Fasting Blood Sugar")
plt.show()

#6.People of which sex have the most heart disease ?
print(pd.crosstab(df.target, df.sex))
#plotting a bar chart
sns.countplot(x='target', data=df, hue='sex')
plt.title("6.Heart Disease frequency for Sex")
plt.xlabel("0=No Heart disease, 1=Heart disease")
plt.show()


#7.Peope of which sex has which type of chest pain most ?
print(df.cp.value_counts())
#plotting a bar chart
df.cp.value_counts().plot(kind='bar', color=['lightskyblue','yellow','red','green'])
plt.title("7.Chest Pain type vs count")
plt.show()
pd.crosstab(df.sex, df.cp)
#plotting a bar chart
pd.crosstab(df.sex, df.cp).plot(kind='bar', color=['lightskyblue','yellow','red','green'])
plt.title("Type of chest pain for sex")
plt.xlabel('0=Female, 1=Male')
plt.show()


#8.People with which chest pain are most pron to have heart disease ?
print(pd.crosstab(df.cp, df.target))
#plotting a bar chart
sns.countplot(x='cp', data=df, hue='target')
plt.title("8.Heart Disease frequency for Chest Pain")
plt.show()


#creating a distribution plot with normal distribution curve
sns.displot(x='age', data=df, bins=30, kde=True)
plt.title("Age distribution")
plt.show()

#maximum heart rate
sns.displot(x='thalach', data=df, bins=30, kde=True, color='chocolate')
plt.title("Maximum heart rate distribution")
plt.show()




















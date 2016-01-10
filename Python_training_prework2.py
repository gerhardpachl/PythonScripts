# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:40:06 2016
Exercise: reading and cleaning dataset of titanic passengers (train.csv)
using the pandas package based on tutorial: Getting started with Kaggle
"""
# initialize pandas
import pandas

# get the passenger data
titanic = pandas.read_csv("C:/Users/C924016/MyPythons/CSV/train.csv")
print(titanic.describe())
print(titanic.head(5))

# replace the missing values of variable "Age" with median value of variable "Age"
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

# for non numeric values like gender, we put codes instead of texts
print(titanic["Sex"].unique())

# 0 for male and 1 for female
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

# Converting the Embarked column
print(titanic["Embarked"].unique())

# Replace all the missing values in the Embarked column with S.
# Code 0 to S, 1 to C and 2 to Q
print(titanic["Embarked"].unique())
titanic["Embarked"] = titanic["Embarked"].fillna("S")
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

print(titanic.head(5))
























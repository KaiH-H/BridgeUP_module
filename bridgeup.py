# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")


# Creates function to get Cohort from Name
def student_cohort(name):

	first_name = df["First Name"]

	cohort = df["Cohort"].loc[first_name == name] # USE BRACKETS W/ .LOC[]

	return cohort


#tells you how many people have the same fav animal as you
def animal_num(animal):
	an = df["Fav animal"]
	c = 0
	for i in an:
		if i == animal:
			c+=1
	return c


#Takes the name of student and returns their favorite ice cream flavor

def student_flavor(Name):
	Flavor = df["Fav ice cream flavor"].loc[df["First Name"] == Name]

	return Flavor

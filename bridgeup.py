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

#This function takes in a student name and returns their favorite season.
import pandas as pd
df = pd.read_csv("internship_bootcamp_data.csv")
def student_season(name):
	season = df["Fav season"].loc[df["First Name"] == name]
	return season
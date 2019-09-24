import pandas as pd
df = pd.read_csv("internship_bootcamp_data.csv")


# Creates function to get Cohort from Name
def student_cohort(name):

	first_name = df["First Name"]

	cohort = df["Cohort"].loc[first_name == name] # USE BRACKETS W/ .LOC[]

	return cohort
=======
#goes through the favorite color list and counts how many like a specific color
def color_num(color):
	stud_color = df["Fav color"]
	counter = 0
	for i in stud_color:
		if i == color:
			counter += 1
	return counter


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

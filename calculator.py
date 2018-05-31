# Calculator for BMI, Calories, and Macronutrients

# Name: Fit-Calc

# Greet/Determine user needs:

print("Hello! Welcome to Fit-Calc!")
print(" ")
print("What would you like to do? ")
print("1. Calculate Macronutrients")
print("2. Calculate BMI")
print("3. Calculate suggested calorie intake")
print(" ")
choice = input("Please enter your answer here (1/2/3): ")

# Create class of functions used for generating all user desired outputs 

class Person():
	def __init__(self, weight, weightkg, height, p, c, f):
		self.weight   = weight
		self.weightkg = weightkg   #Converted to kilograms for BMI
		self.height   = height  #Converted to meters for BMI
		self.p        = p
		self.c        = c
		self.f        = f

	def macro_protein(self):		  ## MacroNutrient Calculations
		return self.weight*self.p
	def macro_carb(self):
		return self.weight*self.c
	def macro_fat(self):
		return self.weight*self.f     ##
	def calc_bmi(self):				  # BMI Calculation
		return (self.weightkg) / (self.height*self.height)
	def calc_calorie(self):			  # Calorie Calculation
		return (4*(self.weight*self.p)) + (4*(self.weight*self.c)) + (9*(self.weight*self.f))

# Define variables to be used in class

weight   = int(input("Enter your weight in pounds here: "))
weightkg = weight*0.45
height   = int(input("Enter your height in inches here: "))
height   = height*0.025
p = 1.2 ## Macronutrient Constants 
c = 1
f = 0.2	##
obj=Person(weight, weightkg, height, p, c, f)

# Implementation of control structures to differentiate user needs

if choice == "1":
	print("Your daily macronutrients should be as follows: ")
	print("Protein: ",obj.macro_protein()," Grams.")
	print("Carbohydrates: ",obj.macro_carb()," Grams.")
	print("Fat: ",obj.macro_fat()," Grams.")
	choice = input("Would you also like to see your suggested daily calorie intake? (y/n): ")  
	if choice == "y":
		print("Your suggested daily calorie intake is: ",obj.calc_calorie()," Calories.")
		exit()
	elif choice == "n":
		print("Thanks for using Fit-Calc!")
		exit()

if choice == "2":
	print("Your BMI, or Body Mass Index, is: ",obj.calc_bmi())
	exit()

if choice == "3":
	print("Your suggested daily calorie intake is: ",obj.calc_calorie()," Calories.")
	choice = input("Would you also like to know your suggested macronutrients? (y/n): ")
	if choice == "y":
		print("Your daily macronutrients should be as follows: ")
		print("Protein: ",obj.macro_protein()," Grams.")
		print("Carbohydrates: ",obj.macro_carb()," Grams.")
		print("Fat: ",obj.macro_fat()," Grams.")
		exit()
	elif choice == "n":
		print("Thanks for using Fit-Calc!")
		exit()

else:
	print("Oh no! Looks like something went wrong. Make sure you entered in a valid response. Please restart.")
	exit()  



#Create class of functions used for generating all user desired outputs 
class Person():
	def __init__(self, weight, weightkg, height, p, c, f):
		self.weight   = weight
		self.weightkg = weight*0.45   #Converted to kilograms for BMI
		self.height   = height*0.025  #Converted to meters for BMI
		self.p        = p
		self.c        = c
		self.f        = f

	def macro_protein(self):                  ## MacroNutrient Calculations
		return self.weight*self.p
	def macro_carb(self):
		return self.weight*self.c
	def macro_fat(self):
		return self.weight*self.f             ##
	def calc_bmi(self):				          # BMI Calculation
		return (self.weightkg) / (self.height*self.height)
	def calc_calorie(self):			          # Calorie Calculation
		return (4*(self.weight*self.p)) + (4*(self.weight*self.c)) + (9*(self.weight*self.f))



# Import code to be tested

from calculatorClass import Person
from pytest import approx

# Write a Smoke Test

def test_smoke():
	assert True == True

# Test class

Armin = Person(175, 78.75, 69, 1.2, 1, .2)

def test_macro_protein():
	assert Armin.macro_protein() == 210
def test_macro_carb():
	assert Armin.macro_carb() == 175
def test_macro_fat():
	assert Armin.macro_fat() == 35
def test_calc_bmi():
	assert Armin.calc_bmi() == approx(26, abs=1)
def test_calc_calorie():
	assert Armin.calc_calorie() == 1855




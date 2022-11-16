# This is the beginning of the file that Elliot went through in class
#
# Project Requirements:
#	Able to convert between common metric and Imperial cooking units of measure including mass, volume (liquid and bulk),
#	and temperature.
#	Eggs to cups
#	Kg to lbs
#	Tsp to cups
#
#	Tsp, Tbsp, Cups, Pints, Quarts, Fl. Oz., Lbs, Gal, Oz, Kg, G, L, mL, Farenheit, Celsius, Kelvin
#
#	Command-Line Interface
#		"Convert 6 tbsp to cups"
#		"7.2 Kg to lbs"
#
#
#

class Unit:
  def __init__(self, unitname, convertsto, conversionfactor):
    self.unitname = unitname
    self.convertsto = convertsto
    self.conversionfactor = conversionfactor

def convert(s):
  [from_, to_] = s.split(' to ')

  for i in [Unit('kg', ['lbs', 'g'], [2.205, 1000]),
            Unit('lbs', ['oz', 'kg'], [16, 1 / 2.205])]:
      if from_.endswith(i.unitname):
          val = float(from_.removesuffix(i.unitname))
          ind = i.convertsto.index(to_)
          print(val * i.conversionfactor[ind])

convert("7.2kg to lbs")
convert("3lbs to oz")
convert("7.2kg to g")
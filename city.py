# Author = Okorie Rehoboth
# Date = Feb 24th 2020
# Purpose = Read from a file into a class


# define the class
class City:
    # get the instance variables
    def __init__(self, country, city, region, population, latitude, longitude):
        self.country = country
        self.city = city
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    # get the print output for the class
    def __str__(self):
        return str(self.city)+","+str(self.population)+","+str(self.latitude)+","+str(self.longitude)

# # Author: Rehoboth Okorie
# # Purpose: Sort a list using quick sort algorithm

from city import City
from quicksort import *

# -----------------------------------------------------------------------------------------------

# make city list
text = open("world_cities.txt", "r")

# create empty list that will hold the info form world_cities
city_list = []

# initiate loop process the lines in world_cities into a City object and append into city_list
for i in text:

    # remove the new line escape character and break up the lines into the components
    info = (i.strip("\n").split(","))

    # append new city object to city_list
    city_list.append(City(info[0], info[1], info[2], info[3], info[4], info[5]))

# close file
text.close()


# -----------------------------------------------------------------------------------------------


def cat_sort(fileout, compare_func, glist):

    # sort by criteria in compare_func
    outfile = open(fileout, "w")

    # call sort on city_list but pass in the latitude compare func
    sort(glist, compare_func)

    # iterate through latitude sorted city_list and write into file
    for j in range(len(glist)):
        if j < len(glist) - 1:
            outfile.write(str(glist[j]) + "\n")
        else:
            outfile.write(str(glist[j]))

    # close file
    outfile.close()


# -----------------------------------------------------------------------------------------------

# call the cat_sort func to sort alphabetically, by population and by latitude respectively
cat_sort("cities_alpha", compare_alpha, city_list)
cat_sort("cities_population", compare_pop, city_list)
cat_sort("cities_latitude", compare_lat, city_list)

# Author: Rehoboth Okorie
# Purpose: Draw the city location to a world map
# Date: Feb 28th 2020

from cs1lib import *

# load the world map image
world = load_image("world.png")

# scale the window to a pixel to latitude conversion
lon_scale = 360 / 180
lat_scale = -180 / 90

# g_num is the record of how many cities drawn and the check to limit the number of cities drawn
g_num = 1

# holds the list of the cities that have already been drawn and receives the next city
alist = []
blist = []
btext = []

# ----------------------------------------------------------------------------


def search_city():
    global blist
    city_name = input("What city are you looking for? ")
    get_cities("cities_population", alist)
    for i in alist:
        if i[0].lower() == city_name.lower():
            blist.append(i)
            btext.append(i[0] + ", Population: " + str(i[1]))


# ----------------------------------------------------------------------------


# function that gets the cities from a file and adds them to alist
def get_cities(city, glist):
    # open the file
    text = open(city, "r")

    # iterate thorough CSV file and split them at the commas
    for i in text:
        info = i.strip("\n").split(",")

        # append the stripped and split info to alist ## !NOTE alist will be a list of lists ##
        glist.append([info[0], info[1], info[2], info[3]])

    # close text
    text.close()


# ----------------------------------------------------------------------------

# function to be called by start graphics; draws the cities onto the map
def draw_map():
    # so g_num can be updated by every frame cycle
    global g_num

    # draws the map onto the window
    draw_image(world, 0, 0)
    set_fill_color(1, 0, 1)

    for i in range(g_num):
        draw_circle(float(blist[i][3]) * lon_scale + 360, float(blist[i][2]) * lat_scale + 180, 8)

    if g_num < len(blist):
        g_num += 1
    else:
        g_num = 1


# ----------------------------------------------------------------------------
search_city()
# CALL STARTGRAPHICS!!
start_graphics(draw_map, width=720, height=360, framerate=1)

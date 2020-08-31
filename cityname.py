# Author: Rehoboth Okorie
# Purpose: Draw the city location to a world map
# Date: Feb 28th 2020

from cs1lib import *

# load the world map image
world = load_image("world.png")

# scale the window to a pixel to latitude conversion
lon_scale = 360 / 180
lat_scale = -180 / 90

# hy = 29.7630556
# hx = -95.3630556

# g_num is the record of how many cities drawn and the check to limit the number of cities drawn
g_num = 1

# holds the list of the cities that have already been drawn and receives the next city
alist = []


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

    # sets fill color for the current city to be drawn
    set_fill_color(0, 1, 1)
    # call the get cities function of the file "cities_population"
    get_cities("cities_population", alist)
    # draw the current city to be drawn in blue in a bigger size
    draw_circle(float(alist[g_num][3]) * lon_scale + 360, float(alist[g_num][2]) * lat_scale + 180, 5)
    # display the name of the city
    draw_text(alist[g_num][0], float(alist[g_num][3]) * lon_scale + 360, float(alist[g_num][2]) * lat_scale + 180)

    # iterates through file and draws a circle with the x, y value to the scaled longitude and latitude scale converted
    for i in range(g_num):
        # fill color for all cities already drawn
        set_fill_color(1, 0, 0)
        draw_circle(float(alist[i][3]) * lon_scale + 360, float(alist[i][2]) * lat_scale + 180, 3)

    #  limits the number of cities drawn to the first 50
    if g_num < 50:
        g_num += 1
    # draw_circle(hx * lon_scale + 360, hy * lat_scale + 180, 3)


# ----------------------------------------------------------------------------
# CALL STARTGRAPHICS!!
start_graphics(draw_map, width=720, height=360, framerate=1)

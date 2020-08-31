# Author: Rehoboth Okorie
# Purpose: Sort a list using quick sort algorithm

from random import *

# ------------------------------------------------------------------------------------------------


# sort largest to least; for population
def compare_pop(item1, item2):
    return item2.population < item1.population


# ------------------------------------------------------------------------------------------------


# sorts least to largest; for alphabets
def compare_alpha(item1, item2):
    return item1.city.lower() < item2.city.lower()


# ------------------------------------------------------------------------------------------------


# sorts least to largest; for latitude
def compare_lat(item1, item2):
    return item1.latitude < item2.latitude


# ------------------------------------------------------------------------------------------------


# chooses last value as pivot and separates least into greater than pivot and less than pivot
def partition(glist, border, pivot, compare_func):

    # considers only values between border and pivot
    for i in range(border, pivot):

        # based on the compare func call separates the list
        if compare_func(glist[i], glist[pivot]):

            # switches the positions of the value at i with the value at the border if compare_func is True
            glist[i], glist[border] = glist[border], glist[i]
            border += 1

    # puts the pivotvalue into the border so the list is perfectly divide by the pivotvalue and returns border
    glist[border], glist[pivot] = glist[pivot], glist[border]
    return border


# ------------------------------------------------------------------------------------------------


def quicksort(glist, low, high, compare_func):
    # recursively calls partition as long as the entry border position < the pivot position i.e the list is not empty
    if low < high:

        # gets the value of the former pivotvalue or the former border
        point = partition(glist, low, high, compare_func)

        # calls partition on the values to the left of the former pivotvalue, pivotvalue not inclusive
        quicksort(glist, low, point-1, compare_func)

        # calls partition on the values to the right of the former pivotvalue, pivot value not inclusive
        quicksort(glist, point+1, high, compare_func)


# ------------------------------------------------------------------------------------------------


def sort(glist, compare_func):
    n = len(glist)-1
    x = randint(0, n)
    glist[x], glist[n] = glist[n], glist[x]
    quicksort(glist, 0, n, compare_func)

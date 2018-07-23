# Search Nearest Neighbors from dataset
# using my location (lat long coordinat)

import math
loc = [[-9.455, 112.876],[-9.235, 112.890],[-9.334, 112.891]]
my_loc = [-9.234,112.89]
my_lat = -9.234
my_lon = 112.89
# jarak = math.sqrt((my_loc[0]-loc[0][0])**2 + (my_loc[1]-loc[0][1])**2)
# print (jarak)
panjang_data = (len(loc))
for i in range(panjang_data):
    distance = math.sqrt((my_lat-loc[i][0])**2 + (my_lon-loc[i][1]))
    if i == 0:
        min_distance = distance
    else:
        if distance < min_distance:
            min_distance = distance
        # min_distance = 1
        # slat = loc[i][0]
        # slon = loc[i][1]
        # print i,slat, slon
    print (min_distance)

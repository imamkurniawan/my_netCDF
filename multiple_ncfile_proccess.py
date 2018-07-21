from netCDF4 import Dataset
import numpy as np

def extractNC(nc_file):
    fh = Dataset(nc_file, mode='r')
    lons = fh.variables['lon'][:]
    lats = fh.variables['lat'][:]
    prec = fh.variables['precipitationCal'][:]
    prec_units = fh.variables['precipitationCal'].units
    for x in range(len(lons)):
        for y in range(len(lats)):
            # print nc_file, x, y, lons[x],lats[y], prec[x,y] 
            out = nc_file+" "+str(x)+" "+str(y)+" "+str(lons[x])+" "+str(lats[y])+" "+str(prec[x,y])+ "\r\n"
            out_file.write(out)
    fh.close()

import os
path = 'D:\\IMERG_DATA\NTB\\'
files = os.listdir(path)
out_file = open("out.txt","w")

for name in files:
    full_name = path+name
    baris = extractNC(full_name)


from netCDF4 import Dataset
import numpy as np

def extractNC(nc_file):
    
    # nc_file = 'Z:\\IMERG_DATA\NTB\\3B-DAY.MS.MRG.3IMERG.20161231-S000000-E235959.V05.nc4.nc'
    # return nc_file
    
    # nc_file = nc_file
    fh = Dataset(nc_file, mode='r')
    lons = fh.variables['lon'][:]
    lats = fh.variables['lat'][:]
    prec = fh.variables['precipitationCal'][:]
    prec_units = fh.variables['precipitationCal'].units
    for x in range(len(lons)):
        for y in range(len(lats)):
            print nc_file,
            print x,
            print y,
            print lons[x],
            print lats[y],
            print prec[x,y]    
    # fh.close()

import os
path = 'Z:\\IMERG_DATA\NTB\\'
files = os.listdir(path)
for name in files:
    full_name = path+name
    # print full_name
    extractNC(full_name)

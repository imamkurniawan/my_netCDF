from netCDF4 import Dataset
import numpy as np
nc_file = 'D:\\IMERG_DATA\NTB\\3B-DAY.MS.MRG.3IMERG.20161231-S000000-E235959.V05.nc4.nc'
fh = Dataset(nc_file, mode='r')
lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]
prec = fh.variables['precipitationCal'][:]
prec_units = fh.variables['precipitationCal'].units
for x in range(len(lons)):
    for y in range(len(lats)):
        print x,
        print y,
        print lons[x],
        print lats[y],
        print prec[x,y]
fh.close()

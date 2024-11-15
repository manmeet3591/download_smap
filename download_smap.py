import ee
import os

# Set the path to the service account key file
service_account = 'editor@ee-manmeet20singh15-wbis.iam.gserviceaccount.com'
key_file = '/scratch/08105/ms86336/SMAPL4/ee-manmeet20singh15-wbis-fab7f1ca35e0.json'

# Use the service account for authentication
credentials = ee.ServiceAccountCredentials(service_account, key_file)
ee.Initialize(credentials)

import ee
import wxee

lat_diff = 0
lon_diff = 0
#aoi = ee.Geometry.Polygon(
#        [[[-125, 32],
#          [-113, 32],
#          [-113, 42],
#          [-125, 42]]])
minlat = 29.7
maxlat = 30.7
minlon = -99.0
maxlon = -98.0
aoi = ee.Geometry.Polygon(
        [[[minlon, minlat],
          [maxlon, minlat],
          [maxlon, maxlat],
          [minlon, maxlat]]])

coords = aoi.coordinates().getInfo()[0]

start_date = '2016-01-01'
end_date = '2016-01-02'
dataset = ee.ImageCollection('NASA/SMAP/SPL4SMGP/007').filterDate(start_date, end_date).select('sm_surface')
ds_smap = dataset.wx.to_xarray(region=aoi.bounds(), scale=11000)

ds_smap.to_netcdf('smap_test.nc')

# This script contains functions to download the DOT18, DOT19 and DOT20 datasets from DataWA via WebAPI services.
import geopandas as gpd
import requests
from pyproj import CRS
from owslib.wfs import WebFeatureService

dot_18_url = ""
dot_19_url = ""
dot_20_url = ""

# for loop for parameters
params = dict(
    service="",
    version="",
    request="",
    typeName="",
    outputFormat="",
)

#for loop for requests
dot_18_requet

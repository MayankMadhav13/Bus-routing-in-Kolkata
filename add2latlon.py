# -*- coding: utf-8 -*-
"""Add2LatLon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ihlIltuux8lP2rQnj1UDt3BIvtCMPsxl
"""

!pip install geopy

# Link https://pypi.org/project/geopy/
# Geopy https://towardsdatascience.com/geocode-with-python-161ec1e62b89

from geopy.geocoders import Nominatim

lt = "Ultadanga Road Kolkata - 04"
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode(lt)
print(location.address)
print((location.latitude, location.longitude))

import pandas as pd
cereal_df = pd.read_excel("SchoolBus_Pincode_Relation.xlsx")
cereal_df



import numpy as np

for
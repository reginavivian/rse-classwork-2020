"""A script to find the biggest earthquake in an online dataset."""

import requests
import json

# At the top of the file, import any libraries you will use.
# import ...

# If you want, you can define some functions to help organise your code.
# def helper_function(argument_1, argument_2):
#   ...

# When you run the file, it should print out the location and magnitude
# of the biggest earthquake.
# You can run the file with `python quakes.py` from this directory.
#if __name__ == "__main__":
    # ...do things here to find the results...

    # The lines below assume that the results are stored in variables
    # named max_magnitude and coords, but you can change that.
#    print(f"The maximum magnitude is {max_magnitude} "
#          f"and it occured at coordinates {coords}.")

# Get the response as shown in the exercise description
quakes = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )

# Here, I am extracting the dictionaries from a json file. 
# this would not have worked if it was not a json file
# To check if it was json, I could have said:
# with open ('quakes.json','w') as json_file 
#   json_file.write(quakes.text)

quake_data = json.loads(quakes.text)
# print(json.dumps(quake_data, indent = 4))

# Finding the biggest magnitude 
different_quake_group = quake_data['features']

all_quake_mag = []
for quake in different_quake_group:
    quake_mag = quake['properties']['mag']
    all_quake_mag.append(quake_mag)

max_mag = max(all_quake_mag)

# print(max_mag)
# print(all_quake_mag)

# Finding the index of max magnitude - fail 
all_max_mag_index = []
for i in range(len(all_quake_mag)):
    every_magnitude = all_quake_mag[i]
    if every_magnitude == max_mag: 
       max_mag_index = i
       all_max_mag_index.append(max_mag_index) 
    else:
        pass

print(all_max_mag_index)

# Finding the location of earthquake with max magnitude
all_coords = []
for i in range(len(all_max_mag_index)):
    coords = different_quake_group[i]['geometry']['coordinates']
    all_coords.append(coords)

print(all_coords)


print(f"The maximum magnitude is {max_mag} "
      f"and it occured at coordinates {all_coords}.")












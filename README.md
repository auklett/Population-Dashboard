# Population-Dashboard
Interactive World Population Dashboard made with Power BI
##
<img src="https://github.com/auklett/Population-Dashboard/blob/main/world2022.png" width=50%>

## 1. Data Collection and Cleaning
##
The data is based on the world population estimates of the United States Census Bureau <br />
https://console.cloud.google.com/marketplace/product/united-states-census-bureau/international-census-data  <br /><br />
data_prep.py (https://github.com/auklett/Population-Dashboard/blob/main/data_prep.py) was used to get the data and export them as CSV's 
##
https://github.com/auklett/Population-Dashboard/blob/main/age_group_population.csv
https://github.com/auklett/Population-Dashboard/blob/main/country_codename.csv
https://github.com/auklett/Population-Dashboard/blob/main/population_edit.csv
##
The TopoJSON from https://github.com/topojson/world-atlas?tab=readme-ov-file was also slightly edited to fit the data.
https://github.com/auklett/Population-Dashboard/blob/main/countries_edit.json

## 2. Features of the Dashboard
##
a. Year Slider (1960-2022) <br />
b. Population count and Country Selected <br />
c. Population Heatmap (Green-0, Yellow-150,000,000, Red-1,250,000,000) <br />
d. Population Pyramid (male-left, female-right) <br />
e. Most Densely Populated Countries <br />
f. Most Populated Countries <br />
g. Highest Population Growth Rate <br />
<img src="https://github.com/auklett/Population-Dashboard/blob/main/Philippines2010.png" width=50%>
<img src="https://github.com/auklett/Population-Dashboard/blob/main/World2000.png" width=50%>
<img src="https://github.com/auklett/Population-Dashboard/blob/main/China2013.png" width=50%>



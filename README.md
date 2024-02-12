# Population-Dashboard
Interactive World Population Dashboard made with Power BI
<br />
<img src="" width=50%>
<br />
1. Data Collection and Cleaning
<br />
The data is based on the world population estimates of the United States Census Bureau <br />
https://console.cloud.google.com/marketplace/product/united-states-census-bureau/international-census-data  <br /><br />
data_prep.py (https://github.com/auklett/Population-Dashboard/blob/main/data_prep.py) was used to get the data and export them as CSV's 
<br />
https://github.com/auklett/Population-Dashboard/blob/main/age_group_population.csv
https://github.com/auklett/Population-Dashboard/blob/main/country_codename.csv
https://github.com/auklett/Population-Dashboard/blob/main/population_edit.csv
<br />
The TopoJSON from https://github.com/topojson/world-atlas?tab=readme-ov-file was also slightly edited to fit the data.
https://github.com/auklett/Population-Dashboard/blob/main/countries_edit.json
<br /><br />
2. Features of the Dashboard
<br />
a. Year Slider (1960-2022)
b. Population count and Country Selected
c. Population Heatmap (Green-0, Yellow-150,000,000, Red-1,250,000,000)
d. Population Pyramid (male-left, female-right)
e. Most Densely Populated Countries
f. Most Populated Countries
g. Highest Population Growth Rate



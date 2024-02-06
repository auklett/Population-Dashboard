# %%
print(1)

# %% pip install libraries
# !pip install db-dtypes
# !pip install --upgrade google-cloud-bigquery
# !{sys.executable} -m pip install --upgrade google-cloud-bigquery

# %%
import os
import sys
import time
import json
import pandas as pd
from google.cloud import bigquery

# %%
"""
Use BigQuery API to get data
Transform data to dataframe
Perform cleaning and preparation
input: google api json credentials
output: population (raw, growth, /area) and age csv
"""

# %% Google BigQuery API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bigquery-api-token-credentials.json'
client = bigquery.Client()

#%% SQL Queries
population_sql_query = """
SELECT *
FROM bigquery-public-data.census_bureau_international.midyear_population
"""

area_sql_query = """
SELECT *
FROM bigquery-public-data.census_bureau_international.country_names_area
"""

agegroup_sql_query = """
SELECT country_code, country_name, year, starting_age, midyear_population_male, midyear_population_female
FROM `bigquery-public-data.census_bureau_international.midyear_population_5yr_age_sex`
WHERE total_flag = "A"
"""

# %% Load queries
population = client.query(population_sql_query)
while population.state != 'DONE':
    population.reload()
    time.sleep(5)

area_sql = client.query(area_sql_query)
while area_sql.state != 'DONE':
    area_sql.reload()
    time.sleep(5)

agegroup_sql = client.query(agegroup_sql_query)
while agegroup_sql.state != 'DONE':
    agegroup_sql.reload()
    time.sleep(5)

# %% Convert queries to dataframe
population_df = population.to_dataframe()
area_df = area_sql.to_dataframe()
agegroup_df = agegroup_sql.to_dataframe()

# %%
prev_popu = 1
prev_country = ''
population_df['country_area'] = 1.0
population_df['population_growth%'] = 0.0

# %% Add country area, population growth and population per area
country_area_dict = dict()
for i, row in area_df.iterrows():
    country_area_dict[row['country_name']] = row['country_area']

for i, row in population_df.iterrows():

    curr_country = row['country_name']
    curr_popu = row['midyear_population']

    population_df.at[i, 'country_area'] = country_area_dict[curr_country]
    
    if i > 0 and (prev_country == row['country_name']):
        population_df.at[i, 'population_growth%'] = 100*(curr_popu/prev_popu) - 100
    
    prev_popu = curr_popu
    prev_country = curr_country

population_df['population_per_sqkm'] = population_df['midyear_population']/population_df['country_area']

# %%
country_codename_df = area_df.drop('country_area', axis=1)

# %%
country_codename_df.to_csv('country_codename.csv')
# %%
agegroup_df.to_csv('age_group_population.csv')

# %%
population_df.to_csv('population_edit.csv')


# %%
"""
Change some country names of TopoJSON 
to match countries from the csv dataset
input: json, output: new json
"""

# %% Convert json to list
with open('countries-50m.json') as countries_file:
    countries_contents = countries_file.read()

country_dict = json.loads(countries_contents)
countries_json = country_dict['objects']['countries']['geometries']
n = len(countries_json)

country_json_list = []
for i in range(n):
    country_json_list.append(countries_json[i]['properties']['name'])

# %%
print(country_json_list)

# %% Convert csv to list
country_df = pd.read_csv('population_edit.csv')
country_csv_list = country_df['country_name'].tolist()

# %%
not_in_json = []
for c in country_csv_list:
    if c not in country_json_list:
        not_in_json.append(c)
not_in_json.sort()

# %%
not_in_csv = []
for c in country_json_list:
    if c not in country_csv_list:
        not_in_csv.append(c)
not_in_csv.sort()

# %% Countries in csv but not in json
for c in not_in_json:
    print(c)

# %% Countries in json but not in csv
for c in not_in_csv:
    print(c)

# %% Match json countries to csv countries
c_i = [1, 3, 4, 26, 7, 8, 9, 13, 10, 12, 
 11, 14, 15, 53,  16, 18, 20, 32, 5, 31,
 40, 23, 24, 25, 28, 41, 36, 43, 42, 44, 
 45, 46, 38, 35, 47, -1, 49, 6, 48, 52,
 32, 51]

json_to_csv = dict()
for i, c in enumerate(c_i):
    json_to_csv[not_in_csv[c]] = not_in_json[i]

# %% Change json dict values
for i in range(n):
    c = countries_json[i]['properties']['name']
    if c in json_to_csv.keys():
        countries_json[i]['properties']['name'] = json_to_csv[c]
        
# %% Export new countries json
with open('countries_edit.json', 'w') as cjson:
    json.dump(country_dict, cjson)



# %%
print(0)
# %%

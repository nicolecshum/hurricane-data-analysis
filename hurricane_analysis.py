# %% [markdown]
# # Hurricane Analysis

# %% [markdown]
# #### Overview

# %% [markdown]
# This project is slightly different than others you have encountered thus far. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you'll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

# %% [markdown]
# #### Project Goals

# %% [markdown]
# You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.

# %% [markdown]
# #### Prerequisites

# %% [markdown]
# In order to complete this project, you should have completed the Loops and Dictionaries sections of the [Learn Python 3 Course](https://www.codecademy.com/learn/learn-python-3). This content is also covered in the [Data Scientist Career Path](https://www.codecademy.com/learn/paths/data-science/).

# %% [markdown]
# ## Project Requirements

# %% [markdown]
# 1. Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, you want to look at data about the most powerful hurricanes that have occured. 
# 
#    Begin by looking at the `damages` list. The list contains strings representing the total cost in USD(`$`) caused by `34` category 5 hurricanes (wind speeds $\ge$ 157 mph (252 km/h)) in the Atlantic region. For some of the hurricanes, damage data was not recorded (`"Damages not recorded"`), while the rest are written in the format `"Prefix-B/M"`, where `B` stands for billions (`1000000000`) and `M` stands for millions (`1000000`).
#    
#    Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as `"Damages not recorded"`.
#    
#    Test your function with the data stored in `damages`.

# %%
# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M',
          '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M',
          '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded',
          '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B',
          '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
          '91.6B', '25.1B']

# 1
# Update Recorded Damages

def convert_dmg(damages):
    # conversion rates
    conversion = {"M": 1000000,
                  "B": 1000000000}

    # make list    
    converted_damages = list()

    # actual conversion of data
    for dmg in damages:
        if dmg == "Damages not recorded":
            converted_damages.append(dmg)
        if dmg.find("M") != -1:
            new_dmg = float(dmg[0:dmg.find('M')])*conversion["M"]
            converted_damages.append(new_dmg)
        if dmg.find("B") != -1:
            new_dmg = float(dmg[0:dmg.find('B')])*conversion["B"]
            converted_damages.append(new_dmg)
    
    #end
    return(converted_damages)


# test function by updating damages
print(convert_dmg(damages))
converted_damages = convert_dmg(damages)

# %% [markdown]
# 2. Additional data collected on the `34` strongest Atlantic hurricanes are provided in a series of lists. The data includes:
#    - `names`: names of the hurricanes
#    - `months`: months in which the hurricanes occurred
#    - `years`: years in which the hurricanes occurred
#    - `max_sustained_winds`: maximum sustained winds (miles per hour) of the hurricanes
#    - `areas_affected`: list of different areas affected by each of the hurricanes
#    - `deaths`: total number of deaths caused by each of the hurricanes
#    
#    The data is organized such that the data at each index, from `0` to `33`, corresponds to the same hurricane.
#    
#    For example, `names[0]` yields the "Cuba I" hurricane, which occurred in `months[0]` (October) `years[0]` (1924).
#    
#    Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (`Name`, `Month`, `Year`, `Max Sustained Wind`, `Areas Affected`, `Damage`, `Death`) about the hurricane.
#    
#    Thus the key `"Cuba I"` would have the value: `{'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}`.
#    
#    Test your function on the lists of data provided.

# %%
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 2
# Create a Table

def create_dict(names, months, years, winds, areas, damages, deaths):
    hurricanes_dict = {}
    for name in names:
        # get index and name of hurricane
        i = names.index(name)
        name_str = str(name)

        # get other values
        mini_dict = {}
        mini_dict["Name"] = names[i]
        mini_dict["Month"] = months[i]
        mini_dict["Year"] = years[i]
        mini_dict["Max Sustained Wind"] = winds[i]
        mini_dict["Areas Affected"] = areas[i]
        mini_dict["Damage"] = damages[i]
        mini_dict["Deaths"] = deaths[i]

        # put into main list
        hurricanes_dict[name_str] = mini_dict
    return(hurricanes_dict)

# Create and view the hurricanes dictionary
hurricanes = create_dict(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths)
print(hurricanes)

# %% [markdown]
# 3. In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.
# 
#    Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
#    
#    For example, the key `1932` would yield the value: `[{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damage not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}]`.
#    
#    Test your function on your hurricane dictionary.

# %%
# 3
# Organizing by Year
def org_by_year(dic):
    years = {}
    for hurricane in dic:
        year = dic[hurricane]["Year"] 
        info = dic[hurricane]
        if year not in years:
            years[year] = [info]
        else:
            years[year].append(info)
    return(years)

# create a new dictionary of hurricanes with year and key
org_by_year(hurricanes)

# %% [markdown]
# 4. You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.
# 
#    Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
#    
#    Test your function on your hurricane dictionary.

# %%
# 4
# Counting Damaged Areas
def count_areas(dic):
    areas_dict = {}
    for hurricane in dic:
        areas = dic[hurricane]["Areas Affected"]
        for area in areas:
            if area not in areas_dict:
                areas_dict[area] = 1
            if area in areas_dict:
                areas_dict[area] += 1
    return(areas_dict)

# create dictionary of areas to store the number of hurricanes involved in
areas_count = count_areas(hurricanes)
print(areas_count)

# %% [markdown]
# 5. Write a function that finds the area affected by the most hurricanes, and how often it was hit.
# 
#    Test your function on your affected area dictionary.

# %%
# 5
# Calculating Maximum Hurricane Count
def max_count(dic):
    max_key = max(dic, key=lambda k: dic[k])
    max_value = max(dic.values())
    print("The area most affected was", max_key, "with", max_value,"hurricanes.")
# find most frequently affected area and the number of hurricanes involved in
max_count(areas_count)

# %% [markdown]
# 6. Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
# 
#    Test your function on your hurricane dictionary.

# %%
# 6
# Calculating the Deadliest Hurricane
def deadliest_cane(hurricanes):
    all_deaths = {}
    for cane in hurricanes:
        deaths = hurricanes[cane]["Deaths"]
        all_deaths[cane] = deaths
    max_key = max(all_deaths, key=lambda k: all_deaths[k])
    max_value = max(all_deaths.values())
    print("The hurricane with the highest number of deaths was", max_key, "with", max_value, "deaths.")
        
# find highest mortality hurricane and the number of deaths
deadliest_cane(hurricanes)

# %% [markdown]
# 7. Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.
# 
#    Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.
#    
#    ```py
#    mortality_scale = {0: 0,
#    1: 100,
#    2: 500,
#    3: 1000,
#    4: 10000}
#    ```
#    
#    For example, a hurricane with a `1` mortality rating would have resulted in greater than `0` but less than or equal to `100` deaths. A hurricane with a `5` mortality would have resulted in greater than `10000` deaths.
#    
#    Store the hurricanes in a new dictionary where the keys are the mortaility ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.
#    
#    Test your function on your hurricane dictionary.

# %%
# 7
# def org_by_year(dic):
#     years = {}
#     for hurricane in dic:
#         year = dic[hurricane]["Year"] 
#         info = dic[hurricane]
#         if year not in years:
#             years[year] = [info]
#         else:
#             years[year].append(info)
#     return(years)
# Rating Hurricanes by Mortality
def org_by_rating(hurricanes):
    ratings = {}
    for cane in hurricanes:
        deaths = hurricanes[cane]["Deaths"]
        info = hurricanes[cane]
        if deaths == 0:
            rating = 0
        elif deaths <= 100:
            rating = 1
        elif deaths <= 500:
            rating = 2
        elif deaths <= 1000:
            rating = 3
        elif deaths <= 10000:
            rating = 4
        elif deaths > 10000:
            rating = 5
        if rating not in ratings:
            ratings[rating] = [info]
        else:
            ratings[rating].append(info)
    return(ratings)

# categorize hurricanes in new dictionary with mortality severity as key
canes_rated = org_by_rating(hurricanes)
print(canes_rated)

# %% [markdown]
# 8. Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
# 
#    Test your function on your hurricane dictionary.

# %%
# 8
# def deadliest_cane(hurricanes):
#     all_deaths = {}
#     for cane in hurricanes:
#         deaths = hurricanes[cane]["Deaths"]
#         all_deaths[cane] = deaths
#     max_key = max(all_deaths, key=lambda k: all_deaths[k])
#     max_value = max(all_deaths.values())
#     print("The hurricane with the highest number of deaths was", max_key, "with", max_value, "deaths.")
# Calculating Hurricane Maximum Damage
def max_damage_cane(hurricanes):
    all_damages = {}
    for cane in hurricanes:
        damage = hurricanes[cane]["Damage"]
        if damage == "Damages not recorded":
             damage = 0
        all_damages[cane] = damage
    max_key = max(all_damages, key=lambda k: all_damages[k])
    max_value = max(all_damages.values())
    print(all_damages)
    print("The hurricane with the highest damage was", max_key, "with", max_value, "dollars in damage.")
# find highest damage inducing hurricane and its total cost
max_damage_cane(hurricanes)

# %% [markdown]
# 9. Lastly, you want to rate hurricanes according to how much damage they cause.
# 
#    Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.
#    ```py
#    damage_scale = {0: 0,
#    1: 100000000,
#    2: 1000000000,
#    3: 10000000000,
#    4: 50000000000}
#    ```
#    
#    For example, a hurricane with a `1` damage rating would have resulted in damages greater than `0` USD but less than or equal to `100000000` USD. A hurricane with a `5` damage rating would have resulted in damages greater than `50000000000` USD (talk about a lot of money).
#    
#    Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
#    
#    Test your function on your hurricane dictionary.

# %%


# %%
# 9
# def org_by_rating(hurricanes):
#     ratings = {}
#     for cane in hurricanes:
#         deaths = hurricanes[cane]["Deaths"]
#         info = hurricanes[cane]
#         if deaths == 0:
#             rating = 0
#         elif deaths <= 100:
#             rating = 1
#         elif deaths <= 500:
#             rating = 2
#         elif deaths <= 1000:
#             rating = 3
#         elif deaths <= 10000:
#             rating = 4
#         elif deaths > 10000:
#             rating = 5
#         if rating not in ratings:
#             ratings[rating] = [info]
#         else:
#             ratings[rating].append(info)
#     return(ratings)
# # Rating Hurricanes by Damage
# damage_scale = {0: 0,
#                 1: 100000000,
#                 2: 1000000000,
#                 3: 10000000000,
#                 4: 50000000000}

def org_by_rating2(hurricanes):
    ratings = {}
    for cane in hurricanes:
        damage = hurricanes[cane]["Damage"]
        if damage == "Damages not recorded":
            damage = 0
        info = hurricanes[cane]
        if damage == 0:
            rating = 0
        elif damage <= 100000000:
            rating = 1
        elif damage <= 1000000000:
            rating = 2
        elif damage <= 10000000000:
            rating = 3
        elif damage <= 50000000000:
            rating = 4
        elif damage > 50000000000:
            rating = 5
        if rating not in ratings:
            ratings[rating] = [info]
        else:
            ratings[rating].append(info)
    return(ratings)

# categorize hurricanes in new dictionary with damage severity as key
cane_ratings2 = org_by_rating2(hurricanes)
print(cane_ratings2)

# %% [markdown]
# ## Solution

# %% [markdown]
# Great work! View the **Hurricane Analysis_Solution.ipynb** file or visit [our forums](https://discuss.codecademy.com/t/hurricane-analysis-challenge-project-python/462363) to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different than ours, and that's okay! There are multiple ways to solve these projects, and you'll learn more by seeing others' code.

# %%




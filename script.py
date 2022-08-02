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

# write your update damages function here:
def new_damages(damages):
    damages_new = []
    for i in damages:
        if "M" in i:
            i = float(i[:-1]) * 1000000
            damages_new.append(i)
        elif "B" in i:
            i = float(i[:-1]) * 1000000000
            damages_new.append(i)
        else:
            damages_new.append(i)

    return damages_new

damages_new = new_damages(damages)
#print(damages_new)


# write your construct hurricane dictionary function here:
def hurri_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dict_of_hurri = {}
    n = 0
    for name in names:
        dict_of_hurri[name] = {"Name" : names[n], "Month" : months[n], "Year": years[n], "Max Sustained Wind" : max_sustained_winds[n], "Area Affected" : areas_affected[n], "Damage" : damages[n], "Death" : deaths[n]}
        n += 1       

    return dict_of_hurri


hurricanes = hurri_dict(names, months, years, max_sustained_winds, areas_affected, damages_new, deaths)
#print(hurricanes)

# write your construct hurricane by year dictionary function here:
def name_to_year(h_name):
    h_year = {}
    for hdict in h_name.values():
        current_year =  hdict["Year"]
        current_cane = hdict
        if  not (current_year in h_year.keys()):
            h_year[current_year] = []
            h_year[current_year].append(current_cane)
        else:
            h_year[current_year].append(current_cane)
    return h_year
    
hurricanes_year = name_to_year(hurricanes)
#print(hurricanes_year)


# write your count affected areas function here:
def count_area(hurricanes):
    areas_countdic ={}
    for hur in hurricanes.values():
        areas = hur["Area Affected"]
        for area in areas:
            if not (area in areas_countdic.keys()):
                areas_countdic[area] = 1
            else:
                areas_countdic[area] += 1
    return areas_countdic

affected_area = count_area(hurricanes)
#print(affected_area)



# write your find most affected area function here:
def find_most(affected_area):
    max_area = ""
    max_affected = 0
    for area, times in affected_area.items():
        if times > max_affected:
            max_area = area
            max_affected = times
    return max_area, max_affected
lucky_place, lucky_time = find_most(affected_area)
#print(lucky_place)
#print(lucky_time)


# write your greatest number of deaths function here:
def most_death(hurricanes):
    death_max = 0
    hurri_max = ""
    for dict in hurricanes.values():
        hurri = dict["Name"]
        death = int(dict["Death"])
        if death > death_max:
            death_max = death
            hurri_max = hurri
    
    return hurri_max, death_max

lucky_place, lucky_times = most_death(hurricanes)
#print(lucky_place)
#print(lucky_times)
        
        
# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def hurricanes_morscale(hurricanes):
    hurricanes_ms = {}
    for value_dict in hurricanes.values():
        if value_dict["Death"] >= mortality_scale[4]:
            ms = 4
        elif value_dict["Death"] >= mortality_scale[3]:
            ms = 3
        elif value_dict["Death"] >= mortality_scale[2]:
            ms = 2
        elif value_dict["Death"] >= mortality_scale[1]:
            ms = 1
        else:
            ms = 0
        if not (ms in  hurricanes_ms.keys()):
            hurricanes_ms[ms] = []
            hurricanes_ms[ms].append(value_dict)
        else:
            hurricanes_ms[ms].append(value_dict)
    return hurricanes_ms

hurricanes_ms = hurricanes_morscale(hurricanes)
#print(hurricanes_ms)


# write your greatest damage function here:
def find_greatest_damage(hurricanes):
    name_max = ""
    damage_max = 0
    for value_dict in hurricanes.values():
        name = value_dict["Name"]
        try:
            damage = int(value_dict["Damage"])
        except:
            damage = 0
        if damage > damage_max:
            name_max = name
            damage_max = damage
    return name_max, damage_max

name_max, damage_max = find_greatest_damage(hurricanes)
#print(name_max, damage_max)


# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def hurricanes_damscale(hurricanes):
    hurricanes_ds = {}
    for value_dict in hurricanes.values():
        try:
            for i in [4,3,2,1,0]: 
                if value_dict["Damage"] >= damage_scale[i]:
                    ds = i

            if not (ds in  hurricanes_ds.keys()):
                hurricanes_ds[ds] = []
                hurricanes_ds[ds].append(value_dict)
            else:
                hurricanes_ds[ds].append(value_dict)
        except:
            continue
    return hurricanes_ds

hurricanes_ds = hurricanes_damscale(hurricanes)
print(hurricanes_ds)
        
            

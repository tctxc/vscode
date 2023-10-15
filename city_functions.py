def get_city_country(city, country, population=''):
    '''获得城市和国家的隶属关系'''
    if population:
        formatted_city_country = city + ',' + country + '-population=' + population 
    else:
        formatted_city_country = city + ',' + country
    return formatted_city_country.title()
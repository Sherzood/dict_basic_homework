def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    a=enumerate(cities)
    return dict(a)




print(cities_dict(['samarqand','buxara','toshkent','xiva','qarshi']))
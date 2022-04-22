def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    max_ege=0
    old_person=''
    for key,value in people.items():
        if value>max_ege:
            max_ege=value
            old_person=key
    return old_person        
 
    
print(oldest({"Javohir": 22, "Sharof": 35, "Tolib": 34, "Rustam": 16}))
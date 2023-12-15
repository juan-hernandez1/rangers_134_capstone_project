import requests 
# import requests_cache 
import json




# requests_cache.install_cache('image_cache', backend='sqlite')


def get_exercises(body_part, equipment=None):
    # url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/" + body_part
    url = "https://exercisedb.p.rapidapi.com/exercises/equipment/" + equipment if equipment else "https://exercisedb.p.rapidapi.com/exercises/bodyPart/" + body_part
   


    querystring = {"limit": "20"}

    headers = {
        "X-RapidAPI-Key": "a545654756msh41215968af0133ap15acf5jsneb67a6cb1e2e",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    
    return response.json()

# def get_exercises(body_part, equipment=None):
#     url = "https://exercisedb.p.rapidapi.com/exercises"

#     if body_part:
#         url += f"/bodyPart/{body_part}"

#     if equipment:
#         if body_part:  # If body_part is already included, add equipment as a query parameter
#             url += f"?equipment={equipment}"
#         else:  # If only equipment is provided, construct the URL accordingly
#             url += f"/equipment/{equipment}"

#     querystring = {"limit": "20"}

#     headers = {
#         "X-RapidAPI-Key": "a545654756msh41215968af0133ap15acf5jsneb67a6cb1e2e",
#         "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers, params=querystring)

#     return response.json()

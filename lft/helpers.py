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



# def get_exercises_by_id(exercise_id):
#     url = f"https://exercisedb.p.rapidapi.com/exercise/{exercise_id}"
#     headers = {
#         "X-RapidAPI-Key": "0dfb94aa78msheb396cbe39e2fb9p12e051jsn0e705811824d",
#         "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None



# def get_exercises_by_id(exercise_id):
#     url = "https://exercisedb.p.rapidapi.com/exercises/exercise/id/" + exercise_id
    
#     headers = {
#         "X-RapidAPI-Key": "0dfb94aa78msheb396cbe39e2fb9p12e051jsn0e705811824d",
#         "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers)
#     return response.json()

 

# def get_exercises_by_id(exercise_id):
#     url = "https://exercisedb.p.rapidapi.com/exercises/exercise/" + exercise_id

#     headers = {
#         "X-RapidAPI-Key": "0dfb94aa78msheb396cbe39e2fb9p12e051jsn0e705811824d",
#         "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         try:
#             return response.json()
#         except Exception as e:
#             print(f"Error decoding JSON: {e}")
#             return None
#     else:
#         print(f"API request failed with status code {response.status_code}")
#         return None

import requests

BASE_URL = "https://reqres.in/api/users"
HEADERS = {
   "x-api-key": "reqres-free-v1"
}

def get_users():
   response = requests.get(f"{BASE_URL}?page=2", headers=HEADERS)
   print("GET Response:", response.status_code)
   print(response.json())

def create_user():
   payload = {
       "name": "Abhijeet",
       "job": "Engineer"
   }
   response = requests.post(BASE_URL, json=payload, headers=HEADERS)
   print("POST Response:", response.status_code)
   print(response.json())

def update_user_put(user_id=2):
   payload = {
       "name": "Abhijeet",
       "job": "Senior Engineer"
   }
   response = requests.put(f"{BASE_URL}/{user_id}", json=payload, headers=HEADERS)
   print("PUT Response:", response.status_code)
   print(response.json())

def update_user_patch(user_id=2):
   payload = {
       "job": "Tech Lead"
   }
   response = requests.patch(f"{BASE_URL}/{user_id}", json=payload, headers=HEADERS)
   print("PATCH Response:", response.status_code)
   print(response.json())

def delete_user(user_id=2):
   response = requests.delete(f"{BASE_URL}/{user_id}", headers=HEADERS)
   print("DELETE Response:", response.status_code)  # Expect 204

# Run all
if __name__ == "__main__":
   print("GET Users")
   get_users()
   
   print("\nCreate User")
   create_user()
   
   print("\nUpdate User (PUT)")
   update_user_put()
   
   print("\nUpdate User (PATCH)")
   update_user_patch()
   
   print("\nDelete User")
   delete_user()

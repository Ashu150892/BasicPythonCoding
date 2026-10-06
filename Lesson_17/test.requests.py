import requests

response = requests.get("https://www.google.com")

print("Status Code:", response.status_code)
print("URL:", response.url)
print("Response Headers:", list(response.headers.items())[:5])
print("Response Text:", response.text[:5])


### GET

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print("Status Code:", response.status_code)
print("Response:", response.json())

### POST

url = "https://jsonplaceholder.typicode.com/users"

user = {
    "name": "Ashu_LPX",
    "username": "ashu",
    "email": "ashu@example.com"
}

response = requests.post(url, json=user)

print("Status Code:", response.status_code)

data = response.json()

print("Response:", data)

### PUT

url = "https://jsonplaceholder.typicode.com/users/1"

updated_user = {
    "name": "Ashutosh Madhukar",
    "username": "ashu",
    "email": "ashu@example.com"
}

response = requests.put(url, json=updated_user)

print("Status Code:", response.status_code)

data = response.json()

print("Name:", data["name"])
print("Username:", data["username"])
print("Email:", data["email"])


### Delete

import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.delete(url)

print("Status Code:", response.status_code)
print("Response:", response.text)



### Raise the status:


url = "https://jsonplaceholder.typicode.com/users/99999"

try:
    response = requests.get(url)

    print("Status Code:", response.status_code)

    response.raise_for_status()

    data = response.json()
    print(data)

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)
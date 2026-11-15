import requests

# Send GET request
r = requests.get("http://127.0.0.1:8000")

# Print GET response
print("GET Status Code:", r.status_code)
print("Welcome Message:", r.json())


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send POST request
r = requests.post("http://127.0.0.1:8000/data/", json=data)

# Print POST response
print("POST Status Code:", r.status_code)
print("Prediction Result:", r.json())

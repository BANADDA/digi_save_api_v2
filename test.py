import requests

# URL of the endpoint
url = 'http://127.0.0.1:8000/login-with-phone-code/'

# Sample payload data to be sent in the POST request
payload = {
    'phone': +256704959275,
    'unique_code': admin123,
    # Add other required fields in the payload as needed
}

# Making a POST request
response = requests.post(url, data=payload)

# Checking the response
if response.status_code == 200:
    # Successful response
    print("Login successful!")
    print("Response data:")
    print(response.json())  # Prints the JSON response data
else:
    # Unsuccessful response
    print("Login failed!")
    print("Status code:", response.status_code)
    print("Error message:")
    print(response.json())  # Prints the JSON error message

import requests

url = 'http://127.0.0.1:7000/user-login/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'rftghyujikio',
}

# Make the request with the headers
response = requests.post(url, data={'phone': '+256704959275', 'pincode': 'JVU8Q8'})

# Handle the response
print(response.status_code)
print(response.text)

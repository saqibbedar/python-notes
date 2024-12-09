import requests

# Ollama Endpoint API
url = "http://localhost:11434/api/generate" 

query = input("Enter query: ")

# JSON data to send in the request
data = {
    "model": "tinyllama",
    "prompt": f"{query}",
    "stream": False
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# Send POST request to API
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("Response from Ollama: \n")
    value = response.json()
    print("The value type of response: ", type(value))
    print(value["response"])
else:
    print(f"Error: {response.status_code} - {response.text}")
import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/6f5d3bc0-1734-4318-b1f6-60148d289bbf"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])
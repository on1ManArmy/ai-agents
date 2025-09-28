import httpx

client = httpx.Client(verify=False)
response = client.get("https://api.openai.com/v1/models")
print(response.status_code)
print(response.text)

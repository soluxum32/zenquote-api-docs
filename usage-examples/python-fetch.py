import requests

url = "https://api.zenquote.io/v1/koan"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Zen Koan: {data['koan']}")
    print(f"Master: {data['master']}")
    print(f"Theme: {data['theme']}")
else:
    print("Failed to fetch koan.")

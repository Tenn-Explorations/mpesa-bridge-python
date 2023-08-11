from mpesa_bridge.client import Client

BASE_URL = "https://sandbox.safaricom.co.ke"
API_KEY = "YOUR_API_KEY"

client = Client(api_key=API_KEY, base_url=BASE_URL)

response = client.request_payment(2000, "2547XXXXXXXX")

print(response)

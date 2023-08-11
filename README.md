# mpesa-bridge-python
A python client library for mpesa_bridge

## How it works
We have abstracted all the integrations stuff and all that is left for you to do is a one line call

```python
response = client.request_payment(1000, "2547xxxxxxxx")
```
Well, there is small configuration before then. Let us take you through:

## usage
To use mpes_bridge python library, you can install it via pip (recommended).
```bash
pip install git+https://github.com/Tenn-Explorations/mpesa-bridge-python
```

After cloning, import it into your project and initialize the client:
```python
from mpesa_bridge.client import Client

# it is recommended that you load these to variables from .env
BASE_URL = "https://weprocesspayments.ink"
API_KEY = "YOUR_API_KEY"

client = Client(api_key=API_KEY, base_url=BASE_URL)
```

Now you are ready to perform transactions.
```python
response = client.request_payment(2000, "2547XXXXXXXX")

print(response)
```

A full example is available on the `examples/` folder.

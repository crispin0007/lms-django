import requests
import json

url = "https://a.khalti.com/api/v2/epayment/initiate/"

payload = json.dumps({
    "return_url": "http://127.0.0.1:8000",
    "website_url": "http://127.0.0.1:8000",
    "amount": "1000",
    "purchase_order_id": "b526e882-2794-4ee2-8962-f1598f9111c7",
    "purchase_order_name": "test",
    "customer_info": {
    "name": "Ram Bahadur",
    "email": "test@khalti.com",
    "phone": "9800000001"
    }
})
headers = {
    'Authorization': 'test_public_key_212a87eb55d547db9d6a839a4544c510',
    'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
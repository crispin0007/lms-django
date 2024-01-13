from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@login_required
@csrf_exempt  # Use this decorator if you want to disable CSRF protection for this view, adjust as needed
def initiate_payment(request):
    if request.method == 'POST':
        # Retrieve data from the request or use your own logic to get the required information
        return_url = "http://127.0.0.1/"
        website_url = "http://127.0.0.1/"
        amount = "1000"
        purchase_order_id = "Order01"
        purchase_order_name = "test"
        customer_info = {
            "name": "Ram Bahadur",
            "email": "test@khalti.com",
            "phone": "9800000001"
        }

        # Create payload
        payload = {
            "return_url": return_url,
            "website_url": website_url,
            "amount": amount,
            "purchase_order_id": purchase_order_id,
            "purchase_order_name": purchase_order_name,
            "customer_info": customer_info
        }

        # Convert payload to JSON
        payload_json = json.dumps(payload)

        # Add your Khalti secret key
        khalti_secret_key = 'test_secret_key_1d286d30433b43348b4ad1b4c8e34fd1'
        headers = {
            'Authorization': f'key {khalti_secret_key}',
            'Content-Type': 'application/json',
        }

        # Make a POST request to Khalti API
        url = "https://a.khalti.com/api/v2/epayment/initiate/"
        response = requests.post(url, headers=headers, data=payload_json)

        # Handle the response as needed
        return HttpResponse(response.text, content_type='application/json')

    else:
        # Handle other HTTP methods as needed
        return HttpResponse("Method not allowed", status=405)

import requests

baseurl = "http://localhost:5000/v1/api" 
request_url = f"{baseurl}/iserver/marketdata/snapshot?conids=265598,8314&fields=31,84,86"

try:
    response = requests.get(url=request_url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    # Process the response here
    print(response.json())

except requests.exceptions.SSLError as ssl_err:
    print("SSL Error:", ssl_err)
except requests.exceptions.ConnectionError as conn_err:
    print("Error Connecting:", conn_err)
except requests.exceptions.Timeout as timeout_err: 
    print("Timeout Error:", timeout_err)
except requests.exceptions.RequestException as req_err:
    print("An Error Occurred:", req_err)


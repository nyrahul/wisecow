import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The application at {url} is UP.")
        else:
            print(f"The application at {url} is DOWN. Status Code: {response.status_code}")
    except requests.ConnectionError:
        print(f"The application at {url} is DOWN. Failed to establish a connection.")
    except requests.Timeout:
        print(f"The application at {url} is DOWN. The request timed out.")
    except requests.RequestException as e:
        print(f"The application at {url} is DOWN. An error occurred: {e}")

url_to_check = "http://127.0.0.1:5000"
check_application_health(url_to_check)

import requests

url = input("Enter any URL") #for example "https://www.geeksforgeeks.org"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        # Process the HTML content as needed
        print(html_content)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)

#chat api
import requests
from time import time as t

URL = "https://move.pythonanywhere.com"

# Get the link
def get_link():
    url = f'{URL}/get_link'  # Replace with your server address
    response = requests.get(url)
    if response.status_code == 200:
        link = response.json().get('link')
        if link is not None:
            return link
        else:
            print("Link not found in the response")
    else:
        print("Failed to retrieve the link")


def ChatGpt(prompt, link):
    url = f'{link}/Gpt_Get_Data'  # Change the URL if the server is running on a different host

    # Define the JSON payload to send to the server
    json_payload = {
        "prompt": f"{prompt}",
        "model": "gpt-4-32k-0613"
    }

    try:
        with requests.post(url, json=json_payload, stream=True) as response:
            if response.status_code == 200:
                for chunk in response.iter_content(chunk_size=128, decode_unicode=True):
                    if chunk:
                        print(chunk)  # Print the response from the server
            else:
                print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed with an exception: {e}")


if __name__ == '__main__':
    link = get_link()
    if link is not None:
        while True:
            user_input = input(">>> ")
            start_time = t()
            ChatGpt(user_input, link)
            end_time = t()
            print(end_time - start_time)
            
#use_gpt("what is your name", "https://bbe8-35-240-224-111.ngrok-free.app/")

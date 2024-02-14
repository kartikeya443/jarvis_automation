import requests
from PIL import ImageGrab
import io
from pyautogui import click,sleep


def Ocr(st:str,url:str,double_click:bool=False):
    #to take screen shot
    screenshot = ImageGrab.grab()

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    screenshot.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # Create a dictionary with the form data
    if double_click:
        payload = {
            "search_string": st,
            "double_click": "on"
        }
        files = {'image': image_bytes}
    else:
        payload = {
            "search_string": st,
            "double_click": "off"
        }
        files = {'image': image_bytes}

    # Send a POST request to the Flask application
    response = requests.post(f"{url}/imgs", files=files, data=payload)
    screenshot.close()
    response=response.json()
    if "error" in response:
        return f"no button found name {st}"
    else:
        # Print the response
        print(response["time"])
        point=response["point"]
        if double_click:
            click(point)
            sleep(0.30)
            click(point)
            return f"button found name {st} clicking on it"
        else:
            click(point)
            return f"button found name {st} clicking on it"
        

#print(Ocr("main.py", "https://bbe8-35-240-224-111.ngrok-free.app/", False))
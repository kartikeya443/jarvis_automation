#pip install -U g4f (this is a prebuild gpt api freely available)

import g4f

'''print([
    provider.__name__
    for provider in g4f.Provider.__providers__
    if provider.working
])'''

messages=[{"role": "system", "content": "You are the AI JARVIS virtual assistant." + "You're the latest version of J.A.R.V.I.S. AI, designed by Kartikeya Acharya with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
          {"role": "system", "content": "You're coded by Kartikeya Acharya and not by OpenAI."},
          {"role": "system", "content": "use modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},       
          {"role": "user", "content": "Open Google Chrome."},
          {"role": "assistant", "content": "'''python\nimport webbrowser\nwebbrowser.open('https://www.google.com')'''"}]

def ChatGpt(*args,**kwargs):
    global messages
    assert args!=()
    #MsgDelAuto()
    message=""
    for i in args:
        message+=i


    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.Koala,
        messages=messages,
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})
    return ms

if __name__=="__main__":
    ChatGpt(input(">>> "))
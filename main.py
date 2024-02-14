# import sys
# # Set the encoding for stdout to UTF-8
# sys.stdout.reconfigure(encoding='utf-8')

from func.Chat import Chat
from func.speak_offline import Speak
from func.listenJs import Listen
from func.data_online import online_data_scraper
#from func.speak_online import Speak
from llm.gpt_server import ChatGpt
from func.ocr_online import Ocr
from llm.filter import filter
from buildin import chrome_code
from buildin import knowApps
import pygetwindow as gw
import keyboard

link = input("Enter passcode -> ")
if link=="69":
    from llm.gpt import ChatGpt
    from func.ocr_online import Ocr



if __name__ == "__main__":
    
    while 1:
        Q = Listen()
        QL = Q.lower()        
        LQ = len(Q.split(" "))
        SQ = Q.split(" ")[0]
        EQ = Q.split(" ")[-1]
        CURRENT_APP=""
        try:
            CURRENT_APP = gw.getActiveWindowTitle()
        except gw.PyGetWindowException:
            CURRENT_APP = ""
        #CURRENT_APP NAME
        CURRENT_APP_NAME=CURRENT_APP.split(" - ")[-1]
        
        
        if (SQ == "click" or (SQ == "double" and "click" in Q)) and LQ<7:
            QL.replace("click","").replace("on","").replace("JARVIS","").replace("double","")
            A = Ocr(QL.strip(),url=link)
            Speak(A)
            
        elif "jarvis" == SQ.lower():
            code = ChatGpt(f"{Q} ***use python programming language. just write complete code nothing else***", link = link)
            code = filter(code)
            exec(code)
        
        if CURRENT_APP_NAME in knowApps:
            
            Func_=knowApps[CURRENT_APP_NAME]
            Output = Func_(QL)
            if Output != False:
                keyboard.press_and_release(Output)
            
            else:
                web = online_data_scraper(Q)
                if web is not None:
                    Speak(web)
                elif Chat(QL)[1]>0.99:
                    Speak(Chat(QL)[0])
                else:
                    #for llm fxn
                    reply = ChatGpt(f"{Q} ***reply like tony stark jarvis in less words***", link = link)
                    Speak(reply)
        
        else:
            web = online_data_scraper(Q)
            if web is not None:
                Speak(web)
            elif Chat(QL)[1]>0.99:
                Speak(Chat(QL)[0])
            else:
                #for llm fxn
                reply = ChatGpt(f"{Q} ***reply like tony stark jarvis in less words***", link = link)
                Speak(reply)


from func.Chat import Chat
from func.data_online import online_data_scraper

from func.speak_online import Speak
from func.listenJs import Listen
from llm.gpt import ChatGpt

from func.ocr import ocr_v1_cl


if __name__ == "__main__":
    
    while 1:
        Q = Listen()
        QL = Q.lower()        
        LQ = len(Q.split(" "))
        SQ = Q.split(" ")[0]
        EQ = Q.split(" ")[-1]
        
        if (SQ == "click" or (SQ == "double" and "click" in Q)) and LQ<7:
            QL.replace("click","").replace("on","").replace("JARVIS","").replace("double","")
            A = ocr_v1_cl(QL.strip())
            Speak(A)
        else:
            web = online_data_scraper(Q)
            if web is not None:
                Speak(web)
            elif Chat(QL)[1]>0.98:
                Speak(Chat(QL)[0])
            else:
                #for llm fxn
                reply=ChatGpt(Q, " ***reply like tony stark jarvis in less words***")
                Speak(reply.encode('utf-8', errors='ignore').decode('utf-8'))


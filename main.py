from func.Chat import Chat
from func.speak_online import Speak
from func.listenJs import Listen
from func.data_online import Online_Scraper

if __name__ == "__main__":
    while 1:
        Q = Listen()
        qL = Q.lower()
        getChat = Chat(qL)
        getData = Online_Scraper(Q)
        
        if getData != None:
            Speak(getData)
        else:
            Speak(getChat[0])
        
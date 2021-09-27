from api import server
import backend.main as bm


if __name__=="__main__":
    server.start(bm.recogniseEmotion,2)
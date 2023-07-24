# TenorGifs | TenorGifs






#Imports
from random import randint

from urllib.request import urlopen
from urllib.request import Request






#Classes
class GifSearch:
    def __init__(self):
        self.Gifs = []
    

    @property
    def gifCount(self) -> int:
        return len(self.Gifs)
        

    @property
    def firstGif(self) -> str:
        if self.gifCount == 0: return None
        return self.Gifs[0]
    

    @property
    def lastGif(self) -> str:
        if self.gifCount == 0: return None
        return self.Gifs[-1]

    

    def getRandomGif(self) -> str:
        if self.gifCount == 0: return None
        return self.Gifs[randint(0, len(self.Gifs) - 1)]
    


    def search(self, query: str):
        try:
            url = 'https://tenor.com/search/' + query.replace(' ', '-') + '-gifs'
            information = urlopen(Request(url)).read().decode('utf8')

            Gifs = information.split('src="')
            Gifs = [i.split('"')[0] for i in Gifs[54:]]
            self.Gifs = [i for i in Gifs if i.startswith('https://')]
        except: pass

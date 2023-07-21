# TenorGifs
Simple [**python**](https://www.python.org/) class to handle requesting for gifs from [**Tenor**](https://www.tenor.com).
<br />
<br />
<br />
<br />
<br />
## Usage
To import the **module**, simply put:
```py
from TenorGifs.TenorGifs import GifSearch
```
​
<br />
Then, later on you may utilize:
```py
Gifs = GifSearch()

Gifs.search('hello')
#Searches for a gif and stores the resuls to be retrieved.
```
```py
Gifs.Gifs
#Stored gifs.
```
```py
Gifs.gifCount
#Returns the amount of gifs currently stored.

Gifs.firstGif
#Returns the first gif in the list of stored gifs.

Gifs.lastGif
#Returns the last gif in the list of stored gifs.

Gifs.getRandomGif()
#Returns a random gif from the list of stored gifs.
```
​
<br />
<br />
### Code Examples
```py
from TenorGifs.TenorGifs import GifSearch

Gifs = GifSearch()
Gifs.search('hello')

print(Gifs.firstGif)
```

```py
from TenorGifs.TenorGifs import GifSearch

Gifs = GifSearch()
Gifs.search('hello')

print('Successfully found ' + str(Gifs.gifCount) + ' gifs.')
print(Gifs.getRandomGif())
```
```py
from TenorGifs.TenorGifs import GifSearch

Gifs = GifSearch()

Gifs.search('1')
numberOne = Gifs.firstGif

Gifs.search('2')
numberTwo = Gifs.firstGif

Gifs.search('3')
numberThree = Gifs.firstGif


print(numberOne)
print(numberTwo)
print(numberThree)
```
​
<br />
<br />
​<br />
<br />
<br />
## Installation
```sh
git clone https://github.com/IrtsaDevelopment/TenorGifs.git
```

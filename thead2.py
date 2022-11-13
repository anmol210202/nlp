import threading
from queue import Queue
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup


queue = Queue()
def get_links(url):
    links = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

links = []
valid_links = []
arr = []
 
for link in get_links('https://imsdb.com/all-scripts.html'):
    if 'Movie Scripts' in link:
        links.append('https://imsdb.com'+link.replace('Movie Scripts', 'scripts').replace(' ', '-').replace('-Script', ''))

def get_movie_name(link):
    return link.split('/')[-1].replace('-', ' ').replace('script', '').title().replace('.Html', '')

def get_text(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.find('pre').text
    return text


def get_genre(url):
    result = requests.get(url)
    genres =['action','adventure','animation','comedy','crime','drama','family','fantasy','film-noir','horror','musical','mystery','romance','sci-fi','short','thriller','war','western']
    doc =  BeautifulSoup(result.content, "html.parser")
    script = ''.join(doc.text)
    script = re.sub(r'\s+', ' ', script)
    array = script.split(' ')
    movieGenres = ''
    for i in range(array.index('Genres')+1,array.index(array[-2])):
        if array[i].lower() in genres:
            movieGenres = movieGenres + (array[i].lower()) + ','
    movieGenres = movieGenres[0:len(movieGenres)-1]
    return movieGenres

# https://imsdb.com/Movie Scripts/A Prayer Before Dawn Script.html
# https://imsdb.com/scripts/A-Prayer-Before-Dawn.html

# def make_csv_pd(link,arr):
#     # df = pd.DataFrame(columns=['link', 'text'])
#     # for link in links:
#         # df = df.append({'link': link, 'text': get_text(link)}, ignore_index=True)
#     # for i in range(0, 10):
#     arr = arr.append({'link': get_movie_name(link), 'text': get_text(link)}, ignore_index=True)
#     # df.to_csv('movie_scripts.csv', index=False)
                                                           # original 
def fill_queue(links):
    for link in links:
        queue.put(link)
                                                            # new


def fill_queue(links):
    for i in range(200, 500):
        queue.put(links[i])

def check_link(link):
    response = requests.get(link)
    if response.status_code == 200:
        # print(link)
        return True
    else:   
        return False

def worker(arr):
    while not queue.empty():
        link = queue.get()
        if check_link(link):
            print('Link {} is valid'.format(link))
            valid_links.append(link)
            arr.append({'name': get_movie_name(link), 'script': get_text(link), 'genre': get_genre(link)})
            # df = df.append({'link': get_movie_name(link), 'text': get_text(link)}, ignore_index=True)

fill_queue(links)

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker , args=(arr,))
    thread_list.append(thread)
    
for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()

pd.DataFrame(arr).to_csv('movie_scripts_new.csv', mode='a'  ,index=False)
# print('Valid links: {}'.format(len(valid_links)))
# print('Total links: {}'.format(len(links)))

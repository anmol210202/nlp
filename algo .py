import requests
from bs4 import BeautifulSoup
import threading
from concurrent.futures import ThreadPoolExecutor
import sys
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from nrclex import NRCLex

# find number of rows and columns in csv
def find_csv_size():
    df = pd.read_csv('movie_scripts.csv')
    print(df.shape)

# print rows in csv
def print_csv():
    df = pd.read_csv('movie_scripts.csv')
    print(df)

# print_csv()
# find_csv_size()



# def get_links(url):
#     links = []
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     for link in soup.find_all('a'):
#         links.append(link.get('href'))
#     return links

# links = []
 
# for link in get_links('https://imsdb.com/all-scripts.html'):
#     if 'Movie Scripts' in link:
#         links.append('https://imsdb.com'+link.replace('Movie Scripts', 'scripts').replace(' ', '-').replace('-Script', ''))

# soup link from link and get text save to csv file as a row
def get_text(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.find('pre').text
    return text
# make a csv file with the text from the links and the link
# def make_csv(links):
#     with open('movie_scripts.csv', 'w') as f:
#         for link in links:
#             f.write('{},{}\n'.format(link, get_text(link)))


# make a csv using pandas and save link and text as a row

# movie name from link
def get_movie_name(link):
    return link.split('/')[-1].replace('-', ' ').replace('script', '').title()

def make_csv_pd(links,df):
    # for link in links:
        # df = df.append({'link': link, 'text': get_text(link)}, ignore_index=True)
    # for i in range(0, 10):
    df.append({'link': links, 'text': get_text(links)})
    # return pd.DataFrame(df)
    # df.to_csv('movie_scripts.csv', mode='a'  ,index=False)
    

arr = []

# for i in range(0, 10):
    # make_csv_pd(links[i],arr)

# pd.DataFrame(arr).to_csv('movie_scripts.csv', mode='a'  ,index=False)
# print(len(arr))

# df.to_csv('movie_scripts.csv', mode='a'  ,index=False)

find_csv_size()
print_csv()



# url = 'https://imsdb.com/scripts/Chinatown.html'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# text = soup.find('pre').text
# df = pd.DataFrame({'text': [text]})
# df.to_csv('scripts.csv', mode='a', header=False, index=False)
# print(*links, sep='\n')

# check if the link is valid

# valid_links = []

# def check_link(link):
#     response = requests.get(link)
#     if response.status_code == 200:
#         print(link)
#         valid_links.append(link)




# def some_action(links):
#     for link in links:
#         check_link(link)

# # use threading to speed up the process
# def main():
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         executor.map(some_action, links)
        
# main()
        
# use threading to check all links in parallel and save valid links in a list
# def check_links(links):
#     threads = []
#     for link in links:
#         thread = threading.Thread(target=check_link, args=(link,))
#         thread.start()
#         threads.append(thread)
#     for thread in threads:
#         thread.join()

# check_links(links)

# for link in links:
#     valid_links = []
#     check_link(link)

# vaild =[]
# for link in links:
#     if check_link(link):
#         print(link)
#         vaild.append(link)

# print(len(vaild) - len(links))



                                                                               #siddharth

# df2 = pd.read_csv('scripts.csv')

# # number of rows in the dataframe
# def get_num_rows(df):
#     return len(df.index)

# # print(get_num_rows(df2))
# #how to check if the word is in all caps
# def is_all_caps(word):
#     return word.isupper()
# #how to get the number of columns in the dataframe
# def get_num_columns(df):
#     return len(df.columns)

# arr = []
# oldword = ''


# for line in df2[1:2]:
#     for word in line.split():
        
#             # displaying the words           
#         if(is_all_caps(word) and len(word) > 1):
#             arr.append(oldword)
#             oldword = ''
#         else:
#             oldword =oldword+ ' '+ word
# newarr = []
# for i in arr:
#     if i!='':
#         newarr.append(i)
        
# compoundScores = []
# obj  = SentimentIntensityAnalyzer()
# for line in newarr:
#     sentiment  = obj.polarity_scores(line)
#     # print(sentiment['compound'])
#     compoundScores.append(sentiment['compound'])

# #plot a graph of the compound scores
# def plot_graph(compoundScores):
#     plt.plot(compoundScores)
#     plt.show()

# # plot_graph(compoundScores)

# for i in range(len(newarr)):
 
#     # Create object
#     emotion = NRCLex(newarr[i])
 
#     # Classify emotion
#     print('\n\n', newarr[i], ': ', emotion.top_emotions)

# # make csv file with all the scripts
# # def make_csv(links):
# #     for link in links:
# #         response = requests.get(link)
# #         soup = BeautifulSoup(response.text, 'html.parser')
# #         text = soup.find('pre').text
# #         df = pd.DataFrame({'text': [text]})
# #         df.to_csv('scripts.csv', mode='a', header=False, index=False)

# # print(df['text'].apply(count_lines)/20)
# # print(type(text))
# # f = open('Chinatown.txt', 'w',encoding="utf-8")
# # f.writelines(text.text)
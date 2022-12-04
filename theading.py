# import pandas as pd

# def find_csv_size():
#     df = pd.read_csv('movie_scripts_new.csv')
#     print(df)

# find_csv_size()

# https://imsdb.com/Movie Scripts/12 Script.html
# https://imsdb.com/Movie Scripts/12.html
# https://imsdb.com/Movie Scripts/12.html


import numpy as np

#2d array with random numbers between 0 and 10 with 5 rows and 10 columns

# array with numbers between -1 and 1

def trunc(arr, decimals=0):
    multiplier = 10 ** decimals
    return np.trunc(arr * multiplier) / multiplier

def random_array():
    # return np.random.randint(-1,1, (100,5))
    return trunc(np.random.normal(0, 1, (1000,40)), 2)

M = random_array()
print(M)
N = trunc(np.random.normal(0, 1, (40)), 2)

print(N)

# take n and find most similar row in array
def find_similar_row(array, n):
    # find the difference between n and each row in array
    # find the sum of the difference
    # find the row with the lowest sum of difference
    # return the row
    # return array[np.argmin(np.sum(np.abs(array - n), axis=1))]
    return M[np.argmax(np.dot(N, M.T)/(np.linalg.norm(M)*np.linalg.norm(N)))]

# print(find_similar_row(array, n))
print(find_similar_row(M,N))
    
# get div with class from beautiful soup
def get_div_class(soup, class_name):
    return soup.find('div', class_=class_name)
# get text from div with class
def get_text_from_div_class(soup, class_name):
    return get_div_class(soup, class_name).text 
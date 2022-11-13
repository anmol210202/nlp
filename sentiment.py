# read txt file and string
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
#nltk.download('omw-1.4')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from nrclex import NRCLex
# from gensim.models import Word2Vec
import re
with open('output.txt', 'r') as f:
    text = f.read()
    string = str(text)


# when find a word put rest of string in a list
def find_word(string, word,arr):
    index = string.find
    return index


def arr_scence(string ):
    arr = [string.start() for string in re.finditer('INT.', string)]
    arr = arr + [string.start() for string in re.finditer('EXT.', string)]
    arr.sort()
    scene = []
    for i in range(0,len(arr)):
        if i == 0:
            scene.append(string[0:arr[i]])
        else:
            scene.append(string[arr[i-1]:arr[i]])
    return scene
    

# print(len(arr_scence(string)))

token_arr = []

for scene in arr_scence(string):
    text = re.sub(r'\[[0-9]*\]', ' ', scene)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = re.sub(r'\d', ' ', text)
    text = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', text)
    text = re.sub('\W+',' ', text )
    text = word_tokenize(text)
    scene = []
    for word in text:
        if word not in stopwords.words('english'):
            scene.append(word)
            
    token_arr.append(scene)
    # model = Word2Vec([text], min_count=1)
    # words = model.wv.vocab
    # print(text)
    # sentences = nltk.sent_tokenize(text)
    # sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    # for i in range(len(sentences)):
    #     sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]


def lemmatize_words(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    return lemmatized_words
token_arr2 = []
for token in token_arr:
    token_arr2.append(lemmatize_words(token))
    
token_arr = token_arr2

#stemming without using nltk
def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = []
    for word in words:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words
token_arr2 = []
for token in token_arr:
    token = stem_words(token)
    token_arr2.append(token)
token_arr = token_arr2

token_dictionary = {}
i=1
for token in token_arr:
    for word in token:
        if word not in token_dictionary:
            token_dictionary[word] = i
            i+=1
    # print(token)
    # print(len(token))
    # print('
print(token_dictionary)
sequences = []
for token in token_arr:
    sequences.append([token_dictionary[word] for word in token])
    
print(sequences)

#padding of sequences
def pad_sequences(sequences):
    max_length = max([len(seq) for seq in sequences])
    padded_sequences = []
    for seq in sequences:
        while len(seq) < max_length:
            seq.append(0)
        padded_sequences.append(seq)
    return padded_sequences
padded = pad_sequences(sequences)
for seq in sequences:
    print(len(seq))
    


for token in token_arr:
    joined = ' '.join(token)
    token_arr[token_arr.index(token)] = joined








compoundScores = []
obj  = SentimentIntensityAnalyzer()
for line in token_arr:
    sentiment  = obj.polarity_scores(line)
    # print(sentiment['compound'])
    compoundScores.append(sentiment['compound'])

def plot_graph(compoundScores):
    plt.plot(compoundScores)
    plt.show()

plot_graph(compoundScores)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[43]:


#create a template for the lyrics dictionary and lyrics name list
song_template = {
     'Colorado' : ['Rockies','a','happy','brilliant'],
     'Boston'   : ['Red Sox','love','hate','design'],
     'Minnesota': ['Twins','fashion'],
     'Milwaukee': ['Brewers','pattern','bowl','baby'],
     'Seattle'  : ['Mariners','swim','vegetables','fresh','cry']
 }
song_list=['Colorado','Boston','Minnesota','Milwaukee','Seattle']


# In[10]:


#define a function to save a list of positive and negative word
def get_pos_neg_words():
    def get_words(url):
        import requests
        words = requests.get(url).content.decode('latin-1')
        word_list = words.split('\n')
        index = 0
        while index < len(word_list):
            word = word_list[index]
            if ';' in word or not word:
                word_list.pop(index)
            else:
                index+=1
        return word_list

    p_url = 'http://ptrckprry.com/course/ssd/data/positive-words.txt'
    n_url = 'http://ptrckprry.com/course/ssd/data/negative-words.txt'
    positive_words = get_words(p_url)
    negative_words = get_words(n_url)
    return positive_words,negative_words


# In[41]:


#define a function to return a list of the percentage of positive word and negative word for each song
def sentiment(song_lyrics, name_list, debug=False):
    positive_words,negative_words = get_pos_neg_words()
    results = list()
    for song in name_list:
        lyrics = song_lyrics[song]
        cpos = cneg = 0
        for word in lyrics:
            if word in positive_words:
                if debug:
                    print("Positive",word)
                cpos+=1
            if word in negative_words:
                if debug:
                    print("Negative",word)
                cneg+=1
        results.append((song,cpos/len(lyrics),cneg/len(lyrics)))
    return results


# In[59]:


#separate the result into two list with sorted rank
def result_rank(song_lyrics, name_list):
    result = sentiment(song_lyrics, name_list)
    result_rank_p={song[0]:song[1] for song in result}
    result_rank_n={song[0]:song[2] for song in result}
    import operator
    sorted_rank_p = sorted(result_rank_p.items(), key=operator.itemgetter(1), reverse=True)
    sorted_rank_n = sorted(result_rank_n.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_rank_p, sorted_rank_n


# In[60]:


result_rank(song_template, song_list)


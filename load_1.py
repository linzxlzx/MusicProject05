#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:42:39 2019

@author: zixuan_leah
"""
import zipfile
import nltk
#nltk.download('wordnet')
from nltk.stem.snowball import SnowballStemmer
#from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
     

#def get_songnames(zipname):
#    
#    return song_names


def read_lyrics(zipname: zip):  # return the songname and lyric words as a dic
    lyrics_zip = zipfile.ZipFile(zipname)  # read songnames from the zipfile
    song_names = lyrics_zip.namelist()

    song_lyrics = {}
    for song in song_names:
        lyric_context = lyrics_zip.open(song, mode='r')

        text = ''
        for sentence in lyric_context.readlines():  # split into sentences
#            text += sentence.rstrip("\n")            
            sentence = sentence.decode()
            text += sentence.strip("\r\n")+" "

        words = text.split(" ")  # split into words
        for letters_in in range(len(words)):  # take off chars "...", ","...
            word_adj = ''.join([char for char in words[letters_in]
                                if (char.isalpha()
                                    or char == "'"  # "they're" as one word
                                    or char == "*")])
            stemmer = SnowballStemmer("english")  # get stems of the words
            words[letters_in] = stemmer.stem(word_adj)

        song_lyrics[song] = words  # put songname and lyrics in dic

    return song_lyrics


def detect_lang(songwords: list):  # func used to detct whether is english song
    index = 0
    count = 1
    stop = 10  # we take the first 10 words to detct whether it is english
    eng_words = 0
    if len(songwords) < stop:
        stop = len(songwords)
    while count < stop:
        if songwords[index].isalpha():
            if wordnet.synsets(songwords[index].isalpha()):
                eng_words += 1
            count += 1
        index += 1
# we set the criteria: English song has 70% of first 10 words as English
    if eng_words / stop >= 0.7:
        return True



lyrics_dic = read_lyrics("Lyrics.zip")
a=detect_lang(lyrics_dic["232~Jacqueline-Taïeb~7-Heures-du-Matin.txt"])
print(s)










stemmer = SnowballStemmer("english")
print(stemmer2.stem("seeing*****"))
#wordnet_lemmatizer = WordNetLemmatizer()
#w=wordnet_lemmatizer.lemmatize("seeing", pos="v")
#print(w)

if wordnet.synsets("got"):
         #Do something
    print("yes")
else:
    print("no")
          #Do some otherthing

#print(song_names)


#f=zip.open('my_txt_file.txt')
#contents=f.read()
#f.close()
#
#import zipfile
#
#zf = zipfile.ZipFile('example.zip', 'r')
#print zf.namelist()
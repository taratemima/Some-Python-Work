from __future__ import division
import nltk, pprint, re
import os.path
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.corpus import words as wordlist

def extractingFromFolders():
    folder2 = os.path.expanduser('~\\My Documents\\Tara\\Ongoing\\CharacterCorpus\\Reference')
    fileresult = os.path.expanduser('~\\My Documents\\Tara\\Ongoing\\CharacterCorpus\\results.txt')
    refer = PlaintextCorpusReader(folder2, 'harrygrepster.txt')
    grepster = refer.words()
    results = open(fileresult, 'a')
    completeWords = wordlist.words()
    stoppers = stopwords.words()
    return grepster, results, completeWords, stoppers

#I will need to revise findNonStopwords and findUnusual, since even
#when I have them as a sorted set, they are listed as lists


def findUnusual(completeWords,stoppers,wordlist):
    #complete = sorted(set(completeWords))
    #stops = sorted(set(stoppers))
    wlist = sorted(set(wordlist))
    correct = []
    unusual = []

    for w in wordlist:
        if w not in stoppers:
            if w in completeWords:
                correct.append(w)
            else:
                unusual.append(w)
    return correct, unusual

def RefineLists():
    grepster, results, complete, stoppers = extractingFromFolders()
    grepsterRefined = sorted(set(grepster))
    grepsterSpelled, grepsterUnusual = findUnusual(complete, stoppers, grepsterRefined)
    return grepsterSpelled, grepsterUnusual, results

def PrintLists(title, wordlists, results):
    results.write(title+'\r\n')
    if wordlists != False:
        for item in wordlists:
            results.write(item+'\r\n')
    else:
        results.write('Results not found\r\n')

def PrintAll():
    grepsterSpelled, grepsterUnusual, results = RefineLists()
    PrintLists('Sample text with correct spelling',grepsterSpelled, results)
    PrintLists('Sample text with unusual words',grepsterUnusual,results)

PrintAll()

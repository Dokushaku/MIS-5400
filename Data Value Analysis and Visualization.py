import re
import nltk
from operator import itemgetter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
nltk.download('punkt')
from nltk.tokenize import word_tokenize as st
from nltk.probability import FreqDist as fd
import json
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
cl= MongoClient('mongodb://supchanda08kol50:Password44@ds050087.mlab.com:50087/azuredatabase')
mis_db= cl.azuredatabase
bigramDict=dict()
trigramDict=dict()
mostFreqWordList=dict()
count=0
col_List = mis_db.list_collection_names()
def funcJSON(NameOfItems,count):
    mostFreqWord=NameOfItems[0]
    k=0
    mostFreqWordList[k]=(mostFreqWord)
    bigramDict[k]=list(nltk.bigrams(NameOfItems))
    col_List = mis_db.list_collection_names()
    
    for key,value in mostFreqWordList.items():
        JSONDictForMongo = [
            {'Most Frequent Word in Sentence No: ' + str(count)  : value }
        ]
        bi_Name= 'Most Frequent Word in Sentence No: ' + str(count) 
        if bi_Name not in col_List:
            collectionCreated = mis_db.create_collection('Most Frequent Word in Sentence No: ' + str(count))
            collectionCreated.insert_many(JSONDictForMongo)
    #print(bigramDict)
    for key,value in bigramDict.items():
        #print(key)
        JSONDictForMongo = [
            {'BigramCollection: ' + str(count) : value }
        ]
        print(type(JSONDictForMongo),JSONDictForMongo)
        #print(dictTostr)
        bi_Name='Bigram Collection No:' + str(count)
        if bi_Name not in col_List:
            collectionCreated = mis_db.create_collection('Bigram Collection No:' + str(count))
            collectionCreated.insert_many(JSONDictForMongo)
    trigramDict[k]=list(nltk.trigrams(NameOfItems))
    #print(trigramDict)
    for key,value in trigramDict.items():
        #print(key)
        JSONDictForMongo = [
            {'TrigramCollection: ' + str(count): value }
        ]
        print(type(JSONDictForMongo),JSONDictForMongo)
        #print(dictTostr)
        tri_Name='Trigram Collection No:' + str(count)
        if tri_Name not in col_List:
            collectionCreated = mis_db.create_collection('Trigram Collection No:' + str(count))
            print(type(collectionCreated))
            collectionCreated.insert_many(JSONDictForMongo)
    k+=1

wordsDataFrame = pd.DataFrame()
with open('C:\\Users\\supratik chanda\\Downloads\\RawFrenchCorpus001.txt', 'r',encoding="utf8") as text:
    i=0
    with open('C:\\Users\\supratik chanda\\Desktop\\CorpusTurnedSentence.txt', 'w+',encoding="utf8") as appendedText:
        for each in text :
            each=each.strip()
            if len(each)>0:
                itemConcat=pd.DataFrame()
                count+=1
                wordToken = nltk.tokenize.WhitespaceTokenizer().tokenize(re.sub('[!@#$%^&*().]',' ', each))
                #print(wordToken)
                freq= fd(wordToken)
                #print(type(freq.items()))
                #print(sorted(freq.items(),key=itemgetter(1),reverse=True)[0:5])
                itemsList = sorted(freq.items(),key=itemgetter(1),reverse=True)[0:5]
                itemNames = []
                itemCountInASentence=[]
                for elem in itemsList:
                    itemNames.append(elem[0])
                    itemCountInASentence.append(elem[1])
                i+=1
                print('itemNames: ',itemNames)
                j=0
                sentNames=[]
                while j < len(itemNames):
                    sentNames.append('Sentence No:'+ str(i))
                    j+=1
                print('itemCountInaSentence: ',itemCountInASentence)
                itemNamesDFrame = pd.DataFrame(itemNames)
                itemCountInASentenceDFrame = pd.DataFrame(itemCountInASentence)
                itemConcat = pd.concat([pd.DataFrame(sentNames,columns=['Sentence No:']),pd.DataFrame(itemNames,columns=['WordName']),pd.DataFrame(itemCountInASentence,columns=['WordsCount'])],axis=1)
                
                wordsDataFrame = pd.concat([itemConcat,wordsDataFrame],axis=0)
                
                plt.figure(figsize=(8,6))
                sns.barplot(x=itemNames,y=itemCountInASentence,palette='spring')
                plt.xlabel('ItemNames')
                plt.ylabel('itemCountInASentence' )
                plt.title('First 5 words with highest frequency in a sentence No:' + str(i),fontsize=20)
                plt.show() 
                plt.pie(x=itemCountInASentence,autopct='%.0f',wedgeprops={'edgecolor':'black','linewidth':1})
                circle = plt.Circle((0,0),0.75,fc='white',color='black',linewidth=1)
                k= plt.gcf()
                k.gca().add_artist(circle)
                plt.legend(labels=itemNames)
                plt.axis('equal')
                plt.show()
                appendedText.write(str(i) + ')' + each)
                appendedText.write('\n\n')
                # Function is called where we convert the list in bigram and trigram and deposit those n-grams in mongoadatabase
                #as individual collections
                funcJSON(itemNames,count)
            if i ==15:
                break
pivotMap = wordsDataFrame.pivot('WordName','Sentence No:','WordsCount')
plt.figure(figsize=(16,10))
sns.heatmap(pivotMap,annot=True,cmap='icefire_r')
plt.show()

import re
import nltk
from operator import itemgetter
import matplotlib.pyplot as plt
import seaborn as sns
nltk.download('punkt')
from nltk.tokenize import word_tokenize as st
from nltk.probability import FreqDist as fd
with open('C:\\Users\\supratik chanda\\Downloads\\RawFrenchCorpus001.txt', 'r',encoding="utf8") as text:
    i=0
    with open('C:\\Users\\supratik chanda\\Desktop\\CorpusTurnedSentence.txt', 'w+',encoding="utf8") as appendedText:
        for each in text :
            each=each.strip()
            if len(each)>0:
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
                plt.figure(figsize=(8,6))
                sns.barplot(x=itemNames,y=itemCountInASentence,palette='spring')
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
            if i ==10:
                break
                
                

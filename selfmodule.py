import requests
import pandas as pd
from textblob import TextBlob
from matplotlib import pyplot as plt 
import numpy as np

def entereddata(entered_keyword):
        q=entered_keyword
        l=[]
        url = ('http://newsapi.org/v2/top-headlines?q='+q+'&apiKey=d7866b4abb874bb687cccf16aabe1f4f')
        response = requests.get(url)
        a = response.json()
        for i in range(len(a['articles'])):
             print(a['articles'][i]['description'])
        for i in range(len(a['articles'])):
            l.append(a['articles'][i]['description'])
        df= pd.DataFrame(l,columns=['news description'])
        nan_value = float('NaN')
        df.replace("",nan_value,inplace=True)
        df.dropna(subset = ['news description'],inplace=True)
        df.reset_index(drop=True,inplace=True)
        pos=0
        neg=0
        neut=0
        for i in range(len(df)):
            sent=TextBlob(df.iloc[i]["news description"])
            ## print(sent.sentiment)
            if sent.sentiment.polarity<0:
                pos=pos+1
            elif sent.sentiment.polarity>0:
                neg=neg+1
            else:
                neut=neut+1
        l=[pos,neg,neut]  
        output_plot(l)

def output_plot(l):
        news=["POSITIVE","NEGATIVE","NEUTRAL"]
        data = l 
        def func(pct, allvalues): 
            absolute = int(pct / 100.*np.sum(allvalues)) 
            return "{:.1f}%\n".format(pct, absolute) 
        # Creating plot 
        fig = plt.figure(figsize =(10, 7))
        fig.patch.set_facecolor('#80c1ff')
        plt.pie(data,autopct = lambda pct: func(pct, data),  labels = news,explode=(0.1,0.1,0.1),shadow = True,colors =("orange","blue","pink"),textprops = dict(color ="black") )  
        plt.legend(title ="SENTIMENT",loc ="upper right",prop={"family":"Times New Roman"},bbox_to_anchor=(0.85, 0.5, 0.5, 0.5))
        plt.text(x=1.4,y=-1.2,s="Total positive news: "+str(l[0]),fontsize=12)
        plt.text(x=1.4,y=-1.3,s="Total negative news: "+str(l[1]),fontsize=12)
        plt.text(x=1.4,y=-1.4,s="Total neutral news: "+str(l[2]),fontsize=12)
        plt.title("SENTIMENT ANALYSIS",fontsize=20)    
        # show plot 
        plt.show() 




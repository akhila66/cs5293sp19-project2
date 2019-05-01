import glob
import io
import os
import pdb
import nltk
import sys
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from scipy import spatial
from operator import itemgetter
import re

def	get_entity(text):
    persons=[]
    for sent in	sent_tokenize(text):
        from nltk import word_tokenize
        x=word_tokenize(sent)
        for chunk in ne_chunk(pos_tag(x)):
            if hasattr(chunk, 'label') and	chunk.label() == 'PERSON':
                persons.append(' '.join (c[0] for c in chunk.leaves()))   
    return persons   

def get_features(persons,text):
    dic=[]
    # f1 = c #no of times it repeating the word in sentence
    for n in persons:
        featuresvec = []
        feature = []
        feature.append(n)
        f2 = n.count(' ') #space count
        f3 = len(n) #length of name
        f4 = len(word_tokenize(text)) #length of whole sentence
        featuresvec.append(f2)
        featuresvec.append(f3)
        featuresvec.append(f4)
        feature.append(featuresvec)
        dic.append(feature)
    # print(dic)
    return dic
                     
def doextraction(glob_text):
    import re
    d=[]
    files = glob.glob(glob_text)
    # sorted(files, key=lambda x: int(re.search('(.*)/(.*)_(.*)', x).group(2)))
    files.sort(key = lambda x: int(re.search('(.*)/(.*)_(.*)', x).group(2)))
    for thefile in files[:20]:
        with io.open(thefile,'r',encoding="utf-8") as file:
            text=file.read()
            x=get_entity(text)
            y=get_features(x,text)
            d.extend(y)
    return d # trained date
                   


def get_Redacted_Features(text):
    feature=[]
    w=len(word_tokenize(text))
    count=0
    space=0
    count_word=0    
    for i in range(0,len(text)):
        if text[i]=="█":
            count_word=1
            count+=1
        elif(i+1 < len(text)):
            if text[i-1]=="█" and text[i+1]=="█":
                space+=1
                continue
            if count>0:
                l=[]
                l.append(space)
                l.append(count)
                l.append(w)
                feature.append(l)
            count=0     
            space=0
            if count_word==1:
                count_word=0
    # print(feature)
    return feature       
    
def cos_similar(v1,v2):
    result=1 - spatial.distance.cosine(v1, v2)
    return result               
                
               
def doprediction(glob_text, trainData):
    files = glob.glob(glob_text)
    files.sort(key = lambda x: int(re.search('(.*)/(.*)_(.*)', x).group(2)))
    for thefile in files:
        print(thefile)
        with io.open(thefile,'r',encoding="utf-8") as file:
            text=file.read()
            redact_vec = get_Redacted_Features(text)
            file.close()
            td=trainData
            fd=redact_vec
            similarity=[]
            count=0
            for i in fd:
                vec=[]
                count+=1
                vec.append(count)
                sim=[]
                x=[]
                for j in td:
                    temp=[]
                    temp.append(j[0])
                    temp.append(cos_similar(i,j[1]))
                    sim.append(temp)
                sim = sorted(sim,key=itemgetter(1),reverse=True)
                for i in range(0,4):
                    x.append(sim[i])
                vec.append(x)
                similarity.append(vec)
        unredactfile = thefile.replace("test/redact/","test/unredact/")
        unredactfile = unredactfile.replace(".redactor",".unredactor")
        print(unredactfile)
        with io.open(unredactfile,'w',encoding="utf-8") as file:
            output = text
            for i in similarity:
                p = "\n\n The top four most likely words that can fit for the {0} redacted word in file are: {1}\n".format(i[0],i[1])
                output = output+p
            if len(similarity)==0:
                p = "\n There are no person names in the file !"
                output = output+p
            file.write(output)
            file.close()

if __name__=='__main__':
    #	Usage:	python3	unredactor.py	'train/pos/*.txt'
    trainData = doextraction(sys.argv[-1])
    doprediction('test/redact/*.redactor',trainData)    

from nltk import word_tokenize,sent_tokenize,ne_chunk,pos_tag
import io,glob,re
import sys
import glob
import numpy
def	get_entity(text):
    persons=[]
    for sent in	sent_tokenize(text):
        from nltk import word_tokenize
        x=word_tokenize(sent)
        for chunk in ne_chunk(pos_tag(x)):
            if hasattr(chunk, 'label') and	chunk.label() == 'PERSON':
                persons.append(' '.join (c[0] for c in chunk.leaves()))   
    return persons 

def doredact(input):
    files = glob.glob(input)
    files.sort(key = lambda x: int(re.search('(.*)/(.*)_(.*)', x).group(2)))
    stats = ""
    files = files
    for thefile in files:
        print(thefile)
        with io.open(thefile,'r',encoding="utf-8") as file:
            text=file.read()
            redact_it=get_entity(text)
            stats = stats + "\n\n the person names which are redacted from - " + thefile + " - are \n-" + str(redact_it)
            for i in redact_it:
                temp=""
                for j in word_tokenize(i):
                    temp+="█"*len(j)
                    temp+=' '
                temp=temp[:-1] #removing last extra space which is adding for in b/w words
                text=text.replace(i,temp)
            file.close()
        
        redactfile = thefile.replace("test/pos/","test/redact/")
        redactfile = redactfile.replace(".txt",".redactor")
        with io.open(redactfile,'w',encoding="utf-8") as file:
            file.write(text)
            file.close()        
        with io.open("test/redact.stats",'w',encoding="utf-8") as file:
            file.write(stats)
            file.close() 

if __name__=='__main__':
    #	Usage:	python3	redactor.py	'test/pos/*.txt'
    # print(doredact(sys.argv[-1]))
    input = 'test/pos/*.txt'
    # input = sys.argv[-1]
    doredact(input)
    
import requests
from lxml import html

class Getlinks:
    # Get Link of each videos webpage
    
    def getlink(self,web):
        self.web = web
        x = requests.get(web)
        webpage = html.fromstring(x.content)
        ln = webpage.xpath('//a/@href')
        c=0
        arr=[]
        for i in ln:
            if "/course/" in i:
                if c == 0:
                    c+=1
                    continue
                arr.append(f"https://maktabkhooneh.org{i}")
                c+=1
        return arr[2::]
   
    def getMp4(self,web):
        self.web = web
        x = requests.get(web)
        webpage = html.fromstring(x.content)
        ln = webpage.xpath('//a/@href')
        h = ""
        c=1
        for i in ln:
            if "video-resolver" in i and c == 1:
                ar = x.text.split("<")
                for b in ar:
                    if "h1" in b[0:2]:
                        h = (b[33:])
                return i,h
                c+=1
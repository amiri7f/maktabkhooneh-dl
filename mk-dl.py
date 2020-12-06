import requests
from lxml import html
import download
from download import download

weblink = 'https://maktabkhooneh.org/course/%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1-mk137/%D9%81%DB%8C%D9%84%D9%85-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-ch185/%D9%88%DB%8C%D8%AF%DB%8C%D9%88-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-%D8%AC%D9%84%D8%B3%D9%87-%D8%AF%D9%88%D9%85-%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1/'
def getlink(web):
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
def getMp4(web):
    x = requests.get(web)
    webpage = html.fromstring(x.content)
    ln = webpage.xpath('//a/@href')
    c=1
    for i in ln:
        if "video-resolver" in i and c == 1:
            return i
            c+=1
arr=[]
for i in getlink(weblink):
    arr.append(getMp4(weblink))
for i in arr:
    download(i, "C:\a.mp4", progressbar=True)
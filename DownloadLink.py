import requests
from lxml import html
from LinkList import Getlinks

class DlLink:

    def DlList(self):
        webln = 'https://maktabkhooneh.org/course/%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1-mk137/%D9%81%DB%8C%D9%84%D9%85-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-ch185/%D9%88%DB%8C%D8%AF%DB%8C%D9%88-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-%D8%AC%D9%84%D8%B3%D9%87-%D8%AF%D9%88%D9%85-%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1/'
        lnArr = Getlinks().getlink(web = webln)
        arr=[]
        for i in lnArr:
            arr.append(Getlinks().getMp4(i))
        return arr
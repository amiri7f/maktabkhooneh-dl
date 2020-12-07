import requests
from lxml import html

class Getlinks:

    # Return List of video`s link from given page
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
        return arr[3::]
   
    # Return name and download link of a video from each page
    def getMp4(self,webs,cookieSid):
        self.webs = webs
        self.cookieSid = cookieSid
        ## cookies 
        cookie = {'sessionid': cookieSid,
        'never_show_phone_number':'true',
        # 'csrftoken':'RSA3AUZyo1rQihHnh5UUclPGKH4pd9qFSYKewIaSnQ2rbKFGbdC8xbxUwL6AE0if'
        }
        # Use python requests module to get related url and send cookies to it with cookies parameter. 
        x = requests.get(webs , cookies=cookie)
        webpage = html.fromstring(x.content)
        ln = webpage.xpath('//a/@href')
        c=1
        for i in ln:
            if "video-resolver" in i and c == 1:
                # print video Dl link
                print(f"---- {i} ----")
                # Get Video name 
                ar = x.text.split("<")
                for b in ar:
                    if "h1" in b[0:2]:
                        print(c,b[33:])
                        name = (b[33:])
                return i,name
                c+=1
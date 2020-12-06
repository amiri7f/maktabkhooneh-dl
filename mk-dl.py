from download import download
from os import getcwd
import requests
from DownloadLink import DlLink as List

# from requests.auth import HTTPBasicAuth 

# cookies = dict(sessionid = 's3wuatcuo2wbi1d4ei1zzikzht0wzhud')
 
# Use python requests module to get related url and send cookies to it with cookies parameter. 
response = requests.get("https://maktabkhooneh.org/")

# response = requests.put('https://maktabkhooneh.org/', data = {'tessera':'pewega3654@demail3.com','password':'Awdrg@12'})
if "password" in str(response.content):
    print('jkhlkghjgjf')
print(response)

#   ToDo !!!! Athuntecate pewega3654@demail3.com

# ln = 'https://maktabkhooneh.org/course/%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1-mk137/%D9%81%DB%8C%D9%84%D9%85-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-ch185/%D9%88%DB%8C%D8%AF%DB%8C%D9%88-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-%D8%AC%D9%84%D8%B3%D9%87-%D8%AF%D9%88%D9%85-%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1/'
        
# arr = List().DlList(webln = ln)
# c=len(arr)
# print(f"Total : {c}")

# for i in arr:
#     path = download(i[0], getcwd()+"/"+i[1]+".mp4",progressbar=True)
from download import download
from os import getcwd
from DownloadLink import DlLink as List

#   ToDo !!!! Athuntecate pewega3654@demail3.com

ln = input("Link :")
Cookie = 'ok9ets8ftx7p2c3wth77sfksyryfjlmk'

arr = List().DlList(webln = ln, sid = Cookie)

c=len(arr)
print(f"Total : {c}")

for i in arr:
    path = download(i[0], getcwd()+i[1]+f" {str(i[0][-5:-8:-1])[::-1]}"+".mp4", progressbar=True)
    # path = download(i[0], getcwd()+f"/{i[0][-5:-8:-1]} - "+i[1]+".mp4", progressbar=True)

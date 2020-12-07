from download import download
from os import getcwd
from DownloadLink import DlLink as List

#   ToDo !!!! Athuntecate pewega3654@demail3.com

ln = 'https://maktabkhooneh.org/course/%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1-mk137/%D9%81%DB%8C%D9%84%D9%85-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-ch185/%D9%88%DB%8C%D8%AF%DB%8C%D9%88-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-%D8%AC%D9%84%D8%B3%D9%87-%D8%AF%D9%88%D9%85-%D8%A7%D8%B9%D8%AF%D8%A7%D8%AF-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-%D8%B9%D9%85%D9%88%D9%85%DB%8C-%DB%B1/'
Cookie = 'ok9ets8ftx7p2c3wth77sfksyryfjlmk'

arr = List().DlList(webln = ln, sid = Cookie)

c=len(arr)
print(f"Total : {c}")

for i in arr:
    path = download(i[0], getcwd()+f"/{i[0][-5:-8:-1]} - "+i[1]+".mp4", progressbar=True)

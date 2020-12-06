from download import download
from os import getcwd
from DownloadLink import DlLink as List

arr = List().DlList()

print(arr)
print(len(arr))
# for i in arr:
#     path = download(i[0], getcwd()+"/"+i[1]+".mp4",progressbar=True)
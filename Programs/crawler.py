import requests
from bs4 import BeautifulSoup
import multiprocessing
import time
from util import prepDir
import requests
import urllib.request
import os.path

baseUrl = 'https://aclanthology.org/events/emnlp-2019/'
#save all the links to mainlinks
mainlinks = []

def crawl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a', class_='badge badge-primary align-middle mr-1')
    for link in links:
        mainlinks.append(link.get('href'))
        
    #remove the first link 
    mainlinks.pop(0)


save_path = 'C:\\Users\\tonny\\OneDrive\\Desktop\\Projects\\IT Workshop Project\\EMNLP\\PDF'

def download(download_url):
    save_path = 'C:\\Users\\tonny\\OneDrive\\Desktop\\Projects\\IT Workshop Project\\EMNLP\\PDF'

    file_name = 'document' + str(mainlinks.index(download_url)) + '.pdf'

    #check if the pdf file is already downloaded
    if os.path.isfile(os.path.join(save_path, file_name)):
        print('File already exists')
        return
    else:
        response = urllib.request.urlopen(download_url)
    
    
        file_path = os.path.join(save_path, file_name)
        with open(file_path, 'wb') as f:
            print("Downloading %s" % file_name)
            f.write(response.read())
            f.close()


if __name__ == "__main__" :
        crawl(baseUrl)
        for link in mainlinks:
            download(link)
            
            
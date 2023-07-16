from bs4 import BeautifulSoup
import requests
import pandas as pd

def extact(file_path):
  data = pd.read_csv(file_path)
  rows,col = data.shape
  count = 0
  missed_one = []


  for i in range(rows):
    url = requests.get(data.URL[i])
    soup = BeautifulSoup(url.text, "html.parser")
    try:
      title = soup.find('h1')
      parent = soup.find("div",class_ = "td-post-content tagdiv-type").find_all_next('p')
      f = open(f'text_files/{data.URL_ID[i]}.txt',"a")
      print(f.mode)
      f.write(title.text)
      f.write("\n")
      for p in parent:
        f.write(p.text)
        f.write("\n")
      f.close()
      

    except :
      print(i)
      missed_one.append(i)
      
  
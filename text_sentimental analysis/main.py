import os
from analysize import text_analysis
import csv
import pandas as pd 



directory_files = os.listdir("text_files/")
print(directory_files)
header = ["URL_ID","URL","POSITIVE SCORE",	"NEGATIVE SCORE","POLARITY SCORE",	"SUBJECTIVITY SCORE",	"AVG SENTENCE LENGTH",	"PERCENTAGE OF COMPLEX WORDS",	"FOG INDEX",	"AVG NUMBER OF WORDS PER SENTENCE",	"COMPLEX WORD COUNT",	"WORD COUNT",	"SYLLABLE PER WORD",	"PERSONAL PRONOUNS",	"AVG WORD LENGTH"]





for files in directory_files:
  id = files.split(".")[0]
  #print(id)
  try:
    with open("output.csv", "a") as f:
      analysis = text_analysis(files)
      csvwriter = csv.writer(f)
      csvwriter.writerow(id)
      csvwriter.writerow(analysis)
      f.close()
    print("sucessfully written the values") 
      
  except Exception as e:
    print(e)
    print(files)

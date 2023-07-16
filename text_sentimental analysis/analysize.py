from numpy import average
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import textstat
import regex as re


 


def find_complex_words(text):
  complex_words = []
  for word in text.split():
    syllable_count = textstat.syllable_count(word)
    if syllable_count >= 2:
      complex_words.append(word)
  return len( complex_words)


def count_sentences(text):
  sentences = 0
  for i in range(len(text)):
    if text[i] == ".":
      sentences += 1
  return sentences

def average_words_per_sentence(text):
  total_words = len(text.split())
  number_of_sentences = text.count(".")
  average_words_per_sentence = total_words / number_of_sentences
  return average_words_per_sentence


  

def syllable_counts(word):
  return textstat.syllable_count(word)

def find_personal_pronouns(text):
  personal_pronouns = []
  pattern = r"/(I|me|you|he|she|it|we|us|they|them)/"
  for match in re.finditer(pattern, text):
    personal_pronouns.append(match.group(0))
  return len(personal_pronouns)

def average_word_length(text):
  words = text.split()
  total_length = 0
  for word in words:
    total_length += len(word)
  average_word_length = total_length / len(words)
  return average_word_length





def text_analysis(files):

  own_stopwords = open("all_stop_word.txt",'r').read().lower()

  text = open(f"text_files/{files}",'r',encoding="utf8").read().lower()

  positive = open("positive-words.txt",'r').read().lower()
  negative = open("negative-words.txt",'r').read().lower()

  pos = 0
  neg = 0
  total_number_of_words = text.split()
  number_of_sentence = count_sentences(text)

  average_sent = len(total_number_of_words)/number_of_sentence
  complex_words_percentage = (find_complex_words(text)/len(total_number_of_words))*100

  Fog_Index =  0.4*(average_sent + complex_words_percentage)
  AverageNumberofWordsPerSentence =  average_words_per_sentence(text)

  complex_word_count = find_complex_words(text)

  word_count = text.split()
  PERSONALPRONOUNS = find_personal_pronouns(text)
  AVGWORDLENGTH = average_word_length(text) 

  data = text
  stopWords = stopwords.words('english')
  stopWords.extend(own_stopwords)
  words = word_tokenize(data)

  wordsFiltered = []
  length  = len(text)

  for w in words:
      if w not in stopWords:
          wordsFiltered.append(w)
  for word in wordsFiltered:
    if word in positive:
      pos+=1
    elif word in negative:
      neg-=1
    else:
      pass
  SYLLABLEPERWORD = syllable_counts(wordsFiltered[0])
  positive_score = ((pos/len(wordsFiltered)))
  negative_score = ((neg/len(wordsFiltered)))
  pollarity_score = (positive_score - negative_score)/((positive_score + negative_score)+0.000001)
  Subjectivity_Score = (positive_score + negative_score)/(len(wordsFiltered)+0.000001) 

  return positive_score,negative_score,pollarity_score,Subjectivity_Score,average_sent,complex_words_percentage,Fog_Index,AverageNumberofWordsPerSentence,complex_word_count,SYLLABLEPERWORD, PERSONALPRONOUNS,AVGWORDLENGTH



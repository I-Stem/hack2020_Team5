import pytesseract
import cv2
import os
from gtts import gTTS
import PIL
from PIL import Image
from pdf2image import convert_from_path
import spacy
import re
import nltk
from nltk.corpus import stopwords


from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from nltk.tokenize import word_tokenize, sent_tokenize
text=[]
with open("goods.txt","r+") as f:
    text.append(f.readlines())

data = ""
for i in text[0]:
    data += i

print(summarize(data, ratio = 0.5))



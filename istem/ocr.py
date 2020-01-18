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
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import time

language = "en"

app = Flask(__name__)
CORS(app)

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()


@app.route("/imgread", methods=['GET', 'POST'])
def real_time_stream():
    time.sleep(8)
    video_capture = cv2.VideoCapture('http://172.16.101.152:8080/video')

    laplas = []
    frams = []
    for i in range(100):
        if i%5 == 0:
            ret,frame  = video_capture.read()
            #img = cv2.imread(img_path)
            img = cv2.resize(frame,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_LINEAR)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            check = variance_of_laplacian(img)
            frams.append(img)
            laplas.append(check)

            print("++++++++++++++++=>",check)

    video_capture.release()


    max_value = max(laplas)
    max_index = laplas.index(max_value)
    print(max_value)
    print(max_index)

    result = pytesseract.image_to_string(frams[max_index],lang = 'eng')
    """
    path = "igg.jpg"

    print(result)
    
    speech = gTTS(text = result, lang = language, slow = False)
    speech.save("book.mp3")
    os.system("play book.mp3")
    """
    with open("goods.txt","w+") as f:
            f.write(result)
    return "IMG Done"

@app.route("/test", methods=['GET', 'POST'])
def test():
    data = request.json
    hello = data["hello"]
    return hello


@app.route("/pdfread", methods=['GET', 'POST'])
def pdf_text_converter():
    data = request.json
    #pdf_file = request.files["file"]
    pdf_file = data["mypdf"]
    count = 0
    image_list = []
    pages = convert_from_path(pdf_file,500)
    for page in pages : 
        image = str(count)+".jpeg"
        image_list.append(image)
        page.save(image,'JPEG')
        count = count + 1
    for i in image_list:

        img = cv2.imread(i)
        
        #img = cv2.resize(img,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_LINEAR)
        #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        result =str(pytesseract.image_to_string(Image.open(i)))
        with open("goods.txt","w+") as f:
            f.write(result)
        return "Done"
'''
pdf_file = "doc.pdf"
text = pdf_text_converter(pdf_file)
textsummary(text)
'''
def textsummary(text):
    text = text.lower()
    text = re.sub("\s+"," ",text)
    text = re.sub('[^a-zA-Z]', ' ',text)
    #txt_words = text.split(" ")
    nlp = spacy.load("en_core_web_sm")
    pretext = nlp(text)

    xents = pretext.ents

    nounchunks = [i for i in pretext.noun_chunks]
    text_dict = word_frequency(nounchunks)
    print(text_dict)
    print(xents)

    print("\n\n\n")


    print(nounchunks)
    print(str(len(xents))+"   "+str(len(nounchunks)))

    for i in xents:
        print(str(i) + str(i.label_) + spacy.explain(i.label_))

def word_frequency(text_list):
    word_dict = {}
    stopword = set(stopwords.words("english"))        
    for i in text_list:
        if i not in stopword:
            if i not in word_dict :
                word_dict[i] = 1
            else :
                word_dict[i] += 1
    return word_dict


@app.route("/summary", methods=['GET', 'POST'])
def wor_summary():
    text=[]
    with open("goods.txt","r+") as f:
        text.append(f.readlines())

    data = ""
    for i in text[0]:
        data += i

    sum1 = summarize(data, ratio = 0.5)
    print(sum1)
    return jsonify(message=sum1)

@app.route("/keyword", methods=['GET', 'POST'])
def wor_keyword():
    text=[]
    with open("goods.txt","r+") as f:
        text.append(f.readlines())

    data = ""
    for i in text[0]:
        data += i

    kword = keywords(data) 
    return jsonify(message = kword)

@app.route("/readentire", methods=['GET', 'POST'])
def entiretext():
    text=[]
    with open("goods.txt","r+") as f:
        text.append(f.readlines())

    data = ""
    for i in text[0]:
        data += i

    return jsonify(message = data)


@app.route("/filesave", methods=["GET","POST"])
def filesave():
    fsave = request.files["file"]
    fsave.save("/home/supreeth/istem/MYPDF.pdf")
    #with open('/home/supreeth/istem/MYPDF.pdf', 'wb') as fd:
    #    fd.write(fsave)

    return "/home/supreeth/istem/MYPDF.pdf"

if __name__ == "__main__":

    app.run(host= '172.16.101.103',port = 5001,debug=True)
    """
    pdf_file = "doc.pdf"
    text = pdf_text_converter(pdf_file)
    with open("goods.txt","w+") as f:
        f.write(text)

    print(text)
    print("\n\n\n========")
    textsummary(text)
    """


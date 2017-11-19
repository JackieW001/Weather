from flask import Flask, render_template
#import request

app = Flask(__name__)

@app.route("/")
def root():
    '''
    data = open('request.json', 'rb').read()
    key = open('apiKey.txt', 'rb').read()
    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=%s'%(key), data=data, headers={'Content-Type': 'application/json'})
    print response.text
    '''
    return render_template("home.html", title="Weather")

def getfile():
    return ""

def baseEncode64():
    return ""

def callgvision():
    return ""

def readgvision():
    return ""
    
@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

def callf2f():
    return ""

def f2flinks():
    links = []
    return links

def f2fimgs():
    imgs = []
    return imgs

def f2ftitles():
    titles = []
    return titles

if __name__ == '__main__':
    app.debug = True
    app.run()

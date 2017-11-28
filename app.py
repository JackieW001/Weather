from flask import Flask, render_template, request
import requests, base64, json, os
app = Flask(__name__)

newJSON = ""


@app.route('/', methods = ['GET','POST'])
def root():
    '''

    key = open('apiKey.txt', 'rb').read()
    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=%s'%(key), data=data, headers={'Content-Type': 'application/json'})
    print response.text
    '''

    #print data

    key2 = open('f2fKey.txt', 'rb').read()


#    print 'TESTING'
#    for keys in dict['responses']['labelAnnotations']:
#        if keys == 'description':
#            print dict['responses']['labelAnnotations'][keys]
#    print '---------'
    #response2 = requests.post(url='https://food2fork.com/api/search?key=%s'%(key2))


    #static/images folder
    images=[]
    for filename in os.listdir('static/images'):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            images.append(os.path.join('../static/images', filename))
        else:
            continue
    first=images[0]
    images=images[1:]
    return render_template("home.html", title="Weather", images=images, first=first)


def getfile():
    return ""

def baseEncode64(imagePath):
    with open(imagePath, "rb") as image_file:
        encode = base64.b64encode(image_file.read())
        return encode

def replaceRequest(imagePath):
    encodeString = baseEncode64(imagePath)
    data = open('request.json', 'rb').read()
    newJSON = data.replace("toBeReplaced", encodeString)
    return newJSON

def replaceRequest2(baseSixtyFour):
    data = open('request.json', 'rb').read()
    newJSON=data.replace("toBeReplaced", baseSixtyFour)
    return newJSON

def callgvision():
    return ""

def readgvision():
    return ""

@app.route("/recipes", methods=['POST'])
def recipes():
    query = pullquery()
    print query
    recipes = f2finfo(callf2f(query))
    return render_template("recipes.html", data = recipes)

def pullquery():
    if request.form['submitted'] == "Submit":
        newJSON = replaceRequest2(request.form["textBox"])
        #print newJSON
    key = open('apiKey.txt', 'rb').read()
    data = newJSON
    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=%s'%(key), data=data, headers={'Content-Type': 'application/json'})
    dict = json.loads(response.text)

    recipes = dict["responses"][0]["labelAnnotations"]
    for food in recipes:
        if "food" in food["description"]:
            pass
        elif "dish" in food["description"]:
            pass
        elif "cuisine" in food["description"]:
            pass
        else:
            retVal = food["description"]
            break
    return retVal


def callf2f(userquery):
    key = open('f2fKey.txt', 'rb').read()
    key = key.strip()
    query = userquery
    r = requests.get('http://food2fork.com/api/search?key=%s&q=%s' %(key, query))
    data = r.json()["recipes"]
    return data

def f2finfo(data):
    recipes = []
    for recipe in data:
        temp = []
        temp.append(recipe["title"])
        temp.append(recipe["source_url"])
        temp.append(recipe["image_url"])
        recipes.append(temp)
    return recipes

if __name__ == '__main__':
    app.debug = True
    app.run()

#import attractiveness
import os
import os, os.path
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
from flask import Flask, request, render_template, url_for, redirect
import numpy as np
import usemodel
from PIL import Image
import os, os.path
import matplotlib.pyplot as plt
#import keras


app = Flask(__name__)

logged_in = True # Change this depending on whether the user is logged in (for later)

@app.route('/')
def index():
    return render_template('home.html',login = logged_in)



@app.route('/start')
def start():
    return render_template('start.html',login = logged_in)


#file upload: http://www.thamizhchelvan.com/python/simple-file-upload-python-flask/

@app.route("/input_image")
def fileFrontPage():
    return render_template('fileform.html', login = logged_in)


@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':       
            photo.save(os.path.join('C:/Users/Public/Pictures', photo.filename))
    #return redirect(url_for('fileFrontPage'))
    return render_template('upload.html', login = logged_in)


@app.route('/attractiveness')
def attractiveness():
    #print(request.form['pic'])
    imgs = []
    path = 'C:/Users/Public/Pictures'
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path,f)))
    
    print (imgs)

    return render_template('attractiveness.html',login = logged_in)

@app.route('/cluster1')
def cluster1(): #you are a woman
    #print(request.form['pic'])
    imgs = []
    path = 'C:/Users/Public/Pictures'
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(os.path.join(path,f))
    imagefull = Image.open(open(imgs[0],"rb"))
    image = imagefull.resize([800,640])
    npimage = np.array(image)
    print (npimage.shape)
    group = usemodel.classify_photo(npimage,0)
    group = group[0]

    
    paths = usemodel.similar_photos(group, 0)

    
    for i in range(len(paths)):
        img = imread(paths[i])
        Image.fromarray(img).show()
    
    
    return render_template('cluster1_result.html',group = group)

@app.route('/cluster2')
def cluster2(): #you are a man
    #print(request.form['pic'])
        #print(request.form['pic'])
    imgs = []
    path = 'C:/Users/Public/Pictures'
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(os.path.join(path,f))
    imagefull = Image.open(open(imgs[0],"rb"))
    image = imagefull.resize([800,640])
    npimage = np.array(image)
    print (npimage.shape)
    group = usemodel.classify_photo(npimage,1)
    group = group[0]
    
    paths = usemodel.similar_photos(group, 1)

    for i in range(len(paths)):
        img = imread(paths[i])
        Image.fromarray(img).show()
        
    return render_template('cluster2_result.html',group = group)
  

if __name__ == '__main__':
    app.run(debug=True)

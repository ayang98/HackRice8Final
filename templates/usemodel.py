from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import os
import numpy as np
import random
from matplotlib.image import imread
import pickle

def classify_photo(photo, gender):
    savedir = "C:/Users/yalex/Pictures"
    pcafile = ["C:/Users/yalex/FlaskApp/PCAfiles/pca64modelfemale.p", "C:/Users/yalex/FlaskApp/PCAfiles/pca64modelmale.p"]
    kmeansfile = ["C:/Users/yalex/FlaskApp/PCAfiles/kmeanswomen.p", "C:/Users/yalex/FlaskApp/PCAfiles/kmeansmen.p"]
    os.chdir(savedir)
    pca = pickle.load(open(pcafile[gender],"rb"))
    kmeans = pickle.load(open(kmeansfile[gender],"rb"))
    npphoto = np.asarray(photo)
    npphoto = np.reshape(npphoto, (1,1536000))
    pcaphoto = pca.transform(npphoto)
    group = kmeans.predict(pcaphoto)
    return group

def similar_photos(group, gender):
    filedir = ["C:/Users/yalex/FlaskApp/TinderPhotos/Women/", "C:/Users/yalex/FlaskApp/TinderPhotos/Men/"]
    fileclass = ["C:/Users/yalex/FlaskApp/PCAfiles/femaleclasslist.p", "C:/Users/yalex/FlaskApp/PCAfiles/maleclasslist.p"]
    fileclasses = pickle.load(open(fileclass[gender],"rb"))
    photos = fileclasses[group]
    fileindex = random.sample(range(len(photos)),8)
    files = []
    for i in fileindex:
        files.append(filedir[gender]+photos[i])
    return files
import os
import pickle

def save(fname, object):
    file = open(fname, 'wb')
    pickle.dump(object,file,protocol = 0)
    file.close()

def load(fname):
    file = open(fname, 'rb')
    object = pickle.load(file)
    file.close()
    return object

def extract():
    posts = []
    names = []
    #searching for all the manpages
    for (currdir,subdir,fileshere) in os.walk('../manpages'):
        for fname in fileshere:
            path = os.path.join(currdir,fname)
            posts.append(open(path).read())
            names.append(str(fname[:-4]))

    return posts,names
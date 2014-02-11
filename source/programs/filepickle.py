import os
import cPickle

def save(fname, object):
    with open(fname, 'wb') as fp:
        cPickle.dump(object, fp)

def load(fname):
    with open(fname, 'rb') as fp:
        object = cPickle.load(fp)
    return object

def extract():
    posts = []
    names = []
    #searching for all the manpages
    for (currdir,subdir,fileshere) in os.walk('../manpages'):

        for fname in fileshere:
                path = os.path.join(currdir,fname)
                posts.append(open(path).read())
                names.append(str(fname))

    return posts,names
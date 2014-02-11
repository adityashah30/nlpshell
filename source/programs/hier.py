import os
import filepickle as fp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, MiniBatchKMeans
from doc_vector import StemmedTfidfVectorizer
import numpy as np

def cluster_doc_vec(similar_indices, posts):
	similar = []
	for i in similar_indices:
		similar.append(posts[i])

	return similar

def hierarchy_creator(level):
	str1 = 'DVL'
	str2 = 'VZL'
	str3 = 'KML'
	str4 = 'PL'
	for i in xrange (level):
		for (currdir,subdir,fileshere) in os.walk('../clusterdata'):
			for fname in fileshere:
				if fname[:4] == str1+str(i):
					
					xt = fp.load(os.path.join(currdir,fname))
					posts  = fp.load(os.path.join(currdir,(str4+fname[3:])))

					km = KMeans(n_clusters=15, init='k-means++', n_init=1,verbose=1)
					km.fit(xt)
					fkm = os.path.join(currdir,str3+str(i)+fname[4:])
					fp.save(fkm,km)
					
					print fkm
					
					clusters = km.cluster_centers_.shape[0]
					
					for j in xrange(clusters):
						dvname = fname[:3]+str(i+1)+fname[4:]+'.'+str(j)
						newpostname = str4+str(i+1)+fname[4:]+'.'+str(j)
						vectorizername = str2+str(i+1)+fname[4:]+'.'+str(j)
						
						similar_indices = (km.labels_ == j).nonzero()[0]
						newpost = cluster_doc_vec(similar_indices,posts)
						fp.save(os.path.join(currdir,newpostname),newpost)
						print newpostname

						vectorizer = StemmedTfidfVectorizer(min_df = 1,stop_words = 'english', decode_error = 'ignore')
						fp.save(os.path.join(currdir,vectorizername),vectorizer)

						fp.save(os.path.join(currdir,dvname),vectorizer.fit_transform(newpost))

def main():
	hierarchy_creator(2)

if __name__ == '__main__':
	main()
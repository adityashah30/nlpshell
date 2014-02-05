import os
import filepickle as fp
from sklearn.cluster import KMeans
import numpy as np

def main():
	xt = fp.load('../clusterdata/X_train')
	num_sample, num_features = xt.shape
	kmo=KMeans(n_clusters=200, init='random', n_init=1,verbose=1).fit(xt)
	fp.save('../clusterdata/km',kmo)
	del kmo
	km = fp.load('../clusterdata/km')
	label = np.reshape(km.labels_, num_sample)
	print km.labels_
	indices = (km.labels_==1).nonzero()
	print indices
if __name__ == '__main__':
	main()
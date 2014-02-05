from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem
import filepickle as fp

#new vectorizer class integrating stemmer
class StemmedTfidfVectorizer(TfidfVectorizer):
    #overriding the build_analyzer function
    def build_analyzer(self):
        #inititalising stemmer
        english_stemmer = nltk.stem.SnowballStemmer('english')
            
        analyzer = super(StemmedTfidfVectorizer,self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))


def main():

    posts,names = fp.extract() #loading the posts

    #initializing the vectorizer
    vectorizer = StemmedTfidfVectorizer(min_df = 1,stop_words = 'english', decode_error = 'ignore') 

    fp.save('../clusterdata/X_train',vectorizer.fit_transform(posts))
    xt = fp.load('../clusterdata/X_train')
    num_sample, num_features = xt.shape
if __name__ == '__main__':
    main()
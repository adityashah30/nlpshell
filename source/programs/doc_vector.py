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

    fp.save('../clusterdata/PL0N0',posts)
    fp.save('../clusterdata/DVL0N0',vectorizer.fit_transform(posts))
    fp.save('../clusterdata/VZL0N0',vectorizer)

if __name__ == '__main__':
    main()
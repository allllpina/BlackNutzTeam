import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

class Movie_predictor:
    def __init__(self, movie_dataset):
        self.__movies = pd.read_csv(movie_dataset)
        self.__indices = pd.Series(self.__movies.index, index=self.__movies['original_title']).drop_duplicates()
        self.__calculate_sig_matrix()

    def __calculate_sig_matrix(self):
        tfv = TfidfVectorizer(min_df=3,  max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')
        tfv_matrix = tfv.fit_transform(self.__movies['overview'])
        self.__sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
        
    def give_recomendations(self, title, count):
        idx = self.__indices[title]

        sig_scores = list(enumerate(self.__sig[idx]))

        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        sig_scores = sig_scores[1: count + 1]

        movie_indices = [i[0] for i in sig_scores]

        return self.__movies[['original_title', 'overview', 'original_language']].iloc[movie_indices]

# mp = Movie_predictor('./data/movies_cleaned.csv')
# print(mp.give_recomendations("Avatar", 10))

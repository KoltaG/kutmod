import pandas as pd

class Recommender(object):
    
       
    def get_countries(self):
        self.foreignMovies = pd.read_csv ('source/foreignMoviesClustered.csv')
        return sorted(self.foreignMovies['country'].unique())
    def get_movies(self):
        self.top100Movies = pd.read_csv ('source/top100Clustered.csv')
        return self.top100Movies['title'].unique()
    def write_results(self, selectedMovie, selectedCountry):
            selectedMovieRow= self.top100Movies[self.top100Movies['title'] == selectedMovie]
            selectedMovieCluster= selectedMovieRow['cluster'][0]
            foreignMovies = self.foreignMovies[(self.foreignMovies.cluster == selectedMovieCluster) & (self.foreignMovies.country == selectedCountry)]
            foreignMovies.sort_values(by=['rating'], ascending=True, inplace=True)
            recommendedMovies = []
            i = 0
            for index, row in foreignMovies.iterrows():
                i += 1
                if i > 5:
                    break
                recommendedMovies.append(row['title'])
            if (recommendedMovies.__len__() == 0): 
                recommendedMovies.append("No movies found")   
            return recommendedMovies

import pandas as pd

class Recommender(object):
    
       
    def get_countries(self):
        foreignMovies = pd.read_csv ('source/foreignMoviesClustered.csv')
        return foreignMovies['country'].unique()
    def get_movies(self):
        top100Movies = pd.read_csv ('source/top100Clustered.csv')
        return top100Movies['title'].unique()    
    def write_results(self, selectedMovie, selectedCountry):
           if selectedMovie != "" and selectedCountry != "": 
            foreignMovies = pd.read_csv ('source/foreignMoviesClustered.csv')
            top100Movies = pd.read_csv ('source/top100Clustered.csv')
            selectedMovieRow= top100Movies[top100Movies['title'] == selectedMovie]

            selectedMovieCluster= selectedMovieRow['cluster'][0]
            foreignMovies = foreignMovies[(foreignMovies.cluster == selectedMovieCluster) & (foreignMovies.country == selectedCountry)]
            foreignMovies.sort_values(by=['rating'], ascending=True, inplace=True)

            print("Your movies:",)
            i = 0
            for index, row in foreignMovies.iterrows():
                i += 1
                if i > 2:
                    break
                print(row['title'])
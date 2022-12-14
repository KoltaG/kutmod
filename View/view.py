import ttkbootstrap as ttk
from recommender import Recommender

class View(ttk.Window):
    def __init__(self):
        """
        Constructor of View class.

        """

        super(View, self).__init__()
        
    
    def show(self) -> None:
        """
        Displays the main window.

        :return: None
        """
        self.title("Foreign Movies")
        self.state("zoomed")

        self.utils = Recommender()
        self.countries = self.utils.get_countries()
        self.top100 = self.utils.get_movies()
        
     # Dropdown menu options
        optionsCountries = self.countries
        optionsTop100 = self.top100
        # datatype of menu text
        self.selectedCountry = ttk.StringVar()
        self.selectedMovie = ttk.StringVar()

        self.selectedCountry.set("Greece")
        self.selectedMovie.set("The Godfather")

        # Create Dropdown menu
        dropCountries = ttk.OptionMenu( self , self.selectedCountry , *optionsCountries )
        dropCountries.pack()
        dropTop100 = ttk.OptionMenu( self , self.selectedMovie , *optionsTop100 )
        dropTop100.pack()

        # Create button, it will change label text
        button = ttk.Button( self , text = "recommend" , command = self.getMovies, ).pack()
        
        # Create Label
        self.label = ttk.Label( self , text = " " )
        self.label.pack()

        self.mainloop()    
  
    def getMovies(self):
        try:
            recommendedMovies = self.utils.write_results(self.selectedMovie.get(), self.selectedCountry.get())
            self.label.configure(text="\n".join(recommendedMovies))
        except:
            self.label.configure(text="No movies found")
           

       

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
        options = self.countries
        options2 = self.top100
        # datatype of menu text
        clicked = ttk.StringVar()
        clicked2 = ttk.StringVar()
        
        clicked.set('Greece')
        clicked2.set('The Godfather')
        # Create Dropdown menu
        drop = ttk.OptionMenu( self , clicked , *options )
        drop.pack()
        drop2 = ttk.OptionMenu( self , clicked2 , *options2 )
        drop2.pack()
        s = ttk.Style()
        # Create button, it will change label text
        def getMovies(self):
            self.utils.write_results(clicked.get(), clicked2.get())
        button = ttk.Button( self , text = "click Me" , command = getMovies(self), ).pack()
        
        # Create Label
        label = ttk.Label( self , text = " " )
        label.pack()

        self.mainloop()    
  
       

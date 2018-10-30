import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name) as fp:
            reader = csv.reader(fp)
            for line in reader:
                player = Player(*line)
                yield player
                
        

    def search(self, country=None, year=None, age=None, position=None):

        input_values = [country, year, age, position]
        if not any (input_values):
            raise ValueError() 
        
        # loops through Player object from all()
        for player in self.all():
            # player.date_of_birth = '(1991-09-09)9 September 1991 (aged 22)'
            # slice notation from the end to get player.age = player.date_of_birth[-3:-1]
            player.age = player.date_of_birth[-3:-1]
            
            if (not country or player.country == country) and (not year or player.year== year) and (not age or player.age == age) and (not position or player.position == position):                                            
                yield player
                
      
                


#importing supporting libraries
import numpy as np
import pandas as pd
import datetime
from textblob import TextBlob

# This class will deal with a majority of the data processing that this project will
# handle.
class Data():

    def __init__(self):
        self.index = pd.read_csv('./data/index.csv')
        self.letters = pd.read_json('./data/letters.json')
        #self.data['deadline'] = pd.to_datetime(self.data['deadline'], infer_datetime_format=True)


    # My plan for the data analysis - I need to get the data broken out by two dates
    # That the user enters.
    # I need to ensure that the letters are only in English - this needs to be
    # the first sort.
    # Place is tied to to the places.csv that also has country in it 

    #This method will get the sentiment of the lines spoken by the four main characters
    #for each season. How this will work is that each line, by character, will get its sentiment
    #and then an average will be found.
    def sentimentByCharacter(self, season):
        #Here I get a smaller data set based on where the season is set to
        #what the user wants.
        season_data_set = self.data[(self.data.Season == season)]
        season_data = []
        #This list will hold the main characters that will be examined
        characters = ['Carrie', 'Miranda', 'Charlotte', 'Samantha']
        columns = ['Character', 'Lines']
        season_data.append(columns)
        #looping through the characters list
        for character in characters:
            rows = []
            #resetting the dataset each time we loop through the data.
            character_data_set = season_data_set
            speaker_data_set = character_data_set[(character_data_set.Speaker == character)]
            valance_list = []
            for line in speaker_data_set['Line']:
                valance = TextBlob(line)
                valance_list.append(valance.sentiment[0])
            list_total = sum(valance_list)
            average = list_total / len(valance_list)
            average = format(average, '.5f')
            rows.append(character)
            rows.append(float(average))
            season_data.append(rows)
        return season_data

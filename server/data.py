#importing supporting libraries
import numpy as np
import pandas as pd
import json
import datetime
from textblob import TextBlob

# This class will deal with a majority of the data processing that this project will
# handle.
class Data():

    def __init__(self):
        self.index = pd.read_csv('./data/index.csv')
        #self.letters = pd.read_json('./data/letters.json')
        self.letters = pd.read_json('./data/letters.json', typ='series')
        #self.data['deadline'] = pd.to_datetime(self.data['deadline'], infer_datetime_format=True)

    def data_idea_test(self):
        # Works
        #data = json.load(open('./data/letters.json'))
        # print(type(data))
        # End works!!!

        #This will get the text in the series
        print(self.letters.loc["na_uk_16"])

    # Place is tied to to the places.csv that also has country in it
    # I may have to break each letter up by using the tokenization feature on
    #Text blob
    def get_sentiment_for_letters(self):
        # Getting the letters in the data set that are only in Engish
        data_set_english_only = self.index[(self.index.language == 'english')]
        years = [1914, 1915, 1916, 1917]
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        for year in years:
            #resetting the data set for each loop
            data_set_english_only_loop = data_set_english_only
            year_data_set = data_set_english_only_loop[(data_set_english_only_loop.year == year)]
            for month in months:
                #resetting the dataset for each loop
                year_data_set_loop = year_data_set
                month_data_set = year_data_set_loop[(year_data_set_loop.month == month)]
                print(month)
        # print(data_set_english_only['year'].min()) # 1914.0
        # print(data_set_english_only['year'].max()) # 1917.0

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

data = Data()
data.get_sentiment_for_letters()

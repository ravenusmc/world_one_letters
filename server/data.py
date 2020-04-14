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
        pass
        # Works
        #data = json.load(open('./data/letters.json'))
        # print(type(data))
        # End works!!!

        #This will get the text in the series
        #print(self.letters.loc["na_uk_16"])

    # Place is tied to to the places.csv that also has country in it
    # I may have to break each letter up by using the tokenization feature on
    #Text blob
    def get_sentiment_for_letters(self):
        sentiment_data = []
        columns = ['Date', 'Sentiment']
        sentiment_data.append(columns)
        # Getting the letters in the data set that are only in Engish
        data_set_english_only = self.index[(self.index.language == 'english')]
        years = [1914, 1915, 1916, 1917]
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        for year in years:
            rows = []
            #resetting the data set for each loop
            data_set_english_only_loop = data_set_english_only
            year_data_set = data_set_english_only_loop[(data_set_english_only_loop.year == year)]
            for month in months:
                #resetting the dataset for each loop
                year_data_set_loop = year_data_set
                #Looping through the loop based on the month.
                month_data_set = year_data_set_loop[(year_data_set_loop.month == month)]
                # if the dataset has data, during the month then we enter this
                #conditional statement
                if not month_data_set.empty:
                    count = 0
                    # This will pull the data from months that have more than one
                    # letter.
                    if len(month_data_set) > 1:
                        monthly_sentiment = []
                        while count < len(month_data_set):
                            # Getting the index of the letter
                            letter_index = month_data_set.iat[count,0]
                            # Getting the text of the letter based on the index
                            letter_text = self.letters.loc[letter_index]
                            text_ready_for_analysis = TextBlob(letter_text)
                            total = 0
                            average_counter = 0
                            for sentence in text_ready_for_analysis.sentences:
                                sentence_sentiment = sentence.sentiment[0]
                                monthly_sentiment.append(sentence_sentiment)
                            count += 1
                        average_sentiment = sum(monthly_sentiment)/len(monthly_sentiment)
                        average_sentiment_formatted = float(format(average_sentiment, '.5f'))
                    else:
                        # Getting the index of the letter
                        letter_index = month_data_set.iat[0,0]
                        # Getting the text of the letter based on the index
                        letter_text = self.letters.loc[letter_index]
                        text_ready_for_analysis = TextBlob(letter_text)
                        total = 0
                        average_counter = 0
                        for sentence in text_ready_for_analysis.sentences:
                            total = sentence.sentiment[0] + total
                            average_counter += 1
                        average_sentiment =  total / average_counter
                        average_sentiment_formatted = float(format(average_sentiment, '.5f'))
                    date = datetime.datetime(year, month, 1)
                    date_formatted = date.strftime("%b %Y")
                    rows.append(date_formatted)
                    rows.append(average_sentiment_formatted)
                    sentiment_data.append(rows)
                    print(sentiment_data)
        return sentiment_data

    #This method will get the data for the drill down.
    def get_data_for_drilldown(self, month_as_digit, year):
        drilldown_data = []
        columns = ['Letter Key', 'Author', 'Place']
        drilldown_data.append(columns)
        # Getting the letters in the data set that are only in Engish
        data_set_english_only = self.index[(self.index.language == 'english')]
        date_dataset = data_set_english_only[(data_set_english_only.year == year) & (data_set_english_only.month == month_as_digit)]
        if len(date_dataset) == 1:
            rows = []
            Letter_key = date_dataset['letter_key'].iloc[0]
            Author = date_dataset['author'].iloc[0]
            Place = date_dataset['place'].iloc[0]
            rows.append(Letter_key)
            rows.append(Author)
            rows.append(Place)
            drilldown_data.append(rows)
        else:
            count = 0
            while count < len(date_dataset):
                rows = []
                Letter_key = date_dataset.iat[count, 0]
                Author = date_dataset.iat[count, 1]
                Place = date_dataset.iat[count, 5]
                rows.append(Letter_key)
                rows.append(Author)
                rows.append(Place)
                drilldown_data.append(rows)
                count += 1
        return drilldown_data


# data = Data()
# data.get_sentiment_for_letters()

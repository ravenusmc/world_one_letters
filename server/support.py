# This class will deal with any support methods that I'll need in this course of this
# project.

class Support():

    def convert_stringDate_to_numberDate(self, date):
        convert_Date_Dictionary = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
             'May': 5,
             'Jun': 6,
             'Jul': 7,
             'Aug': 8,
             'Sep': 9,
             'Oct': 10,
             'Nov': 11,
             'Dec': 12
        }
        month_string = date.strip()[:3]
        integer_month = convert_Date_Dictionary[month_string]
        return integer_month

    def get_year(self, date):
        # print(date) # Nov 1915
        # print(date[4:8])
        return date[4:8]

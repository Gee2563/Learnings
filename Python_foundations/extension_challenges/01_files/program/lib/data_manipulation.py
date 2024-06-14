import os

def does_file_exist(filename):
    return os.path.isfile(filename)

def get_file_contents(filename):
    if does_file_exist(filename):
        data = open(filename, 'r')
        file_content = data.readlines()
        return file_content

    else:
        return 'This file cannot be found!'
#     if does_file_exist(filename):
#         data = []
#         with open(filename, 'r') as file:
#             csvReader = csv.reader(file, delimiter=',')
#             for row in csvReader:
#                 data.append(row)
#         print(data[0])
# #         return data
    
#     else:
#         return 'This file cannot be found!'

def christmas_day_air_quality(filename, include_header_row):
    readeable = get_file_contents(filename)
    xmas_array = list(filter(lambda x : x[:5] == '25/12', readeable))
    if include_header_row == True:
        xmas_array.insert(0, readeable[0])
    return xmas_array


def array_of_air(data):
    return [int(air_quality[3]) for air_quality in [line.split(';') for line in data]]

def christmas_day_average_air_quality(filename):
    data = christmas_day_air_quality(filename, include_header_row=False)
    return round(sum(array_of_air(data)) / len(array_of_air(data)),2)    

# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged togethe

def get_averages_for_month(filename):
    readeable = get_file_contents(filename)
    air_calendar = {}
    # go from 1 -> 12, air_calendar[1] = []
    for i in range(1,13):
        array_month = list(filter(lambda x : x[3:5] == f'{i:02d}', readeable))
        air_calendar[i] = round(sum(array_of_air(array_month))/ len(array_month),2)
    return air_calendar
    


# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"
def create_march_data(filename):
    with open('AirQualityMarch.csv', 'w') as newFile:
        readeable = get_file_contents(filename)
        march_data = list(filter(lambda x: x[3:5] == '03', readeable))
        #insert header
        march_data.insert(0,readeable[0])
        
        newFile.write(('').join([line for line in march_data]))

    print(march_data[0])

# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    os.mkdir('monthly_responses')
    readeable = get_file_contents(filename)
    data_by_monthYear = {}
    for line in readeable:
        monthYear = f'{line[3:5]}-{line[6:10]}'
        if monthYear not in data_by_monthYear:
            data_by_monthYear[monthYear] = [readeable[0], line]
        else:
            data_by_monthYear[monthYear].append(line)
    
    for key in data_by_monthYear:
        if key[0].isdigit():
            with open(f'./monthly_responses/{key}.csv', 'a') as newFile:
                newFile.writelines(data_by_monthYear[key])
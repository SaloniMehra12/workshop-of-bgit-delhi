#reading csv file
import csv

with open('people.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
        
"""In above program,

->First, we open our CSV file as csvFile. or we can use any name instead of csvFile as per our choice
->Then, we used the csv.reader() method to extract the data into the   reader object which we can iterate over to get each line of our     data.

"""
import csv

csvData = [['Name of Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
    
# to see changes run person.csv

#since we have not made person.csv file previously it will make it a 
#file named person and add the given entries in it
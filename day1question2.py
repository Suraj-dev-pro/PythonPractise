"""Write a program that reads a csv  and converts into json"""
import csv
import json

# Open the CSV file
with open('exampledata.csv', 'r') as csv_file:
    # Create a CSV reader object
    reader = csv.reader(csv_file)
    
    # Get the field names from the first row of the CSV
    field_names = next(reader)
    
    # Create an empty list to store the data
    data = []
    
    # Iterate over the rows of the file
    for row in reader:
        # Zip together the field names and row values
        items = zip(field_names, row)
        
        # Create a dictionary for the current row
        item_dict = {}
        for field_name, value in items:
            item_dict[field_name] = value
        
        # Add the dictionary to the data list
        data.append(item_dict)
    
    # Convert the data list into a JSON object
    json_data = json.dumps(data)
    
    # Print the JSON object
    print(json_data)


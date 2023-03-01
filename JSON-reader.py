# Python program to read JSON files
 
import json
print("Usage: Give name of the JSON file in the script!")
# Opening JSON file
f = open('filename.json')
  
# returns JSON object as a dictionary
data = json.load(f)
  
# Iterating through the json list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()

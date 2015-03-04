# ###### TAKE-HOME ASSESSMENT 2 ######
# ###### by: saa419 ######
# ###### Practical Data Science ######

# The following imports json and matplotlib.
import json
import matplotlib.pyplot as plt

# Open the json file and read it.
ad_filename = "ad.json"
ad_file = open(ad_filename, 'r')
# Create a list where all html elements will be placed
all_htmlelements = []

# Iterate through the json file. For each line, append it into the all_htmlelements list.
# The result is a list of dictionaries, where each line in the json file is a dictionary item in list all_customers
for line in ad_file:
    new_element = json.loads(line)
    all_htmlelements.append(new_element)
ad_file.close()

# ##### QUESTION 1 #####

# The following reads the length of the list, i.e. how many total lines are in the json file
print "We have %d html entries in the json file." % len(all_htmlelements)

 ##### DEBUGGING CODE #####
# Print the first item in the all_htmlelements list, just to see what it looks like.
# print "First entry in the all_htmlelements list: %s" % all_htmlelements[0]

# Re-open the customer file.
ad_file = open(ad_filename, 'r')
# Create two lists: one with all the ? lines, and one with the rest.
question = []
validelements = []

for line in ad_file: # for each line in the JSON file,
	templine = json.loads(line) # Read each line separately, name them templine
	for item in templine: # For each tuple (i.e., attribute) in each line in the JSON file,
		if item == "?": # If any of the values = "?"
			question.append(templine) # Add it to question list.
			break # And don't continue checking the values in that line! If the script were to continue, it would duplicate any entries that have multiple ? values.

print "Question 1: We have %d element entries that have a value of ?." % len(question)

# ##### QUESTION 2 #####

# Now, to generate the list of valid elements, go through the all_htmlelements list and add it to valid elements if they're not in the list of ? entries.
# Source: http://stackoverflow.com/a/3462202
validelements = [x for x in all_htmlelements if x not in question]

# The following reads the length of the list, i.e. how many total lines are in the file with valid elements.
print "Question 2: We have %d html element entries that are valid and don't have any ? values." % len(validelements)

# ##### DEBUGGING CODE #####
# Print the list of ? entries, to see what they look like.
# print "question marks!"
# print question[0:2]
# print the first 2 entries for valid elements, to see what they look like.
# print "elements!"
# print validelements[0:2]

# ##### QUESTION 3 #####

# Create a list to re-do the questions to parse for processing.
question2 = []

# This didn't work
'''
['1' if x=='ad.' else '0' for x in validelements2]

print ("test")
print validelements2[0:1]

'''

# This worked!
for line in ad_file: # for each line in the JSON file,
	templine = json.loads(line) # Read each line separately, name them templine
	for item in templine: # For each tuple (i.e., attribute) in each line in the JSON file,
		if item == "?": # If any of the values = "?"
			question2.append(templine) # Add it to question.
			break # And don't continue checking the values in that line! If the script were to continue, it would duplicate any entries that have multiple ? values.
			
# Parse for processing. First, copy the list to a new one we will modify.
validelements2 = validelements

for item in validelements2: # For each item in the list,
    for n,i in enumerate(item): # For each element i, make the following replacements.
            if i=='ad.':
                    item[n]=1
            if i=='nonad.':
                    item[n]=0
            if i=='1':
                    item[n]=1
            if i=='0':
                    item[n]=0
# print validelements2[0:1]

# Finally, go through and make the beginning numbers floats.
ve3 = [[int(float(j)) for j in i] for i in validelements2]

print "Question 3: Data has been prepared for prediction, transforming the ad / nonad label to a 1 / 0 numeric value, and change the string values in the json array to floats."
print "Here is a sample of the data after prediction preparation:"

print ve3[0:1]
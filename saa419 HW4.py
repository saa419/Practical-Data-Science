# ###### Homework 4 ######
# ###### by: saa419 ######
# ###### Practical Data Science ######

import re

# First, open the file and read the entire contents.
f = open('pds_2012_roster.html', 'r')
# Call it html, for simplicity's sake.
html = f.read()

# ##### QUESTION 1 #####

# First, create a list to hold the netids
netids = []
# The following was to debug, to see how to best split the html file.
# print html.split("</TR>")

# Split the html file on the Table elements. For each entry,
for entry in html.split("<TR>"):
# Use regex to search for the netids in each split element (entry). Search for 2 or 3 letters followed by 3 or 4 numbers.
	result = re.search("([a-z]{2,3}\d{3,4})", entry)
	if result: # If we get a result,
		print result.group(1) # Print the result on screen,
		netids.append(result.group(1)) # And append it to the netids list

# Next, print the netids to a file. Open/create regexq1output.txt and write to it.
file = open("regexq1output.txt", "w")
# For each item in the netids list,
for item in netids:
#	write it to the text file, with a new line after each element.
	file.write("%s\n" % item)
file.close()
#print the length of the netids list, to check that we have the right number of students.
print "%d netids found." % len(netids)

# ##### QUESTION 2 #####

# Create a list to hold the last names.
lnames = []

# Split the html file on the Table elements. For each entry,
for entry in html.split("<TR>"):
# Use regex to search for the last names in each split element (entry). Search for words that come after the "SCIENCE'>" element in the html (as part of a link that immediately precedes the last names), and match the ones that start with one capital letter followed by 1, 2, or 3 lowercase letters, followed by a comma. This matches the last name.
   result = re.search("[SCIENCE\'\>]([A-Z]{1}[a-z]{1,3})[\,]", entry)
   if result: # If we get a result,
		print result.group(1) # Print the result on screen,
		lnames.append(result.group(1)) # And append it to the lnames list

print "%d last names with 4 or fewer letters." % len(lnames)

print "%d students (with 5 or more letters in their last name) were removed." % (len(netids)-len(lnames))

# ##### QUESTION 3 #####

# Split the html file on the Table elements. For each entry,
for entry in html.split("<TR>"):
# Use regex to search within each row for last names (captured as group 1), first and middle names (captured as group 2), and netids (captured as group 3). The .*[\n] in between searches for anything that's in the middle plus newlines.
	result = re.search("[SCIENCE\'\>]([A-Z]{1}[a-z].*)[\,]\s(.*)</a>.*[\n].*[\n].*[\n].*([a-z]{2,3}\d{3,4})", entry)
	if result: # If we get a result,
		print "%s\t%s\t%s" % (result.group(2),result.group(1),result.group(3)) # Print the result on the screen.

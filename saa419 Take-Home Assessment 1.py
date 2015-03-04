# ###### TAKE-HOME ASSESSMENT ######
# ###### by: saa419 ######
# ###### Practical Data Science ######

# enable the matplotlib inline code if running in ipython
# %matplotlib inline

# The following imports json and matplotlib.
import json
import matplotlib.pyplot as plt

# Open the json file and read it. I am recycling some of this from my homework 3.
customer_filename = "assess1_data.json"
customer_file = open(customer_filename, 'r')
# Create a list where all customer entries will be placed
all_customers = []

# Iterate through the json file. For each line, append it into the all_customers list.
# The result is a list of dictionaries, where each line in the json file is a dictionary item in list all_customers
for line in customer_file:
    new_customer = json.loads(line)
    all_customers.append(new_customer)
customer_file.close()

# ##### QUESTION A #####

# For the first part of question A, please see accompanying pdf document.
# The following reads the length of the list, i.e. how many total lines are in the json file
print "For the first part of question A, please see accompanying pdf document."
print "Question A: We have %d customer entries in the json file." % len(all_customers)

# ##### DEBUGGING CODE #####
## Print the first item in the all_activities list, just to see what it looks like.
# print "First entry in the all_customers list: %s" % all_customers[0]

# ##### QUESTION B #####

# The following allows me to see how many unique users there are. 
# Create a new list for just the name values in the data.
users = []

# Iterate through the data and extract the names.
for p in all_customers:
    users.append(p['NAME'])
# print len(set(p['NAME'] for p in all_customers))

print "The following is sort of part of question B:"
print "There are %d unique users in the data." % len(set(users))
print "There are %d total user entries in the data, which (by simple math) tells us that there is one duplicated name. Let's find it!" % len(users)

# ##### DEBUGGING CODE #####
## The following was to print out entries in the lists to check my progress.
## Now let's print the first and last user ID. This was a personal choice, to make sure that they matched the ones in all_activities.
#print "The first user is: %s" % users[0]
#print "The last user is: %s" % users[35274]
#print "Let's print the first entry in all_customers list: %s" % all_customers[0]
#print "Let's print the last entry in all_customers list: %s" % all_customers[-1]

# Question B, continued.

# To find the duplicated name(s), let's create a dictionary of total counts for each user. Then we'll see how many are greater than 1.
usertotalcount = {}

# Fill the dictionary of total counts for each user.
for item in all_customers: # For each item in the list all_customers,
	if item['NAME'] in usertotalcount: # Take the values under key "NAME" (i.e., the person's name). If that value is in usertotalcount,
		usertotalcount[item['NAME']] = 1 + usertotalcount[item['NAME']] # Increase that value in usertotalcount. i.e., keep a count
	else: # Or else, set it to one, because it's starting the count if there isn't one there already.
		usertotalcount[item['NAME']] = 1

# Next, let's create a list for user duplicates.
userdups = []

# Source for getting values from dictionary: http://www.dotnetperls.com/dictionary-python
# Here, we read the keys and values from the usertotalcount dictionary.
for k,v in usertotalcount.items():
	line = k,v # Call each tuple in the dictionary a line.
	if v > 1: # If the name count is greater than 1,
		userdups.append(line) # Add the person's name and the number of times their name appears to userdups.

print "Question B: The following is the full list of duplicated names, along with how many times they appear."
print userdups

# ##### QUESTION C #####

# Re-open the customer file.
customer_file = open(customer_filename, 'r')
# Create two lists: one with all the -9999 lines, and one with the rest.
negninecustomers = []
validcustomers = []

for line in customer_file: # for each line in the JSON file,
	templine = json.loads(line) # Read each line separately, name them templine
	for k,v in templine.items(): # For each tuple (i.e., attribute) in each line in the JSON file,
		if v == -9999 or v == "-9999": # If any of the values = -9999 (string or number),
			negninecustomers.append(templine) # Add it to negninecustomers.
			break # And don't continue checking the values in that line! If the script were to continue, it would duplicate any entries that have multiple -9999 values.

# Now, to generate the list of valid customers, go through the all_customers list and add it to validcustomers if they're not in the list of -9999 entries.
# Source: http://stackoverflow.com/a/3462202
validcustomers = [x for x in all_customers if x not in negninecustomers]

# The following reads the length of the lists, i.e. how many total lines are in the json file
print "Question C: We have %d customer entries that have a value of -9999." % len(negninecustomers)
print "We have %d customer entries that are valid and don't have any -9999 values." % len(validcustomers)

# ##### DEBUGGING CODE #####
## Print the list of -9999 entries, to see what they look like.
# print negninecustomers
## print the first 5 entries for valid customers, to see what they look like.
# print validcustomers[0:5]

# ##### QUESTION D #####

## First, create 3 lists to house all of the rfa2f, rfa2a, and wealth values.
rfa2f = []
rfa2a = []
wealth = []

# Iterate through the validcustomers file, and place each value in their appropriate list.
for line in validcustomers:
	rfa2f.append(line['RFA_2F'])
	rfa2a.append(line['RFA_2A'])
	wealth.append(line['WEALTH_INDEX'])

# To find the values that each field takes, make the lists into sets.
# The following commented-out print statements give me the length of the sets; i.e., how many unique values each takes. This was to see if printing them was manageable.
# print "The length of 'rfa2f' *set* is: %d" % len(set(rfa2f))
print "Question D: RFA_2F takes the following values: %s" % set(rfa2f)
# print "The length of 'rfa2a' *set* is: %d" % len(set(rfa2a))
print "RFA_2a takes the following values: %s" % set(rfa2a)

print "WEALTH_INDEX takes %d different values. This is too much! I'll give you a range instead, and if you really want to see each and every value, go into the code and uncomment the line that will do that." % len(set(wealth))
print "The values in 'WEALTH_INDEX' range from: %.2f to %.2f" % (min(wealth), max(wealth))
## The following prints all of the WEALTH_INDEX values:
# print "WEALTH_INDEX takes the following values: %s" % set(wealth)

# Now, to calculate the frequency of each value for RFA_2F and RFA_2A:
# First, let's create a dictionary of total counts for each rfa field.
rfa2fcount = {}
rfa2acount = {}

# Fill the dictionary of total counts for each rfa field.
for item in validcustomers: # For each item in the list of valid customers,
	if item['RFA_2F'] in rfa2fcount: # Take the RFA-2F values. If that value is in rfa2fcount,
		rfa2fcount[item['RFA_2F']] = 1 + rfa2fcount[item['RFA_2F']] # Increase that value in rfa2fcount count. i.e., keep a count
	else: # Or else, set it to one, because it's starting the count if there isn't one there already.
		rfa2fcount[item['RFA_2F']] = 1
	if item['RFA_2A'] in rfa2acount: # Take the RFA-2A values. If that value is in rfa2acount,
			rfa2acount[item['RFA_2A']] = 1 + rfa2acount[item['RFA_2A']] # Increase that value in rfa2acount count. i.e., keep a count
	else: # Or else, set it to one, because it's starting the count if there isn't one there already.
			rfa2acount[item['RFA_2A']] = 1

print "Frequency of each value in RFA_2F:"
print rfa2fcount
# rfa2acount = [s.encode('utf-8') for s in rfa2acount] # get rid of Unicode
print "Frequency of each value in RFA_2A:"
print rfa2acount

# ##### QUESTION E #####

# Let's start a count of how many people responded.
respondedcount = 0

# Next, let's go through the list of valid customer entries, and increase the count if they responded.
for line in validcustomers: # For each line in validcustomers,
	if line['TARGET_B'] == 1: # If the customer responded,
		respondedcount = 1 + respondedcount # Increase the count.

print "Question E: Total number of responses: %d" % respondedcount

# Now, let's calculate the proportion.
# First, get the number of total customer entries.
validcustcount = len(validcustomers)
print "We have %d customer entries in the valid file, so..." % validcustcount

# Calculate the percentage of users who responded. Use float so we get decimals!
respondpercent = (float(respondedcount)/validcustcount)*100

print "Proportion of users who responded: %.2f percent" % respondpercent

# ##### QUESTION F #####

# For this question, let's calculate the total count and the average wealth index of the responders versus the non-responders.
# Create a list for the wealth indices of each group.
responderswealth = []
nonrespondwealth = []

# Next, let's populate those lists.
for line in validcustomers: # For each line in the validcustomers file,
	if line['TARGET_B'] == 1: # If the customer responded,
		responderswealth.append(line['WEALTH_INDEX']) # Add their wealth index to the responderswealth file
	else:
		nonrespondwealth.append(line['WEALTH_INDEX']) # Or else if they didn't respond, add their wealth index to the nonrespondwealth file.
print "Question F: We have %d responders and %d nonresponders." % (len(responderswealth),len(nonrespondwealth))

# Next, let's calculate the averages.
# Seems simple, but here's my source for how to find the average: http://stackoverflow.com/a/9039992 . I searched in order to find out if there was an avg() function.
# I used float because previously I printed the values directly, and that's what made it work then.
#print (sum(responderswealth)/float(len(responderswealth)))
#print (sum(nonrespondwealth)/float(len(nonrespondwealth)))
# Declare variables instead so I can put them in statements.
respondavg = (sum(responderswealth)/float(len(responderswealth)))
nonrespondavg = (sum(nonrespondwealth)/float(len(nonrespondwealth)))

print "The average wealth index of responders is: %f" % respondavg
print "The average wealth index of non-responders is: %f" % nonrespondavg

## The following code gives us the min and max of responders vs. non-responders wealth index. It didn't yield any useful information, so I threw it out.
#print min(responderswealth)
#print max(responderswealth)
#print min(nonrespondwealth)
#print max(nonrespondwealth)

# ##### QUESTION G #####

# Source for info on plotting histograms with matplotlib: http://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/
plt.hist(responderswealth, bins=100, normed=True, histtype='stepfilled', color='b', alpha=0.6, label='Responders')
plt.hist(nonrespondwealth, bins=100, normed=True, histtype='stepfilled', color='r', alpha=0.5, label='Non-Responders')
plt.title("Wealth Index of Responders vs. Non-Responders")
plt.xlabel("Wealth Index")
plt.ylabel("Distribution")
plt.legend()
plt.show()

# ##### QUESTION H #####

# Alphabetizing the customers by last name. First, create a new list of the data that we can sort.
sortvalidcust = validcustomers

# Sort by NAME field.
# Source for sorting: http://stackoverflow.com/questions/14077851/python-list-of-dictionaries-sort-multiple-keys
sortvalidcust.sort(key=lambda x: (x['NAME']))
print "Question H: Alphabetized records 1-10 by first name!"
print sortvalidcust[0:10] # Start at index 0, and go up to but not including index 10. This gives us the top 10.
print "Alphabetized records 20,000-20,010 by first name!"
print sortvalidcust[19999:20010] # Start at index 19,999, which gives us the 20,000th entry. Go up to index 20,000 but not including it, which is entry # 20,011.

# ##### QUESTION I #####

# Create a list to house all of the customer data with an additional field holding the last name,
validwithlast = []

for line in validcustomers: # For each line in the validcustomers file (i.e., for each dictionary),
	templist = line.items() # Make a temporary list of each line instead of a dictionary. We'll append the last name to this in its own field so we can sort by it.
	tempname = line['NAME'] # House the full name in a temporary list.
	splitlist = tempname.split() # Create a list of all the parts of the name.
# Here's where the magic happens! I'm pretty proud of this solution.
	if len(splitlist) == 2: # If the split list of name parts is exactly 2 words long (i.e., no middle initial or Jr./Sr./III),
		lastname = splitlist[1] # the last name is the last word.
	elif len(splitlist) == 4: # If the split list of name parts is exactly 4 words long (it has a middle initial and a suffix),
		lastname = splitlist[2] # the last name is the second to last word.
	elif splitlist[2] == "III" or splitlist[2] == "Jr." or splitlist[2] == "Sr.": # Or else, if the split list of name parts is 3 words long, it either has a suffix or a middle initial, but not both. This checks if it has a suffix as the last word. If it does,
		lastname = splitlist[1] # the last name is the 2nd word.
	else: # Or else it has a middle name, and hence
		lastname = splitlist[2] # The last name is the last word.
	lastentry = 'LASTNAME',lastname # Create what's going to be the entry that goes back in the customer file
	templist.append(lastentry) # Append this last entry to the temporary list of each line in the customer file,
	tempdict = dict(templist) # Change it back to a dictionary,
	validwithlast.append(tempdict) # And put it into the validwithlast list.

## I used the following print statement to read some items in the list to make sure they had a last name field with the proper last name
# print validwithlast[0:10]

# Now, the actual alphabetizing of the customers by first name. First, create a new list of the data that we can sort.
sortvalidlast = validwithlast

# Sort by our shiny new last name field.
# Source for sorting: http://stackoverflow.com/questions/14077851/python-list-of-dictionaries-sort-multiple-keys
# For this one, I'm sorting first by last name, then by first name (which uses the middle initial as a tiebreaker), just in case. Though when I was coding it, it seemed to do that by default. Not sure why.
sortvalidlast.sort(key=lambda x: (x['LASTNAME'], x['NAME']))

print "Alphabetized records 1-10 by last name!"
print sortvalidlast[0:10] # Start at index 0, and go up to but not including index 10. This gives us the top 10.
print "Alphabetized records 20,000-20,010 by last name!"
print sortvalidlast[19999:20010] # Start at index 19,999, which gives us the 20,000th entry. Go up to index 20,000 but not including it, which is entry # 20,011.

# ##### QUESTION J #####

# Create a list to house all the data with the predicted response.
predictedresponse = []

for line in validcustomers: # For each line in validcustomers list,
	templist = line.items() # Place each line in a temporary list that we're going to append the predicted value to.
	wlthvalue = line['WEALTH_INDEX'] # Read the wealth_index value into a variable for calculation.
	rfa2fvalue = line['RFA_2F'] # Read the rfa_2f value into a variable for calculation.
	respvalue = -40 + 0.8*wlthvalue + 0.12*rfa2fvalue # calculate the predicted response based on the formula.
	lastentry = 'PREDICTED_RESPONSE',respvalue # Create an entry consisting of the key and the value to be placed into the dictionary
	templist.append(lastentry) # Append it to the list that holds the current line
	tempdict = dict(templist) # Change it back to a dictionary
	predictedresponse.append(tempdict) # And append it to predictedresponse.

# Now, the sorting. First, create a new list of the data that we can sort.
sortpredictedresponse = predictedresponse

# Sort by the predicted response field. Reverse sort to show us the top entries, the ones more likely to respond.
# Source for sorting: http://stackoverflow.com/questions/14077851/python-list-of-dictionaries-sort-multiple-keys
sortpredictedresponse.sort(key=lambda x: (x['PREDICTED_RESPONSE']), reverse=True)

print "Top 10 customer records in predictive response model:"
print sortpredictedresponse[0:10]
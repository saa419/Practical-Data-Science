/*
Analytics with SQL
Homework 4
*/

/*
1. How many shops are there?
46426
*/
	SELECT COUNT(shop_id) from shops; -- This counts the number of shop_id entries in the shops table, but doesn't show if there are any duplicates
	SELECT COUNT(DISTINCT(shop_id)) from shops; -- This counts the unique instances of shop_id in the shops table. It gives us the same result as above, which means that there aren't any duplicates.
	select count(*) from shops; -- This counts all the lines in the shops table. Same number as above.

/*
2. What is the average price over all listings? What is the average “price” across all transactions?
Average price over all listings: $35.22
*/
	SELECT AVG(price) from listings;
/*
Average price over all transactions: $20.76
*/
	SELECT AVG(price) from transactions;

/*
3. What is the average individual price of each listing purchased (note that the price field in the transactions table is the total price for the transaction; you need to control for quantity). How does this compare to the average listing price?
Average individual price of each listing purchased: $20.45
*/
	SELECT AVG(price/quantity) from transactions;
/*
Average listing price: $32.82
*/
	SELECT AVG(price/quantity) from listings;

/*
4. Remove listings with a price or quantity of 0 and recompute the average price. How does this compare to the average price of each listing purchased?
Average listing price with 0 removed: $34.45
*/
	SELECT AVG(price/quantity) from listings WHERE price > 0 AND quantity > 0;
/*
Average transaction price with 0 removed: $20.51
*/
	SELECT AVG(price/quantity) from transactions WHERE price > 0 AND quantity > 0;

/*
5. What are the 5 most expensive listings?
listing_id	price
929296	25000000
149300	2000000
92558	1100000
685622	950000
699939	949999
*/
	SELECT listing_id,price from listings WHERE price > 0 AND quantity > 0 ORDER BY (price/quantity) DESC LIMIT 10;

/*
6. How many listings has each user purchased? (Explain your interpretation(s))
Each user has purchased an average of 1.11 listings.
*/
	SELECT AVG(listings_bought) FROM (SELECT buyer_user_id as `user_id`, COUNT(DISTINCT(listing_id)) as listings_bought FROM transactions GROUP BY user_id) listpurch;
In my SQL query, I compute the average number of listings bought. In order to do that, I make a listpurch table which groups purchases by listing ID and counts how many purchases each user has, then take the average of that number of purchase column.

/*
Optional:
7. Compute the distribution of how many users purchase different numbers of listings (# listings purchased vs. # users with that many purchases). You can ignore users with 0 purchases.   (Could you plot this? Hint: click export)
listings_bought	no_of_users
1	78378
2	6422
3	849
4	181
5	52
6	29
7	17
8	9
9	4
10	2
11	3
13	1
You can plot this, yes, by exporting as a csv.
*/
	SELECT as1.listings_bought, COUNT(as1.listings_bought) as no_of_users FROM (SELECT buyer_user_id as `user_id`, COUNT(DISTINCT(listing_id)) as `listings_bought` FROM transactions GROUP BY user_id) as1 GROUP BY as1.listings_bought; -- This one shows the count for # listings purchased vs. # users with that many purchases

/*
8. Compute the number of users with each gender.
Male: 6,863
Female: 36,052
Private: 52,228
*/
	SELECT COUNT(`user_id`) FROM users WHERE `gender` = 'male';
	SELECT COUNT(`user_id`) FROM users WHERE `gender` = 'female';
	SELECT COUNT(`user_id`) FROM users WHERE `gender` = 'private';

/*
9. Among the users with purchases, compute the number of users with each gender.
Male: 681
Female: 3,676
Private: 5,222
Both INNER JOIN and LEFT OUTER JOIN give the same answer.
*/
	SELECT COUNT(user_id) FROM transactions INNER JOIN users ON transactions.buyer_user_id = users.user_id WHERE `gender` = 'male';
	SELECT COUNT(user_id) FROM transactions INNER JOIN users ON transactions.buyer_user_id = users.user_id WHERE `gender` = 'female';
	SELECT COUNT(user_id) FROM transactions INNER JOIN users ON transactions.buyer_user_id = users.user_id WHERE `gender` = 'private';
	SELECT COUNT(user_id) FROM transactions LEFT OUTER JOIN users ON transactions.buyer_user_id = users.user_id WHERE `gender` = 'male';
	SELECT COUNT(user_id) FROM transactions LEFT OUTER JOIN users ON transactions.buyer_user_id = users.user_id WHERE `gender` = 'female';
	SELECT COUNT(user_id) FROM transactions LEFT OUTER JOIN users ON transactions.buyer_user_id = users.user_id WHERE `gender` = 'private';

/*
Dealing with Data: Parsing Text and Extracting Information
1. Within the document, there are several student IDs (the column actually is titled E-mail). Extract these IDs from the html and print them to a file, one per line.
44 netids found.
(See attached .py file)

2. Constrain your search to print only those students with four letters in their last names or less. How many students were removed?
31 students (with 5 or more letters in their last name) were removed. 13 remain.
(See attached .py file)

3. For every student in the class, in addition to extracting their student ID, extract their name. Present the results by printing out, one student per line:
                first (and middle) name [tab] last name [tab] student id
(See attached .py file for output)
*/
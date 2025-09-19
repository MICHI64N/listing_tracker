# Listing Tracker
***Monitor E-Commerce Webpages/Listings***
> Note: This tracker is *very* early in development!

## Features and Usage
For any additional information not stated here, look inside the [`/docs/`](/docs/) directory.
### Add Listings to the Database
Add listings to the database (in the `inserted_webpages` table) using the command [`listing_tracker add webpage`](/docs/commands.md#add).
- The first input asks to type or paste the URL to continue.
- The second input asks to confirm the added URL is correct. Any input that starts with a "y" in either (upper/lower) case is accepted as "yes." This includes but is not limited to "y," "Ye," "yeAh," or even "your mama."
- The script then fills in the rest of the columns:
    - it computes the website value by rotating through a list of domains and
    - it fetches the current datetime to the second in UTC and adapts it into ISO format.
- These values are then inserted into the database, after which the success notification is printed:
    - the website is in the statement if a value was found during the rotation while
    - the url is printed instead if no value was found.
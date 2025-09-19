# listings.py Documentation
**Location**: [/listing_tracker/database/listings.py](/listing_tracker/database/listings.py)

Outside of the file's functions, the file looks for the listings table and creates the table if it does not yet exist. It uses the [Table and Column classes](/docs/database/classes.md) to aid in this.

## Functions
* **website_identifier(*url*)** - Compares the URL with the pre-defined website list created in [websites.py](/docs/database.md#websitespy), returning the match if found and returns a null string if not.
* **datetime_adapter(*datetime*)** - Standardizes datetime inputs to the ISO format.
* **insert_webpages(*table, url*)** - Inserts the URL, the website from website_identifier, and the adapted datetime to the database in the listings table.
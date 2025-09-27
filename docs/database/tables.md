# Listing Tracker Database Tables
This is every table included in the packages database (database.sqlite):

## listings
**Location**: [/listing_tracker/database/listings.py](/listing_tracker/database/listings.py)

### Columns
* **link (*text*)** - Stores listing URL's
* **website (*text*)** - The website as listed on the [websites table](#websites) if found; null if not found
* **datetime_added (*blob*)** - The date and time the row was created

## websites
**Location**: [/listing_tracker/database/websites.py](/listing_tracker/database/websites.py)

The websites table is automatically populated by its script, see the [file docs](/docs/database.md#websitespy) for the website list.

### Columns
* **name (*text*)** - The name of the website
* **domain (*text*)** - The domain name (part of URL) of the website
# Database Directory Documentation
**Location**: [/listing_tracker/database/](/listing_tracker/database/)

The database directory contains the files to operate the database (excluding user executions through [\_\_main\_\_.py](/docs/toplevel.md#__main__py)). The following are documented within this file:
* [\_\_init\_\_.py](#__init__py)
* [connection.py](#connectionpy)
* [database.sqlite](#databasesqlite)
* [websites.py](#websitespy)

## \_\_init\_\_.py
**Location**: [/listing_tracker/database/\_\_init\_\_.py](/listing_tracker/database/__init__.py)

This init file imports the other files in the directory to itself for [\_\_main\_\_.py](/docs/toplevel.md#__main__py) to access.

## connection.py
**Location**: [/listing_tracker/database/connection.py](/listing_tracker/database/connection.py)

This file uses the root directory from [dir.py](/docs/toplevel.md#dirpy) and the database name to connect to the database. It is used as an import to execute any request.

## database.sqlite
**Location**: [/listing_tracker/database/database.sqlite](/listing_tracker/database/database.sqlite)

This file is the SQLite database itself. It doesn't exist until the user calls a database command for the first time.

## websites.py
**Location**: [/listing_tracker/database/websites.py](/listing_tracker/database/websites.py)

Creates a table with a pre-defined website list used in [listings.py](/docs/database/listings.md).

### Website List
* \[COM\] Amazon - www.amazon.com
* \[JP] Amazon - www.amazon.co.jp
* eBay - www.ebay.com
* Lashinbang - shop.lashinbang.com
* Mandarake - www.mandarake.co.jp
* \[COM\] Mercari - www.mercari.com
* \[JP\] Mercari - jp.mercari.com; mercari.jp
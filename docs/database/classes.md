# classes.py Documentation
**Location**: [/listing_tracker/database/classes.py](/listing_tracker/database/classes.py)

This file stores the classes used in the program: [Column](#class-column) and [Table](#class-table). As a tool of object oriented programming, the classes are reflective of columns and tables used in real-world databases (such as [database.sqlite](/docs/database.md#databasesqlite)).

## Class Column
### \_\_init\_\_ Properties 
* name (string) - The name of the column
* type (string) - The datatype the column accepts
* null (boolean) - If the column accepts null values
* default_val (string) - The default column value if another is not specified

### Methods
This class contains no methods; it is meant to be used by [Class Table](#class-table)

## Class Table
### \_\_init\_\_ Properties 
* **name *(string)*** - The name of the table
* **columns *(list)*** - Always starts out as an empty list; the column_assign method adds columns to the list.

### Methods
* **column_assign(*columns*)** - Add one or more instances of [Class Column](#class-column) to the table's columns list.
* **get_dict()** - Create a Python dict of the table and its columns's attributes.
* **exists(*dict*)** - Finds if the table exists in the database with the created python dict and returns true or false.
* **create(*dict*)** - Create the table in the database with the created python dict.
* **insert(*values*)** - Insert a row of information into the database.
* **insert_many(*values_list*)** - Insert many rows of information into the database.
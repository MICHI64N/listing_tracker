# Listing Tracker Classes
This is every class in the listing_tracker package; they improve efficiency and keep code neat:
* [Column](#class-column)
* [Command](#class-command)
    * [Database](#class-databasecommand)
        * [Add](#class-adddatabase)
        * [View](#class-viewdatabase)
* [Table](#class-table)

## Class Add([Database](#class-databasecommand))
**Location**: [/listing_tracker/commands.py](/listing_tracker/commands.py)

### Parents
* [Database(Command)](#class-databasecommand)

### \_\_init\_\_ Properties
* **args (*list*)** - [**Inherited from Parent**] The command's arguments
* **arg_amount (*int*)** - [**Inherited from Parent**] The amount of arguments provided in the command
* **table (*string*)** - [**Inherited from Parent**] The first argument of the database command
* **urls (*list*)** - A list of urls to add to the database

### Methods
* **arg_amount_valid(*expected_arg_amount, fixed_amount*)** - [**Inherited from Parent**] Validates if the correct amount of arguments were provided in the command
* **table_valid()** - [**Inherited from Parent**] Validates if the table is usable for the command
* **valid(*expected_arg_amount, fixed_amount*)** - [**Inherited from Parent**] Executes both arg_amount_valid() and table_valid() methods to fully test the command's validity
* **exec_actions(*\*table_actions*)** - [**Inherited from Parent**] Match the command's table and execute the according table action
* **exec()** - Execute self_valid() and exec_actions() to add the urls to the associated table

## Class Column
**Location**: [/listing_tracker/database/tables.py](/listing_tracker/database/tables.py)

### \_\_init\_\_ Properties 
* **name (*string*)** - The name of the column
* **type (*string*)** - The datatype the column accepts
* **null (*boolean*)** - If the column accepts null values
* **default (*string*)** - The default column value if another is not specified

### Methods
This class contains no methods; it is meant to be used by [Class Table](#class-table)

## Class Command
**Location**: [/listing_tracker/commands.py](/listing_tracker/commands.py)

### Children
* [Database(Command)](#class-databasecommand)

### \_\_init\_\_ Properties
* **args (*list*)** - The command's arguments
* **arg_amount (*int*)** - The amount of arguments provided in the command

### Methods
* **arg_amount_valid(*expected_arg_amount, fixed_amount*)** - Validates if the correct amount of arguments were provided in the command

## Class Database([Command](#class-command))
**Location**: [/listing_tracker/commands.py](/listing_tracker/commands.py)

### Parents
* [Command](#class-command)

### Children
* [Add(Database)]()
* [View(Database)]()

### \_\_init\_\_ Properties
* **args (*list*)** - [**Inherited from Parent**] The command's arguments
* **arg_amount (*int*)** - [**Inherited from Parent**] The amount of arguments provided in the command
* **table (*string*)** - The first argument of the database command

### Methods
* **arg_amount_valid(*expected_arg_amount, fixed_amount*)** - [**Inherited from Parent**] Validates if the correct amount of arguments were provided in the command
* **table_valid()** - Validates if the table is usable for the command
* **valid(*expected_arg_amount, fixed_amount*)** - Executes both arg_amount_valid() and table_valid() methods to fully test the command's validity
* **exec_actions(*\*table_actions*)** - Match the command's table and execute the according table action

## Class Table
**Location**: [/listing_tracker/database/tables.py](/listing_tracker/database/tables.py)

### \_\_init\_\_ Properties 
* **name (*string*)** - The name of the table
* **columns (*list*)** - Always starts out as an empty list; the assign_columns method adds columns to the list

### Methods
* **assign_columns(*columns*)** - Add one or more instances of [Class Column](#class-column) to the table's columns list
* **exists()** - Finds if the table exists in the database with the created python dict and returns true or false
* **create()** - Create the table in the database with the created python dict
* **insert(*values*)** - Insert a row of information into the database
* **insert_many(*values_list*)** - Insert many rows of information into the database
* **view()** - View the table in the database

## Class View([Database](#class-databasecommand))
**Location**: [/listing_tracker/commands.py](/listing_tracker/commands.py)

### Parents
* [Database(Command)](#class-databasecommand)

### \_\_init\_\_ Properties
* **args (*list*)** - [**Inherited from Parent**] The command's arguments
* **arg_amount (*int*)** - [**Inherited from Parent**] The amount of arguments provided in the command
* **table (*string*)** - [**Inherited from Parent**] The first argument of the database command

### Methods
* **arg_amount_valid(*expected_arg_amount, fixed_amount*)** - [**Inherited from Parent**] Validates if the correct amount of arguments were provided in the command
* **table_valid()** - [**Inherited from Parent**] Validates if the table is usable for the command
* **valid(*expected_arg_amount, fixed_amount*)** - [**Inherited from Parent**] Executes both arg_amount_valid() and table_valid() methods to fully test the command's validity
* **exec_actions(*\*table_actions*)** - [**Inherited from Parent**] Match the command's table and execute the according table action
* **exec()** - Execute self_valid() and exec_actions() to view the associated table
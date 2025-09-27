# Top Level Files Documentation
**Location**: [/listing_tracker/](/listing_tracker/)

The root directory of this project as specified in "*Location*" has three top level *files*:
* [\_\_init\_\_.py](#__init__py)
* [\_\_main\_\_.py](#__main__py)
* [dir.py](#dirpy)
* [commands.py](#commandspy)

## \_\_init\_\_.py
**Location**: [/listing_tracker/\_\_init\_\_.py](/listing_tracker/__init__.py)

This init file imports [dir.py](#dirpy) to itself for [database/connection.py](/docs/database.md#connectionpy) to access.

## \_\_main\_\_.py
**Location**: [/listing_tracker/\_\_main\_\_.py](/listing_tracker/__main__.py)

As the main file for the tracker, it is where [user commands](/docs/commands.md) are processed and executed.

## dir.py
**Location**: [/listing_tracker/dir.py](/listing_tracker/dir.py)

Grabs the path of the tracker's root directory by detecting its own path and getting its parent.

## commands.py
**Location**: [/listing_tracker/commands.py](/listing_tracker/commands.py)

This file stores these classes used in the program: [Command](/docs/classes.md#class-command), [Database(Command)](/docs/classes.md#class-databasecommand), [Add(Database)](/docs/classes.md#class-adddatabase), and [View(Database)](/docs/classes.md#class-viewdatabase). As a tool of object oriented programming, the classes are reflective of the command hierarchy used in many packages such as this one.
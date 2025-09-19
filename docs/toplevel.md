# Top Level Files Documentation
**Location**: [/listing_tracker/](/listing_tracker/)

The root directory of this project as specified in "*Location*" has three top level *files*:
* [\_\_init\_\_.py](#__init__py)
* [\_\_main\_\_.py](#__main__py)
* [dir.py](#dirpy)

## \_\_init\_\_.py
**Location**: [/listing_tracker/\_\_init\_\_.py](/listing_tracker/__init__.py)

This init file imports [dir.py](#dirpy) to itself for [database/connection.py](/docs/database.md#connectionpy) to access.

## \_\_main\_\_.py
**Location**: [/listing_tracker/\_\_main\_\_.py](/listing_tracker/__main__.py)

As the main file for the tracker, it is where [user commands](/docs/commands.md) are processed and executed.

## dir.py
**Location**: [/listing_tracker/dir.py](/listing_tracker/dir.py)

Grabs the path of the tracker's root directory by detecting its own path and getting its parent.
import database.inserted_webpages
import sys

insert_webpage = database.inserted_webpages.insert_webpage
inserted_webpages_table = database.inserted_webpages.inserted_webpages

if __name__ == "__main__" and len(sys.argv) >= 3:
    arg1_add_cond = sys.argv[1] == "-a" or sys.argv[1] == "-add"
    arg2_webpage_cond = sys.argv[2] == "webpage"
    if arg1_add_cond and arg2_webpage_cond:
        insert_webpage(inserted_webpages_table)
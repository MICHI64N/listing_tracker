import database.listings
import sys

add_listing = database.listings.add_listing
listings_table = database.listings.listings_table

if __name__ == "__main__" and len(sys.argv) >= 3:
    add_cmd = sys.argv[1] == "add"
    webpage_arg = sys.argv[2] == "webpage"
    items_args = sys.argv[3:]
    if add_cmd and webpage_arg and items_args:
        for url in items_args:
            add_listing(listings_table, url)
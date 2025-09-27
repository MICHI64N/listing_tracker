from listing_tracker.database import tables, connection
import datetime, os, re
datetime_type = datetime.datetime

listings_table = tables.Table("listings")
listings_table.assign_columns([tables.Column("link", "text", False, ""),
    tables.Column("website", "text", True, f'{None}'),
    tables.Column("init_datetime", "blob", False, "")])
if not listings_table.exists():
    listings_table.create()

if not os.path.exists(connection.db_path):
    listings_table.create()

def website_identifier(url):
    url = re.sub(r'http[s]?://', "", url)
    domain = re.sub(r'/.*', "", url)
    websites = connection.cursor.execute("SELECT * FROM websites").fetchall()
    for website in websites:
        if domain == website[1]:
            return website[0]
    return "null"

def datetime_adapter(datetime):
    return datetime.isoformat()

def add_listing(url):
    website = website_identifier(url)
    init_datetime = datetime_type.now(datetime.timezone.utc).replace(microsecond=0)
        # 'datetime.timezone.utc' is used instead of 'datetime.UTC' to
        # support Python 3.10
    values = (url, website, datetime_adapter(init_datetime))
    listings_table.insert(values)
    log_message = f'Listing from {website} ({url}) successfully inserted' if website != "null" else f'Listing {url} successfully inserted'
    print(log_message)

def view_listings():
    listings_table.view()
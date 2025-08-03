import database
import datetime
import os
import re
classes = database.classes
connection = database.connection
datetime_type = datetime.datetime

inserted_webpages = classes.Table("inserted_webpages")
inserted_webpages.column_assign([classes.Column("link", "text", False, ""),
    classes.Column("website", "text", True, f'{None}'),
    classes.Column("init_datetime", "blob", False, "")])
inserted_webpages_dict = inserted_webpages.get_dict()
if not inserted_webpages.exists():
    inserted_webpages.create(inserted_webpages_dict)

if not os.path.exists(connection.db_path):
    inserted_webpages.create(inserted_webpages_dict)

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

def insert_webpage(inserted_webpages: classes.Table):
    url = input("E-Commerce Shop URL: ")
    confirm_url = input(f'Is the URL "{url}" correct? Y or N? ')
    if re.match("y", confirm_url.lower()):
        website = website_identifier(url)
        init_datetime = datetime_type.now(datetime.timezone.utc).replace(microsecond=0)
            # 'datetime.timezone.utc' is used instead of 'datetime.UTC' to
            # support Python 3.9 and 3.10
        values = (url, website, datetime_adapter(init_datetime))
        inserted_webpages.insert(values)
import listing_tracker.database.table_class as table_class

website_list = table_class.Table("websites")
website_list.assign_columns([table_class.Column("name", "text", False, ""), table_class.Column("domain", "text", False, "")])
if not website_list.exists():
    website_list.create()
    website_list_values: list[tuple] = [("[COM] Amazon", "www.amazon.com"),
        ("[JP] Amazon", "www.amazon.co.jp"), ("eBay", "www.ebay.com"),
        ("Lashinbang", "shop.lashinbang.com"), ("Mandarake", "www.mandarake.co.jp"),
        ("[COM] Mercari", "www.mercari.com"), ("[JP] Mercari", "jp.mercari.com"), ("[JP] Mercari", "mercari.jp")]
    website_list.insert_many(website_list_values)
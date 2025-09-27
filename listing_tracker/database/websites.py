import listing_tracker.database.tables as tables

website_list = tables.Table("websites")
website_list.assign_columns([tables.Column("name", "text", False, ""), tables.Column("domain", "text", False, "")])
if not website_list.exists():
    website_list.create()
    website_list_values: list[tuple] = [("[COM] Amazon", "www.amazon.com"),
        ("[JP] Amazon", "www.amazon.co.jp"), ("eBay", "www.ebay.com"),
        ("Lashinbang", "shop.lashinbang.com"), ("Mandarake", "www.mandarake.co.jp"),
        ("[JP] Mercari", "jp.mercari.com"), ("[JP] Mercari", "mercari.jp"),
        ("[COM] Mercari", "www.mercari.com")]
    website_list.insert_many(website_list_values)
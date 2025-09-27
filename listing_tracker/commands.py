import listing_tracker.database.tables.listings as listings

class Command:
    def __init__(self, args):
        self.args = args
        self.arg_amount = len(self.args)
    
    def arg_amount_valid(self, expected_arg_amount: int, fixed_amount: bool):
        if self.arg_amount == expected_arg_amount:
            pass
        elif self.arg_amount >= expected_arg_amount and fixed_amount == False:
            pass
        else:
            raise Exception(f'The command has an incorrect amount of arguments: Expected {"minimum" if fixed_amount == False else ""} {expected_arg_amount} arguments but got {self.arg_amount}.')
        
class Database(Command):
    def __init__(self, args):
        super().__init__(args)
        self.type = self.args[0]
        self.valid_types = ["listing"]

    def type_valid(self):
        if not self.type in self.valid_types:
            raise Exception(f'The argument {self.type} is not valid for this command.')
        
    def valid(self, expected_arg_amount, fixed_amount):
        self.arg_amount_valid(expected_arg_amount, fixed_amount)
        self.type_valid()

    def exec_actions(self, listing_action):
        match self.type:
            case "listing":
                return listing_action
            case _:
                print("This is a bug and should not have happened.")

class Add(Database):
    def __init__(self, args):
        super().__init__(args)
        self.urls = self.args[1:]

    def exec(self):
        self.valid(2, False)
        self.exec_actions([listings.add_listing(url) for url in self.urls])

class View(Database):
    def __init__(self, args):
        super().__init__(args)

    def exec(self):
        self.valid(1, True)
        self.exec_actions(listings.view_listings())
import datetime

class Building:
    
    def __init__(self, address, stories):
        self.designer = "Sarah Felts"
        self.date_constructed = None
        self.owner = None
        self.address = address
        self.stories = stories
        
    def construct(self):
        self.date_constructed = datetime.datetime.now()
        
    def purchase(self, new_owner):
        self.owner = new_owner

""" buildings = [eight_hundred_eighth, fifty_fifth_tower, sky_high_plaza, grand_view_apartments, downtown_lofts]
for building in buildings:
    print(f"{building.address} was purchased by {building.owner} on {building.date_constructed.strftime('%m/%d/%Y')} and has {building.stories} stories.") """
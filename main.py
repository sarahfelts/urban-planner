from building import Building
from city import City

eight_hundred_eighth = Building("800 8th Street", 12)
fifty_fifth_tower = Building("55 5th Avenue", 20)
sky_high_plaza = Building("100 Main Street", 30)
grand_view_apartments = Building("500 Elm Street", 15)
downtown_lofts = Building("200 Oak Street", 10)

eight_hundred_eighth.purchase("Bob Buyer")
eight_hundred_eighth.construct()

fifty_fifth_tower.purchase("Hedgefund Horace")
fifty_fifth_tower.construct()

sky_high_plaza.purchase("Bruce Boomer")
sky_high_plaza.construct()

grand_view_apartments.purchase("Two Banks In a Trench Coat")
grand_view_apartments.construct()

downtown_lofts.purchase("Gerald Gentrifier")
downtown_lofts.construct()

metrocity = City("Metrocity", "Megamind", 1836)

metrocity.add_building(eight_hundred_eighth)
metrocity.add_building(fifty_fifth_tower)
metrocity.add_building(sky_high_plaza)
metrocity.add_building(grand_view_apartments)
metrocity.add_building(downtown_lofts)

for building in metrocity.buildings:
    print(f"{building.address} was purchased by {building.owner} on {building.date_constructed.strftime('%m/%d/%Y')} and has {building.stories} stories.")
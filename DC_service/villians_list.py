__author__ = 'Nicholas Rodofile'

villain = {
    "Joker": "Complete unpredictability, intelligence. \n >",
    "Lex Luthor":  "Genius-level intellect, inexhaustible wealth, political influence.\n >",
    "Cheetah":  "Barbara Ann Minerva, is a former archeologist and treasure-hunter who sold her soul to the plant-god Urtzkartaga for power and immortality, not realizing she'd be bound in eternal servitude to him. \n >",
    "Captain Boomerang":  "George \"Digger\" Harkness, best known under his alias Captain Boomerang or just Boomerang,",
    "Black Manta":  "Exceptional martial artist, exceptional swimming ability, energy blasts \n>",
    "Sinestro": "hard light constructs, instant weaponry, force fields, flight, durability, alien technology, fear provocation, intelligence. \n >",
}

def my_service(data):
    if data in villain:
        return villain[data]
    return "villain Not found!\n >"


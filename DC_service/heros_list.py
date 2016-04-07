__author__ = 'Nicholas Rodofile'

heros = {
    "Batman": "exceptional martial artist, combat strategy, inexhaustible wealth, brilliant deductive skill, advanced technology. \n >",
    "Superman": "super strength, flight, invulnerability, super speed, heat vision, freeze breath, x-ray vision, superhuman hearing, healing factor. \n >",
    "Wonder Woman": "super strength, invulnerability, flight, combat skill, combat strategy, superhuman agility, healing factor, magic weaponry. \n >",
    "Flash": "super speed, intangibility, superhuman agility",
    "Aquaman": "super strength, durability, control over sea life, exceptional swimming ability, ability to breathe underwater. \n >",
    "Green Lantern": "hard light constructs, instant weaponry, force fields, flight, durability, alien technology. \n >",
}

def my_service(data):
    if data in heros:
        return heros[data]
    return "Hero Not found!\n >"


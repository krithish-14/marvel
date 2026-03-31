import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marvel_site.settings')
django.setup()

from marvel.models import Comic

comics = [
    {
        "title": "Infinity War",
        "image": "infinity.jpg",
        "desc": "The ultimate cosmic battle! Thanos seeks to control the universe using the Infinity Gauntlet, forcing Earth's mightiest heroes to unite and face their greatest challenge.",
        "url": "https://www.marvel.com/comics/discover/55/infinity-war"
    },
    {
        "title": "Secret Wars",
        "image": "comic1.avif",
        "desc": "The Multiverse is dying! See the collision of countless realities as Doctor Doom reshapes the universe into Battleworld, where only the strongest survive.",
        "url": "https://www.marvel.com/comics/discover/333/secret-wars"
    },
    {
        "title": "Marvels",
        "image": "marvels.jpeg",
        "desc": "Experience the dawn of the Marvel Age from the perspective of an ordinary man. Photographer Phil Sheldon chronicles the spectacular and terrifying arrival of superheroes.",
        "url": "https://www.marvel.com/comics/series/2048/marvels_1994"
    },
    {
        "title": "Daredevil: Born Again",
        "image": "daredevil.jpeg",
        "desc": "The Kingpin has discovered Daredevil's secret identity and systematically dismantles Matt Murdock's life. A gripping tale of downfall and triumphant resurrection.",
        "url": "https://www.marvel.com/comics/discover/1623/daredevil-born-again"
    },
    {
        "title": "X-Men: Dark Phoenix Saga",
        "image": "xmen.jpg",
        "desc": "Jean Grey gains absolute, god-like power that corrupts her soul. The X-Men must decide whether to save their dearest friend or save the entire universe.",
        "url": "https://www.marvel.com/comics/discover/61/dark-phoenix-saga"
    },
    {
        "title": "Civil War",
        "image": "civil war.webp",
        "desc": "Whose side are you on? Following a tragic disaster, the U.S. government forces superheroes to register, splitting the Avengers into factions led by Iron Man and Captain America.",
        "url": "https://www.marvel.com/comics/discover/114/civil-war-the-complete-event"
    },
    {
        "title": "World War Hulk",
        "image": "world war hulk.jpg",
        "desc": "Banished into space, the Hulk returns stronger and angrier than ever. He invades Earth to seek revenge on the heroes who exiled him.",
        "url": "https://www.marvel.com/comics/discover/1230/world-war-hulk"
    },
    {
        "title": "Thor: God of Thunder",
        "image": "thor god.jpg",
        "desc": "Gorr the God Butcher is murdering deities across time and space. Follow three eras of Thor as he attempts to stop the relentless killer.",
        "url": "https://www.marvel.com/comics/series/16729/thor_god_of_thunder_2012_-_2014"
    },
    {
        "title": "Hawkeye: My Life as a Weapon",
        "image": "hawkeye1.jpg",
        "desc": "Discover what Clint Barton does when he's not an Avenger. A critically acclaimed, street-level look at the life of Marvel's favorite marksman.",
        "url": "https://www.marvel.com/comics/series/16309/hawkeye_2012_-_2015"
    }
]

Comic.objects.all().delete()
for c in comics:
    Comic.objects.create(title=c['title'], image_name=c['image'], description=c['desc'], purchase_url=c['url'])

print('Comics populated.')

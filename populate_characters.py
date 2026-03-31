import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marvel_site.settings')
django.setup()

from marvel.models import Character

chars = [
    {"name": "Iron Man", "image": "iron man 1.jpg", "short": "Genius, billionaire, playboy, philanthropist.", "detailed": "Tony Stark is the wealthy son of industrialist and weapons manufacturer Howard Stark. After being kidnapped by terrorists and suffering a severe heart injury, he creates a powered suit of armor to save his life and escape. He then uses the suit to protect the world as Iron Man."},
    {"name": "Spider-Man", "image": "spider man 1.jpg", "short": "Friendly neighborhood web-slinger.", "detailed": "Peter Parker was bitten by a radioactive spider, granting him superhuman strength, agility, and the ability to cling to walls. After the murder of his Uncle Ben, he learns that 'with great power comes great responsibility' and becomes the superhero Spider-Man."},
    {"name": "Hulk", "image": "hulk 1.jpg", "short": "The Green Goliath.", "detailed": "Dr. Bruce Banner was exposed to massive amounts of gamma radiation. Now, whenever he experiences anger or stress, he transforms into the Hulk, a giant, green, incredibly powerful creature driven by rage and primal instincts."},
    {"name": "Captain America", "image": "captain.jpeg", "short": "The First Avenger.", "detailed": "Steve Rogers was a scrawny fine arts student who volunteered for a top-secret military experiment during WWII. Injected with the Super-Soldier Serum, his body was enhanced to the peak of human potential. He wields a virtually indestructible vibranium shield."},
    {"name": "Thor", "image": "thor.jpg", "short": "God of Thunder.", "detailed": "Thor Odinson is the Asgardian God of Thunder, who wields the enchanted hammer Mjolnir, which grants him the ability to fly and manipulate weather. He protects Earth and the Nine Realms from cosmic threats."},
    {"name": "Black Panther", "image": "black 2.jpg", "short": "King of Wakanda.", "detailed": "T'Challa is the King of the secretive and highly advanced African nation of Wakanda. As the Black Panther, he is enhanced by a heart-shaped herb and wears a vibranium suit, protecting his people and the world."},
    {"name": "Black Widow", "image": "black widow.webp", "short": "Expert spy and lethal assassin.", "detailed": "Natasha Romanoff was trained in the Red Room Academy to be a master assassin and spy. She later defected from the KGB to join S.H.I.E.L.D. and became a founding member of the Avengers."},
    {"name": "Captain Marvel", "image": "captain marvel.webp", "short": "Cosmic powers.", "detailed": "Carol Danvers is a former U.S. Air Force pilot who, upon being exposed to the energy of the Tesseract, obtained cosmic powers. She is considered one of the most powerful heroes in the universe."},
    {"name": "Scarlet Witch", "image": "Scarlet_Witch.jpg", "short": "Reality manipulation.", "detailed": "Wanda Maximoff has natural, reality-altering abilities enhanced by the Mind Stone. She has incredible telekinetic and telepathic powers, and profound magical potential."},
    {"name": "Ant-Man", "image": "ant man.jpg", "short": "Size-shifting thief.", "detailed": "Scott Lang is a master thief who uses a specialized suit created by Hank Pym to shrink in scale but increase in strength. He can also communicate with ants and grow to giant sizes."},
    {"name": "Deadpool", "image": "deadpool.jpg", "short": "Merc with a Mouth.", "detailed": "Wade Wilson is a wisecracking mercenary with a severely scarred physical appearance, an accelerated healing factor, and a tendency to break the fourth wall."},
    {"name": "Hawkeye", "image": "hawekey.jpeg", "short": "Master archer.", "detailed": "Clint Barton is a master archer and former special agent of S.H.I.E.L.D. Despite having no superhuman abilities, his unparalleled accuracy and specialized arrows make him a formidable Avenger."}
]

Character.objects.all().delete()
for c in chars:
    Character.objects.create(name=c['name'], image_name=c['image'], short_desc=c['short'], detailed_desc=c['detailed'])

print('Characters populated.')

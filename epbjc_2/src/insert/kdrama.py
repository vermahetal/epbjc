import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO kdrama (nome) VALUES ("Celebrity")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Itaewon Class")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Goblin")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Crash Landing on You")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Descendants of the Sun")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Vincenzo")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("My Love from the Star")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Start Up")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Heirs")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Hometown Cha Cha Cha")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("True Beauty")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Extraordinary Attorney Woo")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Twenty Five Twenty One")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Alchemy of Souls")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Weightlifting Fairy Kim Bok Joo")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Tomorrow")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Mr Sunshine")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Business Proposal")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Signal")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Hotel Del Luna")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Strong Woman Do Bong Soon")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Its Okay to Not Be Okay")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Penthouse War in Life")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Doctor Stranger")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("While You Were Sleeping")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Cheese in the Trap")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("The King Eternal Monarch")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Love Alarm")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Legend of the Blue Sea")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Moon Lovers Scarlet Heart Ryeo")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Secret Garden")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Pinocchio")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("The World of the Married")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Reply 1988")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Sky Castle")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Prison Playbook")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("My Mister")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Doctor Romantic")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Live")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Her Private Life")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Into the Ring")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("My ID is Gangnam Beauty")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Find Me in Your Memory")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Smile Has Left Your Eyes")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("When the Camellia Blooms")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Angel Eyes")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Flower of Evil")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Man to Man")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("Cheer Up")')
cursor.execute('INSERT INTO kdrama (nome) VALUES ("The Glory")')

conn.commit()
conn.close()
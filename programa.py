####EL BUENO
import random
from collections import deque

def ganacion():
    print(f"La {semana[ns]} semana de {mes[nm]} del año {ano[na]} {ganador} se ha coronado ganador.\n¡Enhorabuena {ganador}!\n#HeroWarBot")



personajesbase = ['Batman', 'Spider-man', 'Superman', 'Iron man', 'Flash', 'Wolverine', 'Capitan America', 'Thor', 'Wonderwoman', 'Hulk', 
 'Deadpool', 'Supergirl', 'Linterna Verde', 'Black Widow', 'Green Arrow', 'El Joker', 'Antorcha Humana', 'Magneto', 'Pantera Negra', 'Daredevil',
 'Catwoman', 'Ciclope', 'Storm', 'Black Canary', 'Invisible Woman', 'Silver Surfer', 'Ojo de Halcon', 'Shazam', 'Martian Manhunter', 'Power Girl',
 'Bruja Escarlata', 'Bestia', 'Fenix', 'Hawkgirl', 'Vision', 'Rondador Nocturno', 'Black Cat', 'Magneto', 'Hawkman', 'Kid Flash',
 'Falcon', 'Hiedra Venenosa', 'She-Hulk', 'Nova', 'Quick Silver', 'X-23', 'Big Daddy', 'Archangel', 'Spider-Woman', 'Blade',
 'Cheetah', 'The Wasp', 'Emma Frost', 'Atom', 'Red Arrow', 'Doctor Doom', 'Atrocitus', 'Kitty Pryde', 'Flash Girl', 'Ego',
 'Enchantress', 'Black Adam', 'Wonderman', 'Isis', 'Jack Jack', 'Northstar', 'Spawn', 'Elastigirl', 'Hellboy', 'Constantine',
 'M.O.D.O.K', 'The Comedian', 'Nite Owl', 'Ozymandias', 'Dr. Manhattan', 'Rorschach', 'Silk Spectre', 'Ant-Man', 'Profesor X',
 'Lex Luthor', 'Aquaman', 'Venom', 'Dr. Strange', 'Loki', 'Thanos', 'Groot', 'Rocket', 'Punisher', 'Star Lord',
 'Ghost Rider', 'Bucky', 'Ultron', 'Duende Verde', 'Gambito', 'Gamora', 'Drax', 'Juggernaut', 'Coloso', 'Nick Fury',
 'Galactus', 'Dr. Octupus', 'Carnage', 'Dr. Sivana', 'Elektra', 'Red Skull', 'Spider Gwen', 'Iron Fist', 'Mistica', 'Miles Morales', 
 'Odin', 'Hancock', 'Adam Warlock', 'Nebula', 'Red Hulk', 'Spider-Man Noir', 'Spider-Ham', 'Kingpin', 'Cable', 'Rhino', 
 'Dormammu', 'Electro', 'Mysterio', 'Buitre', 'Scorpion', 'Howard el Pato', 'Egghead', 'Phil Coulson', 'Maria Hill', 'War Machine',
 'Wong', 'Valquiria', 'Shuri', 'Tritonman', 'Kick-Ass', 'Chico Percebe', 'Tommy Oliver', 'Mantis', 'Hela', 'Hit-girl',
 'The Thing', 'Robin', 'Mr. Increible', 'Bane', 'La Rata de Ant-man', 'Cyborg', 'Heimdall', 'Yondu', 'Red Hood', 'Apocalypse',
 'Mr. Fantastico', 'Sabretooth', 'Domino', 'Flash Reverso', 'Gorila Grodd', 'Captain Cold', 'Heat Wave', 'Siniestro', 'Black Manta', 'Misterio',
 'Cabeza Martillo', 'Ocean Master', 'Syndrome', 'Zatanna', 'El Pingüino', 'Enigma', 'Death Stroke', 'Killer Croc', 'Herley Quinn', 'Dos Caras',
 'Man Bat', 'Black Mask', 'Katana', 'Rogue', 'Batgirl', 'Bizarro', 'Brainiac', 'Deadshot',
 'Spider-Woman', 'Bullseye', 'Ra s Al Ghul', 'Polilla Asesina', 'Captain Boomerang', 'Trickster', 'Kill Monger', 'El Mandarín', 'La Cosa del Pantano', 'Lockjaw','Medusa','Firestorm','Eternity',
  'Lobo','Kang','Aniquilación','Nighthawk','Dagger','Escorpio','Pesadilla','Clove','Doctor Fate','Aqualad','Blue Beetle','Black Bolt']

semana = ('Primera','Segunda','Tercera','Cuarta')
mes = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
ano = (2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040)

nm = 0
ns = 0
na = 0


bonus = {'Batman':0, 'Spider-man':0, 'Superman':0, 'Iron man':0, 'Flash':0, 'Wolverine':0, 'Capitan America':0, 'Thor':0, 'Wonderwoman':0, 'Hulk':0, 
  'Deadpool':0, 'Supergirl':0, 'Linterna Verde':0, 'Black Widow':0, 'Green Arrow':0, 'El Joker':0, 'Antorcha Humana':0, 'Magneto':0, 'Pantera Negra':0, 'Daredevil':0,
  'Catwoman':0, 'Ciclope':0, 'Storm':0, 'Black Canary':0, 'Invisible Woman':0, 'Silver Surfer':0, 'Ojo de Halcon':0, 'Shazam':0, 'Martian Manhunter':0, 'Power Girl':0,
  'Bruja Escarlata':0, 'Bestia':0, 'Fenix':0, 'Hawkgirl':0, 'Vision':0, 'Rondador Nocturno':0, 'Black Cat':0, 'Magneto':0, 'Hawkman':0, 'Kid Flash':0,
  'Falcon':0, 'Hiedra Venenosa':0, 'She-Hulk':0, 'Nova':0, 'Quick Silver':0, 'X-23':0, 'Big Daddy':0, 'Archangel':0, 'Spider-Woman':0, 'Blade':0,
  'Cheetah':0, 'The Wasp':0, 'Emma Frost':0, 'Atom':0, 'Red Arrow':0, 'Doctor Doom':0, 'Atrocitus':0, 'Kitty Pryde':0, 'Flash Girl':0, 'Ego':0,
  'Enchantress':0, 'Black Adam':0, 'Wonderman':0, 'Isis':0, 'Jack Jack':0, 'Northstar':0, 'Spawn':0, 'Elastigirl':0, 'Hellboy':0, 'Constantine':0,
  'M.O.D.O.K':0, 'The Comedian':0, 'Nite Owl':0, 'Ozymandias':0, 'Dr. Manhattan':0, 'Rorschach':0, 'Silk Spectre':0, 'Ant-Man':0, 'Profesor X':0,
  'Lex Luthor':0, 'Aquaman':0, 'Venom':0, 'Dr. Strange':0, 'Loki':0, 'Thanos':0, 'Groot':0, 'Rocket':0, 'Punisher':0, 'Star Lord':0,
  'Ghost Rider':0, 'Bucky':0, 'Ultron':0, 'Duende Verde':0, 'Gambito':0, 'Gamora':0, 'Drax':0, 'Juggernaut':0, 'Coloso':0, 'Nick Fury':0,
  'Galactus':0, 'Dr. Octupus':0, 'Carnage':0, 'Dr. Sivana':0, 'Elektra':0, 'Red Skull':0, 'Spider Gwen':0, 'Iron Fist':0, 'Mistica':0, 'Miles Morales':0, 
  'Odin':0, 'Hancock':0, 'Adam Warlock':0, 'Nebula':0, 'Red Hulk':0, 'Spider-Man Noir':0, 'Spider-Ham':0, 'Kingpin':0, 'Cable':0, 'Rhino':0, 
  'Dormammu':0, 'Electro':0, 'Mysterio':0, 'Buitre':0, 'Scorpion':0, 'Howard el Pato':0, 'Egghead':0, 'Phil Coulson':0, 'Maria Hill':0, 'War Machine':0,
  'Wong':0, 'Valquiria':0, 'Shuri':0, 'Tritonman':0, 'Kick-Ass':0, 'Chico Percebe':0, 'Tommy Oliver':0, 'Mantis':0, 'Hela':0, 'Hit-girl':0,
  'The Thing':0, 'Robin':0, 'Mr. Increible':0, 'Bane':0, 'La Rata de Ant-man':0, 'Cyborg':0, 'Heimdall':0, 'Yondu':0, 'Red Hood':0, 'Apocalypse':0,
  'Mr. Fantastico':0, 'Sabretooth':0, 'Domino':0, 'Flash Reverso':0, 'Gorila Grodd':0, 'Captain Cold':0, 'Heat Wave':0, 'Siniestro':0, 'Black Manta':0, 'Misterio':0,
  'Cabeza Martillo':0, 'Ocean Master':0, 'Syndrome':0, 'Zatanna':0, 'El Pingüino':0, 'Enigma':0, 'Death Stroke':0, 'Killer Croc':0, 'Herley Quinn':0, 'Dos Caras':0,
  'Man Bat':0, 'Black Mask':0, 'Katana':0, 'Rogue':0, 'Batgirl':0, 'Bizarro':0, 'Brainiac':0, 'Deadshot':0,
  'Spider-Woman':0, 'Bullseye':0, 'Ra s Al Ghul':0, 'Polilla Asesina':0, 'Captain Boomerang':0, 'Trickster':0, 'Kill Monger':0, 'El Mandarín':0, 'La Cosa del Pantano':0, 'Lockjaw':0,'Medusa':0,'Firestorm':0,'Eternity':0,
   'Lobo':0,'Kang':0,'Aniquilación':0,'Nighthawk':0,'Dagger':0,'Escorpio':0,'Pesadilla':0,'Clove':0,'Doctor Fate':0,'Aqualad':0,'Blue Beetle':0,'Black Bolt':0}

resultado= deque()
contacion= 1

try:
    while 1 == 1:
        if len(personajesbase) == 1:
            ganador = personajesbase.pop()
            ganacion()
        cincuenta = 50
        pj1 = random.choice(personajesbase)
        pj2 = random.choice(personajesbase)
        while pj1 == pj2:
            pj2 = random.choice(personajesbase)        
        if ns == 4:
            ns = 0
            nm +=1
        if nm == 12:
            nm = 0
            na +=1
        muerte = random.randint(0, 100)
        
        if bonus[f"{pj1}"] > 0 or bonus[f"{pj2}"] > 0:
            if bonus[f"{pj1}"] < bonus[f"{pj2}"]:
                cincuenta = cincuenta - (bonus[f"{pj1}"]-bonus[f"{pj2}"])
            if bonus[f"{pj1}"] > bonus[f"{pj2}"]:
                cincuenta = cincuenta + (bonus[f"{pj1}"]-bonus[f"{pj2}"])
#        print(cincuenta)
        if cincuenta <= muerte:
            print(f"{semana[ns]} semana de {mes[nm]}. Año {ano[na]}.\n{pj2} a acabado con {pj1}\n#HeroWarBot\n")
            resultado.append(f"{semana[ns]} semana de {mes[nm]}. Año {ano[na]}.\n{pj2} a acabado con {pj1}\n#HeroWarBot\n")
            personajesbase.remove(f"{pj2}")
#            print(f"\n{personajesbase}\n")
            print(contacion)
            if bonus[f"{pj2}"] < 30:
                bonus[f"{pj2}"]+=5
        
        if cincuenta > muerte:
            print(f"{semana[ns]} semana de {mes[nm]}. Año {ano[na]}.\n{pj1} a acabado con {pj2}\n#HeroWarBot\n")
            resultado.append(f"{semana[ns]} semana de {mes[nm]}. Año {ano[na]}.\n{pj1} a acabado con {pj2}\n#HeroWarBot\n")
            personajesbase.remove(f"{pj2}")
#            print(f"\n{personajesbase}\n")
            print(contacion)
            if bonus[f"{pj1}"] < 30:
                bonus[f"{pj1}"]+=5
        ns = ns+1
        contacion+=1
        
except:
    pass
finally:
    print(f"\n{resultado}")

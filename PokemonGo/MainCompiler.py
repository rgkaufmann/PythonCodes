import DataHandler
import math

dataheader = "C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/PokemonGo/"
data = DataHandler.DataHandler()
BASESTATSDTYPE = [("Name", "S14"), ("BaseATK", "i4"), ("BaseDEF", "i4"), ("BaseSTM", "i4"), ("MaxCP", "i4"),
                  ("Type1", "S14"), ("Type2", "S14")]
POKETYPES = ['Normal', 'Fire', 'Fighting', 'Water', 'Flying', 'Grass', 'Poison', 'Electric', 'Ground', 'Psychic',
             'Rock', 'Ice', 'Bug', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy']

newpoke = input("Is there a new Pokemon that has been added to the roster?\n")
if newpoke.lower() == "yes":
    if not data.loadtxt(dataheader + "DataFiles/BaseStats.txt", BASESTATSDTYPE):
        quit()
    newpokemonstats = []
    name = input("What is the name of the new pokemon?\n")
    while newpoke.lower() == "yes":
        if name.capitalize() not in data.getdata()["Name"]:
            try:
                baseatk = int(input("What is the base attack of "+name.capitalize()+"?\n"))
                basedef = int(input("What is the base defense of "+name.capitalize()+"?\n"))
                basestm = int(input("What is the base stamina of "+name.capitalize()+"?\n"))
                type1 = input("What is the primary type of "+name.capitalize()+"?\n")
                istype2 = input("Does "+name.capitalize()+" have a secondary type?\n")
                if istype2.lower() == 'yes':
                    type2 = input("What is the secondary type of "+name.capitalize()+"?\n")
                else:
                    type2 = "None"
                maxcp = int(math.floor((baseatk+15)*(basedef+15)**0.5*(basestm+15)**0.5*0.790300**2/10))
            except ValueError:
                print("Data did not enter correctly, try again.")
                continue
            if type1.capitalize() not in POKETYPES and (type2.capitalize() not in POKETYPES and type2 != "None"):
                print("Data did not enter correctly, try again.")
                continue
            print("\n")
            print([name.capitalize(), baseatk, basedef, basestm, maxcp, type1.capitalize(), type2.capitalize()])
            confirm = input("Is the above infomation correct?\n")
            if confirm.lower() == "yes":
                newpokemonstats.append([name.capitalize(), baseatk, basedef, basestm, maxcp, type1.capitalize(),
                                        type2.capitalize()])
            else:
                print("Data did not enter correctly, try again.")
                continue
        newpoke = input("Is there a new Pokemon that has been added to the roster?\n")
        if newpoke.lower() == "yes":
            name = input("What is the name of the new pokemon?\n")
    data.adddata(newpokemonstats)
    data.savetxt(dataheader + "DataFiles/BaseStats.txt")

shouldcheck = input("Should the roster be checked for accuracy?\n")
if shouldcheck.lower() == 'yes':
    if not data.loadtxt(dataheader + "DataFiles/BaseStats.txt", BASESTATSDTYPE):
        quit()
    data.checkdata(POKETYPES)

data.loadtxt(dataheader + 'DataFiles/BaseStats.txt', BASESTATSDTYPE)
data.quickpokedex(dataheader + 'DataFiles/Pokedex.txt')

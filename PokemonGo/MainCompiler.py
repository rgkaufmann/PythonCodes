import DataHandler
import math

dataheader = "C:/Users/ryank/Desktop/Github/PythonCodes/PokemonGo/"
data = DataHandler.DataHandler()
BASESTATSDTYPE = [("Name", "S14"), ("BaseATK", "i4"), ("BaseDEF", "i4"), ("BaseSTM", "i4"), ("MaxCP", "i4")]

newpoke = raw_input("Is there a new Pokemon that has been added to the roster?\n")
if newpoke.lower() == "yes":
    if not data.loadtxt(dataheader + "DataFiles/BaseStats.txt", BASESTATSDTYPE):
        quit()
    newpokemonstats = []
    name = raw_input("What is the name of the new pokemon?\n")
    while newpoke.lower() == "yes":
        if name.capitalize() not in data.getdata()["Name"]:
            try:
                baseatk = int(raw_input("What is the base attack of "+name.capitalize()+"?\n"))
                basedef = int(raw_input("What is the base defense of "+name.capitalize()+"?\n"))
                basestm = int(raw_input("What is the base stamina of "+name.capitalize()+"?\n"))
                maxcp = int(math.floor((baseatk+15)*(basedef+15)**0.5*(basestm+15)**0.5*0.790300**2/10))
            except ValueError:
                print "Data did not enter correctly, try again."
                continue
            print "\n"
            print [name.capitalize(), baseatk, basedef, basestm, maxcp]
            confirm = raw_input("Is the above infomation correct?\n")
            if confirm.lower() == "yes":
                newpokemonstats.append([name.capitalize(), baseatk, basedef, basestm, maxcp])
            else:
                print "Data did not enter correctly, try again."
                continue
        newpoke = raw_input("Is there a new Pokemon that has been added to the roster?\n")
        if newpoke.lower() == "yes":
            name = raw_input("What is the name of the new pokemon?\n")
    data.adddata(newpokemonstats)
    data.savetxt(dataheader + "DataFiles/BaseStats.txt")

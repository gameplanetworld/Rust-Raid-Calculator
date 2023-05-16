#imports

import math
from colorama import Fore
import os

#varibles

start = True

#start

while start == True:
    print("[1] Rockets")
    print("[2] C4")
    print("[3] Explosive ammo")
    print("[4] Satchel charge")
    
    userinput = input()
    
    #Rockets
    
    if userinput == "1":
        #rockets choose
        os.system("cls")
        print("[1] sulfur")
        print("[2] craft")
        
        rinput = input()
        
        
        #sulfur craft
        
        if rinput == "1":
            #input
            os.system("cls")
            print("Sulfur ammount?")
            rsinput = input()
            
            #rocket ammount
            rsrocketammount = int(rsinput) / 1400
            
            #suflur needed
            rsexp1 = int(rsrocketammount) * 100
            
            rsexp2 = int(rsinput) - int(rsexp1)
                        
            #resource needed
            rscharcoal = int(rsexp2) / 20 * 30
            rsgunpowder = int(rsrocketammount) * 650
            rsgunpowdercraft = int(rsgunpowder) / 10
            rsmetalfrags = int(rsrocketammount) * 100
            rslowgrade = int(rsrocketammount) * 30
            rsexplosivecraft = int(rsrocketammount) * 10
            rspipe = int(rsrocketammount) * 2
            
            rsprocketammount = math.trunc(int(rsrocketammount))
            rspcharcoal = math.trunc(int(rscharcoal))
            rspgunpowdercraft = math.trunc(int(rsgunpowdercraft))
                        
            #print
            os.system("cls")
            print("[", Fore.CYAN + "Rockets" + Fore.WHITE,"]")
            print("Rockets: ", Fore.GREEN + str(rsprocketammount) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Charcoal: ",Fore.BLUE + str(rspcharcoal) + Fore.WHITE)
            print("Gunpowder: ",Fore.BLUE + str(rsgunpowder) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(rsmetalfrags) + Fore.WHITE)
            print("Low grade: ",Fore.BLUE + str(rslowgrade) + Fore.WHITE)
            print("Metal pipes", Fore.BLUE + str(rspipe) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(rspgunpowdercraft) + Fore.WHITE)
            print("Explosives craft: ",Fore.MAGENTA + str(rsexplosivecraft) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit
        
        #rocket craft
        
        if rinput == "2":
            #input
            os.system("cls")
            print("Rocket ammount?")
            rrinput = input()
            
            #resource calculate
            rrsulfur = int(rrinput) * 1400
            rrcharcoal = int(rrinput) * 1950
            rrexplosives = int(rrinput) * 10
            rrmetalpipe = int(rrinput) * 2
            rrlowgrade = int(rrinput) * 30
            rrmetalfrags = int(rrinput) * 100
            rrgunpowder = int(rrinput) * 650
            rrgunpowdercraft = int(rrgunpowder) / 10
            
            #math
            rrpgunpowdercraft = math.trunc(rrgunpowdercraft)

            #print
            os.system("cls")
            print("[", Fore.CYAN + "Rockets" + Fore.WHITE,"]")
            print("Rockets: ", Fore.GREEN + str(rrinput) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Sulfur: ",Fore.BLUE + str(rrsulfur) + Fore.WHITE)
            print("Charcoal: ",Fore.BLUE + str(rrcharcoal) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(rrmetalfrags) + Fore.WHITE)
            print("Low grade: ",Fore.BLUE + str(rrlowgrade) + Fore.WHITE)
            print("Metal pipes", Fore.BLUE + str(rrmetalpipe) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(rrpgunpowdercraft) + Fore.WHITE)
            print("Explosives craft: ",Fore.MAGENTA + str(rrexplosives) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit
        
        else:
            quit

    #C4

    if userinput == "2":
        #c4 choose
        os.system("cls")
        print("[1] Sulfur")
        print("[2] Craft")
        cinput = input()
        
        #c4 sulfur
        
        if cinput == "1":
            #input
            os.system("cls")
            print("Sulfur ammount?")
            csinput = input()
            
            #c4 ammount
            csc41 = int(csinput) / 2200
            csc4 = math.trunc(csc41)
            
            #materials
            csexplosives = int(csc4) * 20
            cstechtrash = int(csc4) * 2
            cscloth = int(csc4) * 5
            cscharcoal = int(csc4) * 3000
            cslowgrade = int(csc4) * 60
            csmetalfrags = int(csc4) * 100
            csgunpowder = int(csc4) * 1000
            csgunpowdercraft = int(csc4) * 100
            
            #print
            os.system("cls")
            print("[", Fore.CYAN + "C4" + Fore.WHITE,"]")
            print("C4: ", Fore.GREEN + str(csc4) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Charcoal: ",Fore.BLUE + str(cscharcoal) + Fore.WHITE)
            print("Gunpowder: ",Fore.BLUE + str(csgunpowder) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(csmetalfrags) + Fore.WHITE)
            print("Low grade: ",Fore.BLUE + str(cslowgrade) + Fore.WHITE)
            print("Tech trash", Fore.BLUE + str(cstechtrash) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(csgunpowdercraft) + Fore.WHITE)
            print("Explosives craft: ",Fore.MAGENTA + str(csexplosives) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit

        #c4 craft
        if cinput == "2":
            #input
            os.system("cls")
            print("C4 ammount?")
            ccinput = input()
            
            #resource calculate
            ccsulfur = int(ccinput) * 2200
            cccharcoal = int(ccinput) * 3000
            ccexplosives = int(ccinput) * 20
            cctechtrash = int(ccinput) * 2
            cclowgrade = int(ccinput) * 60
            ccmetalfrags = int(ccinput) * 200
            ccgunpowder = int(ccinput) * 1000
            ccgunpowdercraft = int(ccgunpowder) / 10
            cccloth = int(ccinput) * 5
            
            #math
            ccpgunpowdercraft = math.trunc(ccgunpowdercraft)

            #print
            os.system("cls")
            print("[", Fore.CYAN + "C4" + Fore.WHITE,"]")
            print("C4: ", Fore.GREEN + str(ccinput) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Sulfur: ",Fore.BLUE + str(ccsulfur) + Fore.WHITE)
            print("Charcoal: ",Fore.BLUE + str(cccharcoal) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(ccmetalfrags) + Fore.WHITE)
            print("Low grade: ",Fore.BLUE + str(cclowgrade) + Fore.WHITE)
            print("Tech trash", Fore.BLUE + str(cctechtrash) + Fore.WHITE)
            print("Cloth", Fore.BLUE + str(cccloth) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(ccpgunpowdercraft) + Fore.WHITE)
            print("Explosives craft: ",Fore.MAGENTA + str(ccexplosives) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit
        
        else:
            quit

    #Explosive ammo
    
    if userinput == "3":
        #Exploammo choose
        os.system("cls")
        print("[1] Sulfur")
        print("[2] Craft")
        einput = input()
        
        #Sulfur
        
        if einput == "1":
            #input
            os.system("cls")
            print("Sulfur ammount?")
            esinput = input()
            
            #Explosive ammo ammount
            esexplo = int(esinput) / 50
            esexplo1 = math.trunc(esexplo)
            
            #Materials
            escharcoal = int(esexplo) * 30
            esgunpowder = int(esexplo) * 10
            esmetalfrags = int(esexplo) * 5
            esgunpowdercraft = int(esgunpowder) / 10
            espgunpowdercraft = math.trunc(esgunpowdercraft)
            
            #print
            os.system("cls")
            print("[", Fore.CYAN + "Explosive ammo" + Fore.WHITE,"]")
            print("Explosive ammo: ", Fore.GREEN + str(esexplo1) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Charcoal: ",Fore.BLUE + str(escharcoal) + Fore.WHITE)
            print("Gunpowder: ",Fore.BLUE + str(esgunpowder) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(esmetalfrags) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(espgunpowdercraft) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit

        #Craft
        
        if einput == "2":
            #input
            os.system("cls")
            print("Explosive ammo ammount?")
            ecinput = input()
            
            #Explosive ammo ammount
            ecexplo = math.trunc(int(ecinput))
            
            #Materials
            ecsulfur = int(ecexplo) * 25
            eccharcoal = int(ecexplo) * 30
            ecgunpowder = int(ecexplo) * 10
            ecmetalfrags = int(ecexplo) * 5
            ecgunpowdercraft = int(ecgunpowder) / 10
            ecpgunpowdercraft = math.trunc(ecgunpowdercraft)
            
            #print
            os.system("cls")
            print("[", Fore.CYAN + "Explosive ammo" + Fore.WHITE,"]")
            print("Explosive ammo: ", Fore.GREEN + str(ecinput) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Sulfur: ",Fore.BLUE + str(ecsulfur) + Fore.WHITE)
            print("Charcoal: ",Fore.BLUE + str(eccharcoal) + Fore.WHITE)
            print("Gunpowder: ",Fore.BLUE + str(ecgunpowder) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(ecmetalfrags) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(ecpgunpowdercraft) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit
    
    #Satchel charge

        else:
            quit
    
    #Satchel charge
    
    if userinput == "4":
        #Satchel choose
        os.system("cls")
        print("[1] Sulfur")
        print("[2] Craft")
        cinput = input()
        
        #Sulfur
        
        if cinput == "1":
            #input
            os.system("cls")
            print("Sulfur ammount?")
            csinput = input()
            
            #Explosive ammo ammount
            csexplo = int(csinput) / 480
            csexplo1 = math.trunc(csexplo)
            
            #Materials
            cscharcoal = int(csexplo) * 720
            csgunpowder = int(csexplo) * 240
            csmetalfrags = int(csexplo) * 80
            csgunpowdercraft = int(csgunpowder) / 10
            cspgunpowdercraft = math.trunc(csgunpowdercraft)
            csbeancan = int(csexplo1) * 4
            
            #print
            os.system("cls")
            print("[", Fore.CYAN + "Satchel Charge" + Fore.WHITE,"]")
            print("Satchel Charge: ", Fore.GREEN + str(csexplo1) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Sulfur: ",Fore.BLUE + str(csinput) + Fore.WHITE)
            print("Charcoal: ",Fore.BLUE + str(cscharcoal) + Fore.WHITE)
            print("Gunpowder: ",Fore.BLUE + str(csgunpowder) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(csmetalfrags) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(cspgunpowdercraft) + Fore.WHITE)
            print("Beancan craft: ",Fore.MAGENTA + str(csbeancan) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit

        #Craft
        
        if cinput == "2":
            #input
            os.system("cls")
            print("Craft ammount?")
            scinput = input()
            
            #Materials
            scsulfur =int(scinput) * 480
            sccharcoal = int(scinput) * 720
            scgunpowder = int(scinput) * 240
            scmetalfrags = int(scinput) * 80
            scgunpowdercraft = int(scgunpowder) / 10
            scpgunpowdercraft = math.trunc(scgunpowdercraft)
            scbeancan = int(scinput) * 4
            
            #print
            os.system("cls")
            print("[", Fore.CYAN + "Satchel Charge" + Fore.WHITE,"]")
            print("Satchel Charge: ", Fore.GREEN + str(scinput) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Materials" + Fore.WHITE,"]")
            print("Sulfur: ",Fore.BLUE + str(scsulfur) + Fore.WHITE)
            print("Charcoal: ",Fore.BLUE + str(sccharcoal) + Fore.WHITE)
            print("Gunpowder: ",Fore.BLUE + str(scgunpowder) + Fore.WHITE)
            print("Metal fragments: ",Fore.BLUE + str(scmetalfrags) + Fore.WHITE)
            print("")
            print("[", Fore.CYAN + "Crafting" + Fore.WHITE,"]")
            print("Gunpowder craft: ",Fore.MAGENTA + str(scpgunpowdercraft) + Fore.WHITE)
            print("Beancan craft: ",Fore.MAGENTA + str(scbeancan) + Fore.WHITE)
            print("")
            print("[", Fore.RED + "ENTER" + Fore.WHITE, "] Exit")
            rsendinput = input()
            if rsendinput == "":
                start = False
                quit
            else:
                quit
    
    else:
        quit

#end
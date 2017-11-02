import mergeMeli

megMeil = mergeMeli.mergeMeliage()
answer = megMeil.change_airport_to_Prefecture('NRT')
print(answer)
airline =  megMeil.catch_all_airline_airport()
for aline in airline:
    print (aline[0],aline[1])
    departPref = megMeil.change_airport_to_Prefecture(aline[0])
    arrivePref = megMeil.change_airport_to_Prefecture(aline[1])
    departMuni = megMeil.change_airport_to_Municipality(aline[0])
    arriveMuni = megMeil.change_airport_to_Municipality(aline[1])
    if(departPref!='error' and arrivePref!='error'):
        meliage = megMeil.find_the_Meliage(departPref,arrivePref)
        print(meliage)
        if(meliage == 0):
            meliage = megMeil.find_the_Meliage(departPref,arriveMuni)
            print(meliage)
            if(meliage == 0):
                meliage = megMeil.find_the_Meliage(arrivePref,departMuni)
                print(meliage)
                if(meliage == 0):
                    meliage = megMeil.find_the_Meliage(departMuni,arriveMuni)
                    print(meliage)
        megMeil.upload_the_Meliage(meliage,aline[0],aline[1])    
    else:
        print("error")
    
    print(" ")

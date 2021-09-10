print ("sollicitatie roy otten")
print ("we gaan je een paar vragen stellen om erachter te komen of jij geschikt bent voor deze baan")

vraag1 = input ("heb jij praktijkervaring met dieren-dresuur?")
vraag2 = input ("ben jij in bezit van een MBO-4 ondernemen?")
vraag3 = input ("ben jij in bezit van een geldig vrachtwagen bewijs?")
vraag4 = input ("ben jij in bezit van een hoge hoed?")
vraag5 = input ("ben jij een man?")
if vraag5 == ("no"):
    vraagvrouw = input ("ben jij een vrouw?")
    if vraagvrouw == ("yes"):
        vraagroodhaar = input ("beschik je over lang rood krullend haar?") 
    if vraagroodhaar == ("yes"):
        print ("oke")
if vraag5 ==("yes"):
    vraagsnor = input("Heb je een snor?")




vraag6 = input ("wat is uw lengte?")
vraag7 = input ("wat is uw gewicht?")
vraag8 = input ("heb jij een certificaat 'overleven met gevaarlijk personeel'?")
vraag9 = input ("ben je in bezit van een hond?")
vraag10 = input ("ben je heterosexueel?") 
vraag11 = input ("heb je lange schoenen?")
vraag12 = input ("heb je een schildpad?") 


if (vraag1 == ("yes") and vraag2 == ("yes") and vraag3 == ("yes") and vraag5 == ("yes") and vraag6 > 150
 and vraag7 > 90 and vraag8 == ("yes") and vraag9 == ("yes")):
    print ("je bent aangenomen!!!!") 
else:
    print ("je bent helaas niet aangenomen") 









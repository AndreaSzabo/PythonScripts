# Ez a program azert keszult, mert a telefonom kulonbozo formatumba mentette el a kepeimet ebbol adodoan valahogy duplikatumok is lettek
# Namost ez a progi a kovetkezo formatumot 2016-04-02 13.00.07 atalakitja ilyenne: 20160402_130007
import os
import sys
from os import rename

if len(sys.argv) != 2:
    print "Juj, nincs parameter, adj meg egy mappat."
    exit()

input_folder = sys.argv[1]

if os.path.exists(input_folder):
    print " Letezik " + input_folder + " nevu mappa."
else:
    print " Nem letezik " + input_folder + " nevu mappa."
#
# Do stg
#

patterns = ['-', 'jpeg', 'jpg', 'mp4']

for dirName, subdirList, fileList in os.walk(input_folder):
    print('\nFound directory: %s' % dirName + '\n')
    for fname in fileList:
        #print('\t%s' % fname)

        if any(x in fname for x in patterns):
            if fname.count(".") == 3: #Ketto pontot lecserelunk az idoformatumban
                newName = fname.replace("-", "").replace(" ", "_").replace(".", "", 2)
                # Atnevezes:
                oldFilePath = os.path.join(input_folder, fname)
                newFilePath = os.path.join(input_folder, newName)
                if os.path.exists(newFilePath):
                    print "\t Nem tudtam felulirni, mert letezik: " + newFilePath
                else:
                    rename(oldFilePath, newFilePath)
                
                print "\t" + fname + " --> " + newName

            else: #Fajlnev kovetelmenyei nem felelnek meg
                print "\t!!!Nem tudtam atnevezni: " + fname

        else:
            print "\t" + fname + " maradt"	
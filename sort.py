import os, shutil
from datetime import date
from random import randint

#### Constants

# Input Folder 
input_f = "C:/Users/CezarStefan/Videos/Captures/" ###TODO Replace this with your XboxDVR location ( e.g. "C:/Users/*USERNAME*/Videos/Captures/" )
# Output Folder
output_f = "C:/Users/CezarStefan/Desktop/SortedXboxDVR/" ###TODO Replace this with a desired output folder

#### The main program

# We loop through every file in the input folder
for file in os.listdir(input_f):

    # We store the origin full path of the file
    origin_fullpath = input_f+file

    # We need to establish the name of the game/category
    # We check if the name of the file contains '(' so we can remove it (and everything after it) and only keep the actual name. 
    # Reason: if there is more than one file for the same game/category, the filenames end with a number between '()'
    if '(' in file:
        game_f = output_f + file.split('(')[0][:-1] + '/'
    else:
        game_f = output_f + file[:-4] + '/'

    # We save the extension in order to easily rename the file
    ext = file[-4:]

    #  We check if a folder already exists for the game and if not, we create it
    if not os.path.exists(game_f):
        os.makedirs(game_f)

    # We establish the destination : path + name + date + extension
    destin_fullpath = game_f + file[:-4] + '-' + str(date.today()) + ext 

    # We make sure the full path is unique, if not we add a random int between 1000 and 9999
    while os.path.exists(destin_fullpath):
        destin_fullpath = game_f + file[:-4] + '-' + str(date.today()) + '-' + str(randint(1000,9999)) + ext

    # We move the actual files.
    shutil.move(origin_fullpath,destin_fullpath)
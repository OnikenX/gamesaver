import json
import io
import os
import filecmp
from gameslist import Gameslist
from backuper import Backuperficker

path_to_saves_folder = "./"

mylist = Gameslist(path_to_saves_folder)



#for item in mylist.get():
#    print(item["name"])
#
#try:
#    print(os.environ["GAMESAVER_SAVES_PATH"])
#except(KeyError):
#    print("the variable does not exist, using default current directory instead ("+os.environ["PWD"]+")")
#
#
#
#

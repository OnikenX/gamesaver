import filecmp
from gameslist import Gameslist

import os
import pyinotify


def pathexists(path):
    return os.path.isdir(path)


def getfullpath(path):
    if(path[0] == '~'):
            return path.replace('~', os.environ["HOME"], 1)

class Backuperficker:
    def __init__(self, gameslist):
        for game in gameslist:
            if pathexists(getfullpath(game["path"])):
                self.listexisting.add(game)

    def get(self):
        return self.listexisting
        
            

    
        
            

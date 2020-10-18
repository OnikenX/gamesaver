import json
import io
import os
import filecmp



def expandedpath(path):
    "uses echo from system to find the path with variables for cases like user"
    return os.path.expanduser(os.path.expandvars(path))

def pathexists(path):
    "sees if the folder exists"
    return os.path.isdir(path)




class Backuper:
    "class responsable for finding the dirs and copying stuff"
    def __init__(self, gameslist):
        self.gameslist = gameslist
        self.listexisting = []
        self.refreshfolders()

    def getpath(self, game):
        if self.gameslist.getconfig().useechodpath == True:
            return expandedpath(game["PATH"])
        else:
            return game["PATH"]

    def refreshfolders(self):
        "reviews the directories to see if they exist in the disk"
        self.listexisting.clear()
        for game in self.gameslist.get():
            echodpath = expandedpath["PATH"])
            print("Game: "+game["codename"]+"; path: " + echodpath)
            try:

                if pathexists(echodpath):
                    self.listexisting.append(game)
                    game["PATH"] = echodpath
                    print("Added: " + game)
            except TypeError:
                print("Game " + game["codename"] +
                      " does not have an acceptable path (\""+game["PATH"]+"\")")
                pass

    def get(self):
        """Gets the list of games that are found"""
        return self.listexisting



class ConfigManager:
    # starts the function saving the path and loading the list
    def __init__(self):
        gamesaverFolder = 'GameSaver'
        configVar ='XDG_CONFIG_HOME'
        if configVar in os.environ:
            self.configfolder = os.path.join(os.environ[configVar], gamesaverFolder)
        else:
            self.configfolder = os.path.join(os.path.join('~/.config/', gamesaverFolder))
        print("Config folder in {self.configfolder}")
        self.loadconfig()

    def getconfig(self):
        return self.globalconfig.config

    
    def loadconfig(self):
        "loads the list from games.json file"
        with open(os.path.join(self.configfolder,"config.json"), "r") as globalconfig:
            self.globalconfig = json.load(globalconfig)


    # def loadconfig(self):
    #     "loads the list from games.json file"
    #     with open(self.saves_folder+"games.json", "r") as gms:
    #         self.globalconfig = json.load(gms)
    #         self.list = self.globalconfig["games"]

    # saves the list to the games.json file
    def savelist(self):
        with open(self.saves_folder+"games.json", "w") as gms:
            json.dump(self.list, gms)

    # adds a new element to the list

    def add(self, codename, path, name="", notes=""):
        if (name == ""):
            name = codename
        self.list.add(
            {"codename": codename,
             "path": path,
             "name": name,
             "notes": notes}
        )

    # returns a copy of the list
    def get(self):
        return self.list.copy()

    # returns a copy of the game if exists
    def getgamebycodename(self, codename):
        for game in self.list:
            if (game["codename"] == codename):
                return game.copy()

    # vai buscar o fullpath(substituindo ~ por $HOME, se existir no inicio) utilizando como argumento o codename
    def getgamepath(self, codename):
        return self.getgamebycodename(codename)["path"]

    

class Gamesaver():
    
    def __init__(self):
        self.configmanager = ConfigManager
        self.backuper = Backuper
        
    # path_to_saves_folder = "./"
    # mylist = ConfigManager(path_to_saves_folder)
    # backuper = Backuper(mylist)
    # print("Added files: ")
    # for item in backuper.get():
    # print(item)

if __name__ == "__main__":
    print(os.path.join(os.path)
    
    gamesaver = Gamesaver()
    
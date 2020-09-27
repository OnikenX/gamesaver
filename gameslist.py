import json


class Gameslist:

    # starts the function saving the path and loading the list
    def __init__(self, path_to_saves_folder):
        self.saves_folder = path_to_saves_folder
        self.loadlist()

    # loads the list from games.json file
    def loadlist(self):
        with open(self.saves_folder+"games.json", "r") as gms:
            self.list = json.load(gms)

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

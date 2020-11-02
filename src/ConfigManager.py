import json

from utils import *


class ConfigManager:

    @staticmethod
    def get_config_path():
        """gera o caminho para o config file"""
        gamesaver_config_folder_name = 'GameSaver'
        config_var = 'XDG_CONFIG_HOME'
        if config_var in os.environ:
            return os.path.join(os.environ[config_var], gamesaver_config_folder_name)
        else:
            return os.path.join(os.path.join(expandedpath('~/.config/'), gamesaver_config_folder_name))

    @staticmethod
    def create_config(backup_folder: str):
        """Creates a config file
        needs the location of the backup folder"""
        try:
            os.makedirs(backup_folder)
        except FileExistsError:
            pass
        global_config = {"backup_folder": backup_folder}
        with open(os.path.join(ConfigManager.get_config_path(), "config.json"), "w") as global_config_file:
            json.dump(global_config, global_config_file)

    def __init__(self):
        """"starts the class saving the path and loading, if possible, of the configs, if not it will get a function
        to make what it needs"""

        self.config_path = self.get_config_path()

        # creates the folder to save the config file
        try:
            os.makedirs(self.config_path)
        except FileExistsError:
            pass
        self.config_file = os.path.join(self.config_path, "config.json")
        self.global_config = {"backup_folder": ""}
        # List of games that saves where
        self.games_list = []
        if not (os.path.exists(self.config_file)):
            raise FileNotFoundError(
                "Config file does not exist. "
                "Call the create_config method of ConfigManager with the location of the backup folder as the argument "
                "to create a config.")
        else:
            self.load_config()

    def load_config(self):
        """loads the local config"""
        with open(os.path.join(self.config_path, "config.json"), "r") as global_config_file:
            self.global_config = json.load(global_config_file)
        self.load_list()

    def save_config(self):
        """saves the local config"""
        with open(os.path.join(self.config_path, "config.json"), "w") as global_config_file:
            json.dump(self.global_config, global_config_file)

    def list_file_name(self):
        return os.path.join(self.global_config["backup_folder"], "games.json")

    def load_list(self):
        """loads the games list"""
        if not (os.path.exists(self.list_file_name())):
            self.games_list = []
            self.save_list()
        else:
            with open(os.path.join(self.global_config["backup_folder"], self.list_file_name()), 'r') as list_file:
                self.games_list = json.load(list_file)

    def save_list(self):
        """saves the games list"""
        with open(self.list_file_name(), "w") as gms:
            json.dump(self.games_list, gms)

    def add_game(self, codename: str, path: str, name="", notes="") -> bool:
        """added a game to the list. Returns False if the game exists else True"""
        for game in self.games_list:
            if (codename == game["codename"]) or (path == game["path"]):
                return False

        if name == "":
            name = codename

        self.games_list.append(
            {"codename": codename,
             "path": path,
             "name": name,
             "notes": notes}
        )
        self.save_list()
        return True

    def get_game_by_code_name(self, codename):
        """returns a copy of the game if exists else returns None"""
        for game in self.games_list:
            if game["codename"] == codename:
                return game.copy()
        return None

    def get_game_path(self, codename: str):
        """gets the fullpath of the save of the game by codename"""
        return self.get_game_by_code_name(codename)["path"]

    def get_games_list(self):
        """Returns a copy of the games_list"""
        return self.games_list.copy()

    def delete_game(self, codename: str) -> bool:
        """deletes a game from the list. Returns True if deleted"""
        for game in self.games_list:
            if game['codename'] == codename:
                self.games_list.remove(game)
                self.save_list()
                return True
        return False

#
# def print_games(config):
#     string = ""
#     for game in config.get_games_list():
#         string += game['name'] + '; '
#     print(string)
#
#
# if __name__ == '__main__':
#     try:
#         config = ConfigManager()
#     except ConfigNotCreated:
#         ConfigManager.create_config("/home/onikenx/Projects/testing/GameSaverBACKUPS")
#         config = ConfigManager()
#

from utils import pathexists, expandedpath
import os


class Backuper:
    """class responsible for syncing contents and managing branches"""
    @staticmethod
    def sync_saves(games_list: list, backup_folder: str) -> int:
        """this method receives a games_list of the games that need to be sync and the folder where the backups should go. Returns the numbers of folder found and synced with sucess. """
        for game in games_list:
            if os.path.isdir(game['path']):
                





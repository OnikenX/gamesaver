import ConfigManager
import Backuper

if __name__ == '__main__':
    # starts with reading the config file, if it does not find it in the first place the constructor will rase an
    # exception
    try:
        config = ConfigManager
    except FileNotFoundError:
        # when treating the exception we create the config folder and recreat the config class
        ConfigManager.create_config("/home/onikenx/Projects/testing/GameSaverBACKUPS")
        config = ConfigManager
    # when that is done the the program goes to each file and syncs them up

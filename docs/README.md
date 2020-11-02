# GameSaver Documentation

This is the documentation for the gamesaver library, with the steps for creating a interface or accessing to its classes.

## Classes

 - **GameSaver** - is the main class for accessing the library, wraps the others classes in a simple way
 
 - **ConfigManager** - reads and treats the configs, folder locations and the list/database of games
 
 - **Backuper** - is responsible for making the copies of files and managing the backups
 
 ## Usability
 
 1. Starting the GameSaver class 
    
     - Create the class gamesaver, this will create the other ones if the all the configs are created and will load everything automatically
        - if there was no configs in the system, then the ` ()` will return `False`, and needs to receive a path for the backups folder in the method `create_config(backup_folder)`, after that it will 
 

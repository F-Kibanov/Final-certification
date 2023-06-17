from Program.Database.DB_config import config_db_init
from Program.Models.camels import Camels
from Program.Models.cats import Cats
from Program.Models.dogs import Dogs
from Program.Models.donkeys import Donkeys
from Program.Models.hamsters import Hamsters
from Program.Models.horses import Horses
from Program.View.Menu import ls_menu

if __name__ == '__main__':
    print('\nPets accounting started')

    config = config_db_init()
    ls_menu(config)

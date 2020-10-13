#!/usr/bin/env python3

from scraper import __version__


class Banner(object):
    def __init__(self):
        self.version = __version__

    def print_banner(self):
        print(
            f"""
    __    _       __            ___          
   / /   (_)___  / /_____  ____/ (_)___      
  / /   / / __ \/ //_/ _ \/ __  / / __ \     
 / /___/ / / / / ,< /  __/ /_/ / / / / /     
/_____/_/_/ /_/_/|_|\___/\__,_/_/_/ /_/      
  / ___/______________ _____  ___  _____     
  \__ \/ ___/ ___/ __ `/ __ \/ _ \/ ___/     
 ___/ / /__/ /  / /_/ / /_/ /  __/ /         
/____/\___/_/   \__,_/ .___/\___/_/          
                    /_/   v{self.version}

            """
        )


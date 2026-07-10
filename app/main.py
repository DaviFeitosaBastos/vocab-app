from rich import print
from rich.prompt import Prompt
from ui import main_menu, loading_screen, clear, return_option
import logging
from log_utils import get_logger

from time import sleep

log = get_logger(__name__)

def main():
    # loading_screen(0.5)
    while True:
        main_menu()
        try:    
            choose = int(Prompt.ask("[bold blue]Choose here"))
            match choose:
                case 1:
                    ...
                case 2:
                    ...
                case 3:
                    ...
                case 0:
                    ...
                case _:
                    print("[red] Invalid option!")
                    sleep(0.9)
                    continue

        except ValueError as e:
            log.error(f"Error {e} | Try a valid options instead!")
            sleep(1)

        

if __name__ == "__main__":
    main()
    
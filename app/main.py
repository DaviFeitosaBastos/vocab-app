from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from ui import main_menu, loading_screen, clear, return_option, search_menu
from utils import search_word, load_dictionary, load_progress, get_daily_word, save_progress, get_unseen, mark_as_seen
from log_utils import get_logger
from time import sleep

log = get_logger(__name__)

def main():
    load_files = load_progress("progress.json")
    load_dict = load_dictionary("../data/processed/dictionary.json")

    # loading_screen(0.1)

    while True:
        main_menu()
        try:    
            choose = int(Prompt.ask("[bold blue]Choose here"))
            match choose:
                case 1:
                    unseen = get_unseen(load_dict, load_files)
                    daily_word = get_daily_word(unseen)
                    save_progress(mark_as_seen(daily_word), load_files, "progress.json")
                    clear()
                    print(Panel(f"[bold blue]The word today is[/]\n"f"[bold cyan]★ [bold blue]{daily_word[0]['Word']}[/]\n★ [bold blue]Meaning[/] 🢚 {daily_word[0]['Meanings']}[/]", title="[cyan]Daily word", style="cyan",))
                    Prompt.ask("[bold blue]Press enter to return")

                case 2:
                    clear()
                    print(Panel(f"", title="[cyan]★ Progress ★", style="cyan"))
                    Prompt.ask("")

                case 3:
                    search_menu()
                    word = Prompt.ask(f"[bold blue]Type the word").lower()
                    result = search_word(load_dict, word)
                    if result:
                        clear()
                        print(Panel(f"[bold cyan]{result['Word']}[/]\n"f"[italic]{result['Meanings'][0]}[/] — {result['Meanings'][1]}", title="[cyan]Word", style="cyan"))
                        Prompt.ask("[bold blue]Press enter to return to menu")
                    else:
                        clear()
                        print(Panel(f"[cyan]The word [red]|{word}|[/] was not found[/]", title="[red]Word not found!",style="red"))
                        Prompt.ask("[bold blue]Press enter to return to menu")

                case 4:
                    ...

                case 0:
                    print(f"[red]Exitting...")
                    sleep(0.6)
                    clear()
                    exit()

                case _:
                    print("[red] Invalid option!")
                    sleep(0.9)
                    continue

        except ValueError as e:
            log.error(f"Error {e} | Try a valid options instead!")
            sleep(1)

        

if __name__ == "__main__":
    main()
    
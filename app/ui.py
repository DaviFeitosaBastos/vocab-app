from rich import print
import os
from time import sleep
from rich.progress import track
from rich.panel import Panel
import platform
from rich.prompt import Prompt

def clear():
    os.system("clear") if not platform.system() == "windows" else "cls"

def loading_screen(s: float):
    clear()
    for i in track(range(15), description="[blue]Downloading dictionary..."):
        sleep(s)  # Simulate work being done
    clear()
    for i in track(range(9), description="[green]Setting up..."):
        sleep(s)
    clear()
    for i in track(range(3), description="[green]Loading app..."):
        sleep(s)
    
def main_menu(): 
    clear()
    print(Panel("[bold blue]Choose one of those sections![/]\n"
    "[bold blue]1[/] - Get a random word\n"
    "[bold blue]2[/] - Show all progress\n"
    "[bold blue]3[/] - Add a new word in the dictionary\n"
    "[red]0 - Exit", title="[cyan]Vocabulary app", subtitle="[cyan]Enjoy", style="cyan"))

def return_option():
    clear()
    print(Panel("[bold blue]Would you like to return? Press [Y]es and [N]ot![/]", title="[cyan]Returning menu", subtitle="[cyan]↓ Prompt ↓", style="cyan"))
    answer = Prompt.ask("[bold blue]Type here")

    
# loading_screen(0.2)
# main_menu()


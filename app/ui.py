from rich import print
import os
from rich.panel import Panel
import platform
from rich.prompt import Prompt
from rich.table import Table


def clear():
    os.system("clear") if not platform.system() == "windows" else "cls"


def main_menu():
    clear()
    print(
        Panel(
            "[bold blue]Choose one of those sections![/]\n"
            "[bold blue]1[/] - Get a random word\n"
            "[bold blue]2[/] - Show all progress\n"
            "[bold blue]3[/] - Search a Word\n"
            "[red]0 - Exit",
            title="[cyan]Vocabulary app",
            subtitle="[cyan]Enjoy",
            style="cyan",
        )
    )


def return_option():
    clear()
    print(
        Panel(
            "[bold blue]Would you like to return? Press [Y]es and [N]ot![/]",
            title="[cyan]Returning menu",
            subtitle="[cyan]↓ Prompt ↓",
            style="cyan",
        )
    )
    answer = Prompt.ask("[bold blue]Type here")


def search_menu():
    clear()
    print(
        Panel(
            "[bold blue]Type what word would you like to see?[/]",
            title="[cyan]Searching menu",
            subtitle="[cyan]↓ Word ↓",
            style="cyan",
        )
    )


def build_progress_table(sequence: dict, dict_: dict) -> Table:
    table = Table(show_header=False, box=None, padding=(0, 1))
    for k, v in sequence.items():
        table.add_row(f"[bold cyan]{k}.[/]", str(v))
    return table


# loading_screen(0.2)
# main_menu()

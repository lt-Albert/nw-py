from questionary import Style, prompt
import rich
from rich.panel import Panel

from rich.console import Console

console = Console()


custom_style = Style([("question", "bold cyan"), ("answer", "bold")])

questions = [
    {"type": "select",
      "name": "mode",
        "message": "Server or Client?",
          "choices": ["server", "client"]},
    {"type": "input",
      "name": "host", "message": "Host/IP",
        "default": "0.0.0.0"},
    {"type": "input",
      "name": "port",
        "message": "Port",
          "default": "8080",
            "validate": lambda x: x.isdigit()},
    # Conditional questions based on protocol
]

answers = prompt(questions, style=custom_style)
console.print(Panel(f"[green]Setup confirmed:[/green] {answers}"))
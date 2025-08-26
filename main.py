import sys
from cli import main as cli_main
from gui import main as gui_main

isCLI = "gui" not in sys.argv

if __name__ == "__main__":
    print(f"Starting in {'CLI' if isCLI else 'GUI'} mode")
    cli_main() if isCLI else gui_main()

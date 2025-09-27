import listing_tracker.commands as commands
import sys

if __name__ == "__main__" and len(sys.argv) >= 3:
    command = sys.argv[1]
    match command:
        case "add":
            commands.Add(sys.argv[2:]).exec()
        case "view":
            commands.View(sys.argv[2:]).exec()
        case _:
            raise Exception(f'The command "{command}" is not a valid command.')
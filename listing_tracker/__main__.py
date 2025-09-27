import listing_tracker.commands as commands
import sys

if __name__ == "__main__" and len(sys.argv) >= 2:
    command = sys.argv[1]
    match command:
        case "add":
            commands.Add(sys.argv[2:]).exec()
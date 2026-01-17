import sys
from sentinel.runner import run_pipeline


def main():
    if len(sys.argv) < 2:
        print("Usage: sentinel run")
        sys.exit(1)

    command = sys.argv[1]

    if command == "run":
        run_pipeline()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

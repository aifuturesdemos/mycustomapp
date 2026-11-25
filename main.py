import subprocess
import sys

ALLOWED_COMMANDS = {
    "date": ["date"],
    "uptime": ["uptime"],
    "whoami": ["whoami"],
}


def run_command(command_name: str) -> str:
    if command_name not in ALLOWED_COMMANDS:
        raise ValueError("Unsupported command")

    result = subprocess.run(
        ALLOWED_COMMANDS[command_name],
        capture_output=True,
        text=True,
        check=True,
        shell=False,
    )
    return result.stdout.strip()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <date|uptime|whoami>")
        sys.exit(1)

    try:
        print(run_command(sys.argv[1]))
    except ValueError as exc:
        print(str(exc))
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print(exc.stderr.strip() or "Command failed")
        sys.exit(exc.returncode)

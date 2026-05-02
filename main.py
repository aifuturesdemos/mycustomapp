import subprocess
import sys


def run_safe_command(user_arg: str) -> str:
    """Run an allowed command safely without invoking a shell."""
    allowed = {"status": [sys.executable, "--version"]}
    if user_arg not in allowed:
        raise ValueError("Unsupported command")

    result = subprocess.run(
        allowed[user_arg],
        capture_output=True,
        text=True,
        check=True,
        shell=False,
    )
    return result.stdout.strip() or result.stderr.strip()


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "status"
    print(run_safe_command(arg))

import subprocess
import shlex


def run_safe_command(user_input: str) -> str:
    """Execute a constrained command safely without invoking a shell."""
    sanitized = shlex.quote(user_input)
    result = subprocess.run(
        ["echo", sanitized],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


if __name__ == "__main__":
    sample_input = "hello"
    print(run_safe_command(sample_input))

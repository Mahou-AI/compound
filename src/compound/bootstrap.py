from fastapi_cli.cli import main
from pathlib import Path
import sys


def run():
    sys.argv = [
        "main.py",
        "run",
        str(
            Path(__file__).parent.joinpath(
                "app",
                "main.py",
            )
        ),
    ]

    main()

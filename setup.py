import os
from pathlib import Path


if __name__ == "__main__":
    # get current working dir
    root = Path(os.getcwd())

    # save to .env for future use
    with open(root.joinpath(".env"), "w") as f:
        f.write(f"PROJECT_ROOT={root}")
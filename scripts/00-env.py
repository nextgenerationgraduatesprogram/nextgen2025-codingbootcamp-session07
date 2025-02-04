import os
import sys
from pathlib import Path

if __name__ == "__main__":
    """
    highlight the issues with dynamically adding to `sys.path`
    """
    # # print the current working directory
    # print(os.getcwd())
    # print()

    # # lets import src
    # p = Path("..").resolve().absolute()
    # sys.path.append(str(p))
    
    # # print sys path
    # for p in sys.path:
    #     print(p)

    # from src.datasets import FashionMnist

   
    """
    highlight one approach to avoid this issue; provide an absolute path
    """
    #
    print(os.getcwd())
    root = Path(os.getcwd())
    with open(root.joinpath(".env"), "w") as f:
        f.write(f"PROJECT_ROOT={root}")

    # show we can accerss this in future
    from dotenv import load_dotenv
    load_dotenv(".env")

    #  print environment variables
    for key, val in os.environ.items():
        print(f"{key}: {val}")

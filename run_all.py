import glob
import subprocess
import os

notebooks = glob.glob("*.ipynb")
for nb in notebooks:
    print(f"Executing {nb}...")
    try:
        subprocess.run(
            ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", "--ExecutePreprocessor.timeout=-1", nb],
            check=True
        )
        print(f"Successfully executed {nb}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {nb}: {e}")

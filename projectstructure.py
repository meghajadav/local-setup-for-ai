import os
from pathlib import Path

while True:
    projectname = input("Enter source folder name:")
    if projectname!="":
        break

list_of_files=[
    ".github/workflows/.gitkeep",
    f"{projectname}/__init__.py",
    f"{projectname}/components/data_ingestion.py",
    f"{projectname}/components/data_preprocessing.py",
    f"{projectname}/components/model_loading.py",
    f"{projectname}/components/model_evaluation.py",
    f"{projectname}/pipeline/inference.py",
    f"{projectname}/pipeline/training.py",
    f"{projectname}/exception.py",
    f"{projectname}/logger.py",
    "templates/index.html",
    "static/style.css",
    "notebook/research.ipynb",
    "init_setup.sh",
    "requirements.txt",
    "dockerfile",
    "app.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
    if not os.path.exists(filename):
        with open(filepath,'w') as f:
            pass

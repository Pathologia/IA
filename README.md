# IA

1 / Install Anaconda
https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe

2 / Init projet depuis Anaconda Prompt (N'importe où)
conda create -n pathologia python=3.9

3 / Anaconda Prompt niveau du dépôt git 
conda activate pathologia && pip install -r requirements.txt

4 / Init api kaggle
pip install -q kaggle depuis Anaconda Prompt
Générer Api token (kaggle.json) depuis le setting kaggle
Le copier dans C:\Users\votrenom\.kaggle

5 / Run Script .py


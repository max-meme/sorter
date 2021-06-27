import os

os.system("rm -r ./sorter")
os.system("mkdir sorter")
os.chdir("./sorter")
os.system("wget https://github.com/max-meme/sorter/archive/refs/heads/main.zip")
os.system("unzip sorter-main.zip")
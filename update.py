import os

print("removing dir")
os.system("rm -r ./sorter")
print("making dir")
os.system("mkdir sorter")
print("changing dir")
os.chdir("./sorter")
print("downloading from github")
os.system("wget https://github.com/max-meme/sorter/archive/refs/heads/main.zip")
print("unzipping")
os.system("unzip sorter-main.zip")
print("done")
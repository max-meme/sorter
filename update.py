import os

print("removing dir")
os.system("rm -r ./sorter-main")
print("downloading from github")
os.system("wget https://github.com/max-meme/sorter/archive/refs/heads/main.zip")
print("unzipping")
os.system("unzip main.zip")
print("removing zip")
os.system("rm main.zip")
print("done")
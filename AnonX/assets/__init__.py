import os

thumbs = []

for filename in os.listdir("./Anonx/assets"):
    if filename.endswith("png"):
        thumbs.append(filename[:-4])

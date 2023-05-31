import os

thumbs = []

for filename in os.listdir("./AnonX/assets"):
    if filename.endswith("png"):
        thumbs.append(filename[:-4])

import os

thumbs = []

for filename in os.listdir("./MukeshMusic/assets"):
    if filename.endswith("png"):
        thumbs.append(filename[:-4])

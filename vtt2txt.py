# read test.vtt
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

import os

files = [file for file in os.listdir("vtt") if file.split(".")[0].endswith("_large")]

folder = "./vtt/"
new_folder = "./transcripts/"
for file in files:
    with open(folder + file, "r") as f:
        lines = f.readlines()
    new_file = file.replace(".vtt", ".txt")
    with open(new_folder + new_file, "w") as f:
        for line in lines[1:]:
            if len(line) == 1:
                continue
            if line[0] in numbers:
                continue
            # write line to new file
            f.write(line[:-1] + " ")

# there is a list of text files in ./transcripts/
# read each one and create a list of strings
# feed the strings to top2vec model
# save model

import os
from top2vec import Top2Vec

files = [file for file in os.listdir("./transcripts") if file.endswith(".txt")]

folder = "./transcripts/"

transcripts = []

for file in files:
    with open(folder + file, "r") as f:
        transcript = f.read()
    transcripts.append(file + "!!" + transcript)

model = Top2Vec(documents=transcripts, speed="learn", workers=30)

model.save("./models/transcripts_model_all_file_name")

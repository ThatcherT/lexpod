# load model
# get documents related to api
# each document has the file name as the first part of the string
# get the file names
# each file name has a number in it, the episode number
# compare this to episode numbers already listened to
# if the episode number is not in the list of already listened to, add it to a new list of episodes to listen to
# use the spotify api to add the episodes to the user's library
from top2vec import Top2Vec

model = Top2Vec.load("./models/transcripts_model_all_file_name")

topic_count = model.get_num_topics()

topic_words, word_scores, topic_nums = model.get_topics()

documents, document_scores, document_ids = model.search_documents_by_topic(
    topic_num=0, num_docs=177
)

episode_numbers = [str(int(doc.split("_")[1])) for doc in documents]

# there is a text document for lex_shows I haven't listened to lex_shows.txt
# open the text file

with open("lex_shows.txt", "r") as f:
    lex_shows = f.readlines()

episode_ids = []

for show in lex_shows:
    show_num = show.split(' ')[0]
    if '#' in show_num:
        show_num_clean = show_num.split('#')[1]
        if show_num_clean in episode_numbers:
            episode_id = show.rsplit(',', 1)[1]
            episode_ids.append(episode_id)

with open('lex_shows_to_listen_to.txt', 'w') as f:
    for episode_id in episode_ids:
        f.write(episode_id)

# unlistened_ai_shows = [show for show in lex_shows if '#' in show and show.split(" ")[0].split('#')[1] in episode_numbers]
# print(unlistened_ai_shows)

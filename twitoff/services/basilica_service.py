import basilica

import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

conn = basilica.Connection(BASILICA_API_KEY)

embedding = conn.embed_sentence('hey this is a cool tweet', model="twitter")

tweets = ["this is an example", "heres another fun tweet", "I don't really use twitter"]
embeddings = connection.embed_sentences(tweets, model="twitter")
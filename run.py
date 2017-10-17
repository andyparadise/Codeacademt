import fetch_data

from markov_python.cc_markove import MarkovChain

movie1 = raw_input("Input link to lyrics: ")
movie2 = raw_input("Input link to lyrics: ")
movie3 = raw_input("Input link to lyrics: ")

mc = MarkovChain()

mc.add_string(fetch_data.get_data(movie1, movie2 movie3))

print mc.generate_text()

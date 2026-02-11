#find_longes_word and display len

def find_longest_word(words):
    max_l_word=max(words,key=len)
    print(f"the biggest word is {max_l_word} with a length of {len(max_l_word)}")

words=['How','Art','Thousand','Love','War','Compromise','Unleash','Excited','Jupiter','Kara','Jamal','Cuba','Lagos','Ghana','Real Madrid','Django']
print(find_longest_word(words))
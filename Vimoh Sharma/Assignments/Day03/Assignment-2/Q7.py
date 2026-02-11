# word from a thesaurus having more len than input.
def filter_words(words,ln):
    res=[]
    for word in words:
        if len(word)>ln:
            res.append(word)
    return res

words=['How','Art','Thousand','Love','War','Compromise','Unleash','Excited','Jupiter','Kara','Jamal','Cuba','Lagos','Ghana','Real Madrid','Django']
ln=int(input("Enter the length cutoff of words: "))

print(f"the words which are having length greater than {ln} are: {filter_words(words,ln)}")

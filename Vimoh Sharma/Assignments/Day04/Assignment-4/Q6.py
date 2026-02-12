#count occurence 
text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with
the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms,
including structured, object-oriented and functional programming."""

final_text=text.lower()

for word in final_text:
    print(f"{word} : {final_text.count(word)}")
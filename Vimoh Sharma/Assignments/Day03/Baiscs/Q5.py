#$ Occurrences
str="Hi, $I am the $ Symbol $99.99"
cnt=0
for ch in str:
    if ch=='$':
        cnt+=1
print(f"$ appears in the given string {cnt} times")
def matchWords(words):
    
    counter = 0
    lst = []
    
    for word in words:
        
        if len(word) > 1 and word[0] == word[-1]:
            counter  = counter + 1
            lst.append(word)
            
    print(f"List of words with first and last character same\n(lst)")
    
    return counter

list1 = ["abc", "cfc", "xyz", "aba", "1221", "nahian", "abira"]

count = matchWords(list1)

print(f"Numberr of words having first and last character same : {count}")
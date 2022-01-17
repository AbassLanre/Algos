def mostWordsFound(sentences):
    max =0
    for i in range(len(sentences)):
        if len(sentences[i].split()) > max:
            max = len(sentences[i].split())
    return max
    
    
print(mostWordsFound(['alice and bob love me ll','i think so too', 'this is great man k k k k k ']))
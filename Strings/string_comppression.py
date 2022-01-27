def compress(string):
    index = 0
    compressed = ""
    len_str = len(string)
    while index != len_str:
        count = 1
        while (index < len_str-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(string[index])
        else:
            compressed += str(string[index]) + str(count)
        index = index + 1
    return compressed
       
 
string = "pythooonnnpool"
print(compress(string))


new_string = ""
string = "pythooonnnpool"
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count = count + 1
    else:         
        new_string =  new_string + string[i] + str(count)
        count = 1
new_string = new_string + string[i+1] + str(count)
print(new_string)
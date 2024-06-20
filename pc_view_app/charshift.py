def shift_chars(string : str) -> str:
    new_str = ''
    for i in range(len(string)):
        if i % 2 == 1:
            new_str = new_str + chr(ord(string[i])+i)
        else:
            new_str = new_str + chr(ord(string[i])-i)
    return new_str

        

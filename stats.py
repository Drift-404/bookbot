def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
    

def count_chars(text):
    chars = {}
    for c in text:
        if c.isalpha():
            low = c.lower()
            if low in chars:
                 chars[low] += 1
            else:
                chars[low] = 1

    report(chars)

def sort_on(items):
    return items["num"]


def report(dict):
    list = []
    for i in dict:
        list.append({"name" : i, "num" : dict[i]})
    list.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for i in list:
        print(i["name"] + ":",i["num"])
    print("============= END ===============")
        


def get_words_list(content):
    return content.split()


def build_character_dict(content):
    lower_cased_content = content.lower()
    letters = {}
    for char in lower_cased_content:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

def sort_by(dict):
    return dict["frequency"]

def build_sorted_list(dict):
    list = []
    for k,v in dict.items():
        list.append({"char":k, "frequency":v})

    list.sort(reverse=True, key=sort_by)
    return list
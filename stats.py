def word_count(text_file):
    words = text_file.split()
    count_of_words = len(words)
    
    return count_of_words


def letter_count(text_file):
    text_file = text_file.lower()

    letter_counts = {}
    for letter in text_file:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts



def sort_on(letter_Count: tuple[str,int])-> int:
    return letter_Count[1]



def chars_dict_to_sorted_list(letter_counts:dict[str,int])->list[tuple[str,int]]:
    empty_list = []
    for letter in letter_counts:
        append_this =  (letter,letter_counts[letter])
        empty_list.append(append_this)
    sorted_list = sorted(empty_list,reverse = True,key=sort_on)
    return sorted_list
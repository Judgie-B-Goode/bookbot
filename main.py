char_count = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0,
               "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0,
                 "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
                   "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    file_name = f.name
    num_words = word_count(file_contents)
    letter_dict = letter_count(file_contents)
    sorted_dict = letter_sorter(letter_dict)
    report = make_report(file_name, num_words, sorted_dict)
    print(report)

def word_count(file_contents):
    return len(file_contents.split())

def letter_count(file_contents):
    for letter in file_contents:
        lowered = letter.lower()
        if lowered in char_count:
            char_count[lowered] += 1
    return char_count

def letter_sorter(char_dict):
    char_list = []
    for character, count in char_dict.items():
        character_kv = {"character": character, "count": count}
        char_list.append(character_kv)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]
    
def make_report(file_name, word_count, letter_count):
    report_builder = ""
    header = f"--- Begin report of {file_name} --- \n"
    footer = "--- End report ---"
    report_builder += header
    report_builder += f"{word_count} words found in the document\n\n"
    for counted in letter_count:
        report_builder += (f"The \'{counted["character"]}\' character was found {counted["count"]} times\n")      
    report_builder += footer
    return report_builder

main()
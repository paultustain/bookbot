def main(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    # print(file_contents)
    # count_words(file_contents)
    # count_characters(file_contents)
    produce_report(filepath, file_contents)


def count_words(file):
    word_list = file.split()
    return len(word_list)


def produce_report(filepath, file):
    print(f"--- Begin report of {filepath} ---")
    print(f"{count_words(file)} words found in the document\n")
    for k, v in dict(
            sorted(
                count_characters(file).items(), 
                key=lambda item: item[1],
                reverse=True)).items(): 
        if k.isalpha():
            print(f"{k} appears {v} times.") 
    print("--- End of report ---")


def count_characters(file):
    letter_dictionary = {}
    for c in file:
        if c.lower() in letter_dictionary:
            letter_dictionary[c.lower()] += 1
        else: 
            letter_dictionary[c.lower()] = 1
    return letter_dictionary    

if __name__ == '__main__':
    main("books/frankenstein.txt")
    

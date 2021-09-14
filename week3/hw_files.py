len_file = 0
count_words = 0
filename = "referat.txt"
new_filename = "referat2.txt"
with open(filename, 'r', encoding='utf-8') as read_file:
    for line in read_file:
        len_file += len(line)
        count_words += len(line.split())
        with open(new_filename, 'a', encoding='utf-8') as add_file:
            new_line = line.replace('.', '!')
            add_file.writelines(new_line)
    output_len_file = f"Длинна строки: {len_file}"
    output_count_words = f"Количество слов: {count_words}"
    print(output_len_file)
    print(output_count_words)
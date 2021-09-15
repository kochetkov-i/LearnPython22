filename = "referat.txt"
new_filename = "referat2.txt"

with open(filename, 'r', encoding='utf-8') as original_file:
    content_original_file = original_file.read()

content_new_file = content_original_file.replace('.', '!')

with open(new_filename, 'w', encoding='utf-8') as new_file:
    new_file.write(content_new_file)

len_file = len(content_original_file)
count_words = len(content_original_file.split())

output_len_file = f"Длинна строки: {len_file}"
output_count_words = f"Количество слов: {count_words}"

print(output_len_file)
print(output_count_words)
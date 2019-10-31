# 4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить обратное
# преобразование (используя методы encode и decode).
words = ['разработка', 'администрирование', 'protocol', 'standard',]
words_encode = [word.encode('utf-8', errors='replace') for word in words]
for word in words_encode:
    print(word, f'{type(word)}\n', sep='\n')

words_decode = [word.decode('utf-8', errors='replace') for word in words_encode]
for word in words_decode:
    print(word, f'{type(word)}\n', sep='\n')

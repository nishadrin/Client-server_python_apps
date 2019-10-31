# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без
# преобразования в последовательность кодов (не используя методы encode и
# decode) и определить тип, содержимое и длину соответствующих переменных.
words = [
    'class',
    'function',
    'method',
    ]
words_bytes = [
    b'class',
    b'function',
    b'method',
    ]
for word in words:
    print(word, type(word), sep='\n')
for word in words_bytes:
    print(word, type(word), sep='\n')

word_list = {
    'А': 'Б', 'а': 'б', 'Б': 'В', 'б': 'в', 'В': 'Г', 'в': 'г', 'Г': 'Д', 'г': 'д', 'Д': 'Е', 'д': 'е',
    'Е': 'Ё', 'е': 'ё', 'Ё': 'Ж', 'ё': 'ж', 'Ж': 'З', 'ж': 'з', 'З': 'И', 'з': 'и', 'И': 'Й', 'и': 'й',
    'Й': 'К', 'й': 'к', 'К': 'Л', 'к': 'л', 'Л': 'М', 'л': 'м', 'М': 'Н', 'м': 'н', 'Н': 'О', 'н': 'о',
    'О': 'П', 'о': 'п', 'П': 'Р', 'п': 'р', 'Р': 'С', 'р': 'с', 'С': 'Т', 'с': 'т', 'Т': 'У', 'т': 'у',
    'У': 'Ф', 'у': 'ф', 'Ф': 'Х', 'ф': 'х', 'Х': 'Ц', 'х': 'ц', 'Ц': 'Ч', 'ц': 'ч', 'Ч': 'Ш', 'ч': 'ш',
    'Ш': 'Щ', 'ш': 'щ', 'Щ': 'Ъ', 'щ': 'ъ', 'Ъ': 'Ы', 'ъ': 'ы', 'Ы': 'Ь', 'ы': 'ь', 'Ь': 'Э', 'ь': 'э',
    'Э': 'Ю', 'э': 'ю', 'Ю': 'Я', 'ю': 'я', 'Я': 'A', 'я': 'a', 'A': 'B', 'a': 'b', 'B': 'C', 'b': 'c',
    'C': 'D', 'c': 'd', 'D': 'E', 'd': 'e', 'E': 'F', 'e': 'f', 'F': 'G', 'f': 'g', 'G': 'H', 'g': 'h',
    'H': 'I', 'h': 'i', 'I': 'J', 'i': 'j', 'J': 'K', 'j': 'k', 'K': 'L', 'k': 'l', 'L': 'M', 'l': 'm',
    'M': 'N', 'm': 'n', 'N': 'O', 'n': 'o', 'O': 'P', 'o': 'p', 'P': 'Q', 'p': 'q', 'Q': 'R', 'q': 'r',
    'R': 'S', 'r': 's', 'S': 'T', 's': 't', 'T': 'U', 't': 'u', 'U': 'V', 'u': 'v', 'V': 'W', 'v': 'w',
    'W': 'X', 'w': 'x', 'X': 'Y', 'x': 'y', 'Y': 'Z', 'y': 'z', 'Z': '1', 'z': '2', '1': '3', '2': '4',
    '3': '5', '4': '6', '5': '7', '6': '8', '7': '9', '8': '(', '9': ')', '(': '!', ')': '?', '!': '_',
    '?': '-', '_': '=', '-': '+', '=': '*', '+': '/', '*': ':', '/': '.', ':': ',', '.': ' ', ',': '"',
    ' ':'А', '"':'а'
}
word_list_desh = {
    'А': ' ', 'а': '"', 'Б': 'А', 'б': 'а', 'В': 'Б', 'в': 'б', 'Г': 'В', 'г': 'в', 'Д': 'Г', 'д': 'г', 'Е': 'Д',
    'е': 'д', 'Ё': 'Е', 'ё': 'е', 'Ж': 'Ё', 'ж': 'ё', 'З': 'Ж', 'з': 'ж', 'И': 'З', 'и': 'з', 'Й': 'И', 'й': 'и',
    'К': 'Й', 'к': 'й', 'Л': 'К', 'л': 'к', 'М': 'Л', 'м': 'л', 'Н': 'М', 'н': 'м', 'О': 'Н', 'о': 'н', 'П': 'О',
    'п': 'о', 'Р': 'П', 'р': 'п', 'С': 'Р', 'с': 'р', 'Т': 'С', 'т': 'с', 'У': 'Т', 'у': 'т', 'Ф': 'У', 'ф': 'у',
    'Х': 'Ф', 'х': 'ф', 'Ц': 'Х', 'ц': 'х', 'Ч': 'Ц', 'ч': 'ц', 'Ш': 'Ч', 'ш': 'ч', 'Щ': 'Ш', 'щ': 'ш', 'Ъ': 'Щ',
    'ъ': 'щ', 'Ы': 'Ъ', 'ы': 'ъ', 'Ь': 'Ы', 'ь': 'ы', 'Э': 'Ь', 'э': 'ь', 'Ю': 'Э', 'ю': 'э', 'Я': 'Ю', 'я': 'ю',
    'A': 'Я', 'a': 'я', 'B': 'A', 'b': 'a', 'C': 'B', 'c': 'b', 'D': 'C', 'd': 'c', 'E': 'D', 'e': 'd', 'F': 'E',
    'f': 'e', 'G': 'F', 'g': 'f', 'H': 'G', 'h': 'g', 'I': 'H', 'i': 'h', 'J': 'I', 'j': 'i', 'K': 'J', 'k': 'j',
    'L': 'K', 'l': 'k', 'M': 'L', 'm': 'l', 'N': 'M', 'n': 'm', 'O': 'N', 'o': 'n', 'P': 'O', 'p': 'o', 'Q': 'P',
    'q': 'p', 'R': 'Q', 'r': 'q', 'S': 'R', 's': 'r', 'T': 'S', 't': 's', 'U': 'T', 'u': 't', 'V': 'U', 'v': 'u',
    'W': 'V', 'w': 'v', 'X': 'W', 'x': 'w', 'Y': 'X', 'y': 'x', 'Z': 'Y', 'z': 'y', '1': 'Z', '2': 'z', '3': '1',
    '4': '2', '5': '3', '6': '4', '7': '5', '8': '6', '9': '7', '(': '8', ')': '9', '!': '(', '?': ')', '_': '!',
    '-': '?', '=': '_', '+': '-', '*': '=', '/': '+', ':': '*', '.': '/', ',': ':', ' ': '.', '"': ','
}
fact = True
word = []
end_list = []
k = 0

while fact:
    word.reverse()
    print(''.join(word))
    word.clear()
    k = 0
    move = input(f'\nрежим код/декод. Стоп слово "стоп"\n')      #выбор режима работы
    try:
        if move == "код" or move == "code":
            cout = input(f"слово для кодировки.\n")         #Кодировка первым режимом
            for i in range(len(cout)):
                wl = word_list[cout[k]]
                word += wl
                k += 1
        elif move == "декод" or move == "decode":
            cout = input(f"слово для декодировки.\n")        #кодировка вторым режимом
            for i in range(len(cout)):
                wl = word_list_desh[cout[k]]
                word += wl
                k += 1
        elif move == "стоп" or move == "stop":
            fact = False
        else:
            print("неверное значение")
    except KeyError:
        print("Такого ключа нет в списке :(\n Рекомендуем вводить текст в ручную")
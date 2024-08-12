# Произвольное число параметров

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower() in root_word.lower() or root_word.lower() in i.lower():
            same_words.append(i)
            return other_words


result1 = single_root_words('rich', 'RichiEst', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Mable', 'Able', 'Disable', 'Bagel')
print(result2)

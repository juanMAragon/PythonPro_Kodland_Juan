# Questo frammento ci permette di leggere l'intero file di testo
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()
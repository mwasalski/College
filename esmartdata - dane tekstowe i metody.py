text = 'witaj na kursie python. python jest wspaniały'

print(text)

print(dir(text))
help(str.count)
#
text.capitalize() #pierwsze słowo z dużej
print(text)
text.title() #każde słowo z dużej
print(text)
text.count('python')#liczy ile razy występuje dane słowo w tekście
text.startswith('kurs')#s[rawdza, czy tekst startuje z danym wyrazem
'python'.startswith('py')#sprawdza, czy dane słowo zaczyna się od 'py'
text.endswith('wspaniały')#analogicznie jw.

text.find('python') #zwraca numer indeksu, od którego zaczyna się dane słowo
text[text.find('Python');] #wycinan od 16 wiersza do końca

hashtags = '#sport#gym'
idx = hashtags.find('#') # idx = index
hashtags[:idx]

'pawel'.isalnum() #czy są znakami alfanumerycznymi
'pawel14 '.isalnum() #dostaniemy fałsz, bo spacja nie jest znakiem alfanumerycznym

'34132'.isdigit() #czy cyfry T/F

'python'.islower()
'PytHON'.isupper()

'#'.join(['python', '3.7'])

#łączenie tekstów



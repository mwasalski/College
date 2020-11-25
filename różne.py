# %% - kernel = jądra - zapisuje się w nim wszystkie zmienne

a = 10
print(a)

# %%
print('\tPython') ## zrobienie akapitu

print(dir(e))
# %%
print('c:path\\to\something\new') ## w takim przypadku dodać kolejny \

print(r'c:path\to\something\new') ## r= raw text

# %%
import os
os.getcwd()

# %% bardziej zaawansowane printowanie

print("""
      instrukcja uruchamiania pliku python.exe:
          
          --file [nazwa pliku]
          zapisuj output do pliku
          
          --quiet 
          wycisza logi w konsoli
          
          koniec naszej instrukcji
""")

# %%

saldo = 40 
saldo =  saldo + 30 ## można to zapisać jako saldo += 30 albo -=30

print (saldo)

# %%

lokata = 1000
## czynnik akumulacyjny - po przemnożenie przez lokatę da nam wartosć przyszłą 

czynnik_akumulacyjny  = 1 + 0.04

lokata_po_roku = lokata * czynnik_akumulacyjny
print('Wartość lokaty po roku:', lokata_po_roku)

# %%

pixel = 150
pixel /= 255

print (pixel)


# %% 
help('/=')
# %%' potęgowanie 
base = 2
base **= 5
print (base)

# %% dzielenie modulo
x = 103 
x=  x % 10
print (x)

# %% przypisanie danych tekstowych 

imie = 'p '
nazwisko = 'w'
nazwa = imie + nazwisko
print(nazwa)

# %%
name = 'python'
version = '3.7'

# %% ćwiczenie nr 3
kwota_poczatkowa = 1000
stopa_procentowa = 0.05
okres_trwania = 2

print(kwota_poczatkowa*(1 + stopa_procentowa)**okres_trwania)


# %% funkcja 

  ## def roll_dice(num):
       # return random.randint(1, num)
#print(def)
# %%
a = ['python', '3,7', 4, 3.7]
'#'.join(a)
# %%

print('Mateusz jest ekstra')
# %%
'#good#time#mood'.replace('#', "Mateuosz")

#%%
text = 'witaj na kursie python. python jest wspaniały'

print(text)

print(dir(text))
help(str.count)
# %%
text.capitalize() #pierwsze słowo z dużej
print(text)
# %%
text.title() #każde słowo z dużej
print(text)
# %%
text.count('python')#liczy ile razy występuje dane słowo w tekście
# %%
text.startswith('kurs')#sprawdza, czy tekst startuje z danym wyrazem
# %%
'python'.startswith('py')#sprawdza, czy dane słowo zaczyna się od 'py'
# %%
text.endswith('wspaniały')#analogicznie jw.
# %%
text.find('python') #zwraca numer indeksu, od którego zaczyna się dane słowo
# %%
text[text.find('Python'):] #wycinan od 16 wiersza do końca
# %%
hashtags = '#sport#gym'
# %%
idx = hashtags.find('#') # idx = index
# %%
hashtags[:idx]
# %%
'pawel'.isalnum() #czy są znakami alfanumerycznymi
# %%
'pawel14 '.isalnum() #dostaniemy fałsz, bo spacja nie jest znakiem alfanumerycznym
# %%
'34132'.isdigit() #czy cyfry T/F
# %%
'python'.islower()
# %%
'PytHON'.isupper()
# %%
'#'.join(['python', '3.7'])
#łączenie tekstów, tekst który chcemy dodać nie wejdzie na początek, 
#trzeba o tym pamiętać
'#'.join(['python', '4'])
# %%
'#goodtime'.replace('#', "this is ")

# %%
'    python     '.strip()# wycina wszystkie spacje
'    python     '.lstrip()# wycina wszystkie spacje po lewej
'    python     '.rstrip()# wycina wszystkie spacje po prawej
# %%
'1,2,3,4,5'.split(',')
'python java c spark'.split() #tworzy listę
'#gym#fit'.split('#')#stworzy listę. którą rozdzieli w miejscu danego znaku

# %%
'12'.zfill(5)   #wypełnia wartośći odpowiednią liczbą zer, na początku wyrażenia

dir(str)

# %%
result = '#'.join(['sport', 'python', 'free', 'time'])

print(result)

# %%
x = '123,785,45,5'

print(x.split(','))

# %%   Zbiory - zbiór to wartości, które nie są zduplikowane, unikalne
empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs= {'python', 'java', 'sql'}
print(len(techs)) #zwraca długość, w tym przypadku, zbioru
set('python')

# %%
techs.add('sa')#dodaje do zbioru konkretną wartość
techs.remove('sa') #usuwa konkretną wartość ze zbioru

techs.pop() #usuwa losowo
techs.clear()# czyści cały zbiór

# %%
AB = {1, 2, 3, 4, 5, 6, 7}
BC = {5, 6, 7, 8, 9}
CD = {5, 6}

CD.issubset(AB)#sprawdzanie, czy CD zawiera się w zbiorze AB
AB.issuperset(CD)#sprawdza, czy AB jest nad zbiorem CD
CD.issubset({5,7})#sprawdzanie, czy CD zawiera się w zbiorze 5, 7

#nadzbiór zbioru - zawiera w sobie wszsystko

# %%
AB.union(BC) #printuje wszystkie unikalne wartości z obydwu zbiorów
AB.intersection(BC) #wartości na przecięciu
AB.symmetric_difference(BC) #te elementy, które są tylko w AB i BC, a później
# łączy 

EE = AB.copy()

# %% Tuple - uporządkowana struktura, której nie można zmieniać
# definiujemy za pomocą nawiasów okrągłych
empty_tuple = tuple()
print(empty_tuple)
# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)
#elementów tupli nie można zmienić
amazon[0]

# %%
data = (amazon, google)
# ta tupla będzie długości, ale każda wartość będzie kolejną tuplą dł 4
# %%
student = ('Mateusz', 'Wąsalski', 'Data Science')
print(Student_a)

# %% przypisywanie wartości - bardziej złożony sposób
imie_studenta = 'Mateusz'
nazwisko_studenta = 'Wąsalski'

# %% przypisywanie wartości - prostszy sposób

imie_studenta, nazwisko_studenta = ('Mateusz', 'Wąsalski')

# %% tworzenie zmiennych na podstawie tupli

company_name, country, sector, rank = amazon

# %% 
country_google = google[1]

# %% kolejny sposób definiowania tupli
stocks = 'amazon', 'apple', 'ibm'

print(type(stocks))

# %%
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
# %% zagnieżdżanie tupli 
nested = 'Europa', 'Polska', ('Warszawa', 'Kraków')

print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c

print(a, b)

# %% to, co wyżej dzięki tupli

x , y = 10, 15
x , y = y, x
print(x, y)

# %% Listy

empty_list=list()
print(empty_list)

# %% ista techs + zamiana pierwszej wartości na python 3.7

techs = ['python', 'java', 'sql']
techs[0] = 'python 3.7'
print(techs)

# %% lista z numerami, nie dawać w nawias, to program odczyta jako tekst
numbers = [ 3, 5, 6, 9, 10, 12]
print(numbers)
print(type(numbers))

# %% tworzenie listy z różnym typami danych
mixed = ['python', 3, 3.7, True]
print(mixed)

# %% zagnieżdżanie list
empty = []
nested = [[1, 2, 3], ['python', 'sql']]

# %% dodawanie + pokazywanie długości
zagniezdzona = [nested, techs]
len(zagniezdzona)

# %% dodawanie
rozne = mixed + techs + ['scala']

# %% dodawanie do listy

numbers += [18]
print(numbers)

# %% listy - wycinanie

index = [0, 1, 2, 3, 4, 5]
idx_n = [-0, -1, -2, -3, -4, -5]
lista1 = [34, 23, 56, 78, 89]
#lista[::step]- wycinanie co step wartości
index[0::2]
lista1[-3:-1]
index[1:5]

# lista[start:stop]
# lista[index:]
# lista[start:]
# lista[:stop]
# lista[::step]

# %%listy - metody pracy

techs = []
print(techs)

# %% append - wstawia na koniec listy
techs.append('sql')
print(techs)

# %% 
techs.append(['java', 'spark'])

# %% wstawia wartośći na tym samym poziomie
techs.extend(['hadoop', 'sas'])

# %% insert wstawia wartość na danym miejscu
# (miejsce, wartość)
techs.insert(1, 'go')

# %% wyrywa ostatnią wartość z listy
# i wrzuca go do konsoli

techs.pop() #można dodawać nr indeksu
print(techs)
# %%
techs.index('go') #gdzie na liście
techs.count('hadoop') #ile razy na liście

# %%
techs.sort()
print(techs)

# %% sortowanie odwrotne
techs.sort(reverse=True)
# albo
techs.reverse()
# %%
techs[::-1]
print(techs)

# %% zmiana np druegiego elementu
techs[1] = 'python'

# %% sprawdzić funkcję insert

# %% 
# słowniki są zapisywane w nawiasach szcześciennych
# słownik to struktura nieuporządkowana
# słownik zawiera pary klucz-wartość
# w słownikach są klucze, nie indeksy
# klucze są unikalne w obrębie jednego słownika



empty_dict= dict()

print(empty_dict)

# %%
pol_to_eng = {'jeden':'one', 'dwa':'two',
              'trzy':'three'}

print(pol_to_eng)

e= set () #pusty zbiór

# %%
name_to_digit={'jeden':1, 'dwa':2, 'three':3}

# %% długość słownika to ilość par
print(len(name_to_digit))

#szablon
# dict = {'key1':'value1', 'key2':'value2'}

# %% dodawanie do słownika

pol_to_eng['cztery']='four'

# %% czyszczenie słownika

#pol_to_eng.clear()

# kopiowanie słownika
pol_to_eng_copied = pol_to_eng.copy()

# %% wydobywanie wszystkich kluczy
pol_to_eng.keys()

# %% 
pol_to_eng.values()

# %% wydobywanie kluczy i wartości
# pary klucz wartość nie możemy zmienić
# ale możemy np. wyrzucić jakąś parę
pol_to_eng.items()

# %% zwraca wartość klucza
pol_to_eng['jeden']

# %% get - nieco bardziej elastyczne
# (zwracan wartośc, słowo-jeśli błąd)

pol_to_eng.get('zero', 'NaN')

# %% tutaj trzeba podać argument
# argument to key, nie nr indeksu
pol_to_eng.pop('dwa')

# przy popitem usunie ostatni key i go wyprintuje
pol_to_eng.popitem()

# %% update słownika
# {key: update}

pol_to_eng.update({'jeden':1})



















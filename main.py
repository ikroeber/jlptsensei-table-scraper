from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag


class JLPTVocabularyItem:
    def __init__(self, word: str, reading: str, meaning: str):
        self.word = word
        self.reading = reading
        self.meaning = meaning

    def __str__(self) -> str:
        return f'{self.word} - {self.reading} - {self.meaning}\n\n'

    def __repr__(self) -> str:
        return self.__str__()


page = urlopen("https://jlptsensei.com/jlpt-n5-verbs-vocabulary-list/")

parsed_page = BeautifulSoup(page, "lxml")

table = parsed_page.find("table", {"id": "jl-vocab"})

rows = []

if isinstance(table, Tag):
    rows = table.find_all("tr", {"class": "jl-row"})

items = []

for row in rows:
    word = row.find("td", {"class": "jl-td-v"}).a.text
    reading = row.find("td", {"class": "jl-td-vr"}).a
    meaning = row.find("td", {"class": "jl-td-vm"}).text

    reading = "" if reading.p is None else reading.p.text

    items.append(JLPTVocabularyItem(word, reading, meaning))

file = open("output.txt", "w", encoding="utf-8")

for item in items:
    file.write(str(item))

file.close()

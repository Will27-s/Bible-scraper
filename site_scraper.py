import encodings
from fileinput import close
from get_bible_version import get_version_id
from book_chapter_verse import all_Chapters, get_books
import csv
import os
from bs4 import BeautifulSoup
import re
import requests

version_id, version_name = get_version_id()
books, bookName, testament = get_books()
allChapters, NoOfChapters = all_Chapters(books)



def store_books_file(books, bookName, testament,version_id):
    
    key = 0
    data = []
    for book in books:
        id = key + 1

        data.append([id, testament[key], bookName[key], books[key]])
        key += 1
    
    if os.path.exists(f"{version_name} Version Bible Books File.csv"):

        with open(f"{version_name} Version Bible Books File.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerows(data)
    else: 
        with open(f"{version_name} Version Bible Books File.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerows(data)



def get_bible_verses(bookName,books, NoOfChapters, version_id):
    
    
    bible_verses = []
    keybook = 0
    for bookcode in books:
        keychap = 0
        #NoOfChapters = NoOfChapters[keybook]
        for chapter in range(NoOfChapters[keybook]):
            url = f"https://www.bible.com/en-GB/bible/{version_id}/{bookcode}.{keychap+1}.KJV/"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            print(url)
            
        
            chapterFind = soup.find(class_=f"chapter ch{keychap+1}")
            
            NoOfVer = chapterFind.find_all(class_="label",text = re.compile("[0-9]+")) #Any number
            
            print(NoOfVer)
            
            NoOfVer = (len(NoOfVer)-1)
            print(NoOfVer)

            

            
            
            for ver in range(NoOfVer):
                
                print(ver)
                chapter1 = soup.find(class_=re.compile(f"verse v{ver+1}"))
                if chapter1 != None:
                    pass

                    
                else:
                    continue

                verse = chapter1.find_all(class_="content")
                print(verse)
                fullVerse = ""
                key = 0
                length = len(verse)
                for i in range(length):
                
                    content = chapter1.find_all(class_="content")
                    content = content[key]
                    content = content.text
                    fullVerse += content
                    key += 1
                
                data = [str(bookName[keybook]),keychap+1, ver+1, fullVerse]
                bible_verses.append(data)

            keychap += 1
        keybook += 1

    return bible_verses          
                
                
    

def store_bible_verses():
    if os.path.exists(f"{version_name} Version Bible Books File.csv"):

        with open(f"{version_name} Version Bible Verses File.csv", "w", newline="", encoding = "utf-8") as f:
            writer = csv.writer(f, delimiter=",")
            data = get_bible_verses(bookName, books, NoOfChapters, version_id)
            writer.writerows(data)
    else: 
        with open(f"{version_name} Version Bible Verses File.csv", "a", newline="", encoding = "utf-8") as f:
            writer = csv.writer(f, delimiter=",")
            data = get_bible_verses(bookName, books, NoOfChapters, version_id)
            writer.writerows(data)

store_books_file(books, bookName, testament, version_id)
store_bible_verses()






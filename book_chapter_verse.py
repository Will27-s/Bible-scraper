#This file gets all the codes for each chapter the verse number to be able to scrape through the site only has to be done once??

from cgitb import text
import json, requests
import pandas as pd



def get_books(): #gets all the books in the bible
    
    url = requests.get("https://www.bible.com/json/bible/books/1?filter=")

    text = url.text

    data = json.loads(text)

    books = []
    bookName = []
    key = 0
    newTestIdx = 0
    for i in data["items"]:
        books.append(data["items"][key]["usfm"])
        bookName.append(data["items"][key]["human"])



        if data["items"][key]["usfm"] == "MAT":
            newTestIdx = key
            key += 1
            continue
        else:
            key += 1
            continue

        
    key = 0
    testament = []
    for i in data["items"]:
        while key < newTestIdx:
            testament.append(1)
            key += 1
        testament.append(2)
        key += 1
    

    return books, bookName,testament
    



def all_Chapters(books):   
    allChapters = []
    
    NoOfChapters = []
    bookKey = 0
    for book in books: 
        url = f"https://www.bible.com/json/bible/books/1/{book}/chapters"   
        urlRequest = requests.get(url)
        text = urlRequest.text
        data = json.loads(text) 
        
        NoOfChapters.append( len(data["items"])) #Get the number of Chapters in each book

        key = 0
        for i in data["items"]:
            allChapters.append(data["items"][key]["usfm"])
            key += 1    
    
    
        
    return allChapters, NoOfChapters



books, bookName, testament = get_books()
allChapters, NoOfChapters = all_Chapters(books)
print(NoOfChapters)






from cgitb import text
import json, requests
import inquirer #So user can select from multiple options
from tkinter import *


def get_languages(): #Gets all the possible languages and stores it in an array
    url = requests.get("https://www.bible.com/json/bible/languages?filter=")
    text = url.text
    data = json.loads(text)
    key = 0
    languages = []
    for i in data["items"]:
        languages.append(data["items"][key]["local_name"])
        key += 1
    return languages
    
###Get language using GUI###

def Scankey(event):
	
	val = event.widget.get()
	print(val)
	

	if val == '':
		data = list
	else:
		data = []
		for item in list:
			if val.lower() in item.lower():
				data.append(item)				

	
	Update(data)


def Update(data):
	

	listbox.delete(0, 'end')

	# put new data
	for item in data:
		listbox.insert('end', item)



selectedLanguage = ""


list = get_languages()

ws = Tk()


entry = Entry(ws)
entry.pack()
entry.bind('<KeyRelease>', Scankey)


listbox = Listbox(ws)
listbox.pack()
Update(list)



def selected_language():
    global selectedLanguage
    for i in listbox.curselection():
        language = listbox.get(i)
        selectedLanguage = language
        ws.destroy()
        print(language)
    return language    
    
    
    
    

btn = Button(ws, text="Select Language", command=selected_language)
#btn2 = Button(ws, text="Exit", command=ws.des  )
btn.pack(side="bottom")

ws.attributes("-topmost", True)
ws.mainloop()


def get_langcode():
    global selectedLanguage
    url = requests.get("https://www.bible.com/json/bible/languages?filter=")
    text = url.text
    data = json.loads(text)
    key = 0
    for i in data["items"]: #For each language checks if language is the one you select

        if selectedLanguage == data["items"][key]["local_name"]:

            langcode = data["items"][key]["tag"]
            return langcode
        else:
            key += 1
            continue
    print("Invalid Language")




 

def get_version_id():
    
    url = f"https://www.bible.com/json/bible/versions/{get_langcode()}"   
    urlRequest = requests.get(url)
    text = urlRequest.text
    data = json.loads(text) 
    key = 0
    versions = []
    for i in data["items"]:
        versions.append(data["items"][key]["local_title"])
        key += 1
    questions = [
        inquirer.List("size",
        message="Choose a Version",
        choices= versions
        ),
    ]
    answers = inquirer.prompt(questions)
    version = answers["size"]

    key = 0
    for i in  data["items"]:
        if version == data["items"][key]["local_title"]:
            version_id = data["items"][key]["id"]
            version_name = data["items"][key]["local_title"]

            return version_id, version_name
        else:
            key += 1
            continue




###End

 

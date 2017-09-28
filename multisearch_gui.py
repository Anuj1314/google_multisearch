import tkinter
import webbrowser
def multisearch():
	query=searchEntry.get()
	querylist=query.split(',')
	for i in range(len(querylist)):
		if querylist[i][0]==' ':
			querylist[i]=querylist[i][1:]
	for i in range(len(querylist)):
		sublist=querylist[i].split()
		query=""
		url=""
		for j in range(len(sublist)):
			query=query+sublist[j]+"+"
		url="www.google.com/search?q="+query[:-1]
		webbrowser.open_new(url)
window = tkinter.Tk()
queryLabel=tkinter.Label(window,text='Enter query')
searchEntry=tkinter.Entry(window)
searchButton=tkinter.Button(window,text='SEARCH',command=multisearch)
queryLabel.pack()
searchEntry.pack()
searchButton.pack()
window.mainloop()
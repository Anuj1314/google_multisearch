import webbrowser
query=input()
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
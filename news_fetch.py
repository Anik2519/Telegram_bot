import requests

def fetch(q):

    query_params = {
    "q": q,
    "qInTitle": q,
	"sortBy": "popularity",
	"apiKey": "88840f2089bf4c48804b6b5f2f94955e",
    "language": "en"
	}
    main_url = " https://newsapi.org///v2/everything"
    res = requests.get(main_url, params=query_params)
    r = res.json()

    if r["totalResults"] == 0:
        return "Sorry no news in this categorly :'( \nCheck spelling or try different words ヽ(•‿•)ノ"

    article = r["articles"]
    results = ""

    i=1
    for ar in article:
        results= results + str(i) +". " + ar["title"] +"\n" + ar["url"] +"\n" +"\n"
        i=i+1
        if i==16:
            break
  
    return results


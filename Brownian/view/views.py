from django.shortcuts import render
import utils.es

def home(request):
    """ This page is just a simple landing page.
    """
    data = {"indices": utils.es.getIndices()}
    return render(request, "home.html", data)

def query(request):
    """ This page is the main query interface.
    """
    data = {}

    params = request.GET

    # If we have a blank query, just return everything.
    query = params.get("query", "")
    if query == "": query = "*"
    data["query"] = query

    # If we have a blank time window, just return the past 15 minutes.
    time = params.get("time", "")
    if time == "": time = "15m"
    data["time"] = time

    result = utils.es.queryFromString(utils.es.queryEscape(query), index=utils.es.indicesFromTime(time))
    data["hits"] = utils.es.resultToTabbedTables(result)

    # To make the Javascript easier, we strip off the # from the currently open tab.
    # If we don't have an open tab, default to conn.
    openTab = params.get("openTab", "#conn").replace("#", "")

    if openTab in [result["type"] for result in data["hits"]]: data["openTab"] = openTab
    else:
        if data["hits"]: data["openTab"] = data["hits"][0]["type"]
        else: data["openTab"] = "conn"

    return render(request, "query.html", data)

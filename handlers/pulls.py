import requests

username = 'dzmitrymezhva'
userpass = '*************'


def content(response):
    response = response.json()
    table = []
    i = 0
    while i < len(response):
        table.append({"login": response[i]["user"]["login"], "created": response[i]["created_at"],
                      "num": response[i]["number"], "link": response[i]["html_url"],
                      "title": response[i]["title"]})
        i += 1
    return table


def need_pulls(state):
    if state == "open" or state == "closed" or state == "all":
        response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/'
                                'pulls?per_page=100&state=' + state, auth=(username, userpass))
        return content(response)
    else:
        response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/'
                                'issues?per_page=100&labels=' + state, auth=(username, userpass))
        return content(response)


def get_pulls(state):
    if state is None:
        state = "all"
    return need_pulls(state)

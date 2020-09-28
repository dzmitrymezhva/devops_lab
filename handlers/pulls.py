import requests

username = 'dzmitrymezhva'
userpass = '*************'


def content(response):
    table = []
    i = 0
    while i < len(response):
        table.append({"login": response[i]["user"]["login"], "created": response[i]["created_at"],
                      "num": response[i]["number"], "link": response[i]["html_url"],
                      "title": response[i]["title"]})
        i += 1
    return table


def get_state(state):
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/'
                            'pulls?per_page=100&state=' + state, auth=(username, userpass))
    return content(response.json())


def get_label(state):
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/'
                            'issues?per_page=100&labels=' + state, auth=(username, userpass))
    return content(response.json())


def get_pulls(state):
    if state == "open" or state == "closed" or state == "all":
        return get_state(state)
    elif state == "needs work" or state == "accepted" or state == "invalid":
        return get_label(state)
    elif state is None:
        state = "all"
        return get_state(state)

import webbrowser


def network_research(research):
    researching = f"https://www.google.com/search?q={research}"
    webbrowser.open_new_tab(researching)
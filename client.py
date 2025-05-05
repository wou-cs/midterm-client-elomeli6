import requests


def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    try:
        response = requests.get("http://chrisbrooks.pythonanywhere.com/api/programmers")
        if response.status_code == 200:
            data = response.json()
            return len(data["programmers"])
    except Exception:
        return 0


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    try:
        response = requests.get(f"http://chrisbrooks.pythonanywhere.com/api/programmers/{pid}")
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception:
        return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    try:
        response = requests.get(f"http://chrisbrooks.pythonanywhere.com/api/programmers/{first_name}")
        if response.status_code == 200:
            data = response.json()
            for name in data["programmers"]:
                if name["first_name"] == first_name:
                    return f"{name["first_name"] + name["last_name"]}"
    except Exception:
        return {}

    return ""

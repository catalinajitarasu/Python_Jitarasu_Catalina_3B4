import re
import os
from typing import List


def ex_1(text: str) -> List:
    result = re.findall("\\w+", text)
    if result:
        return result


def ex_2(regex: re, text: str, x: int) -> List:
    match = re.findall(regex, text)
    list_substring = []
    for i in range(0, len(match)):
        if len(match[i]) == x:
            list_substring.append(match[i])
    return list_substring


def ex_3(list_string, list_regex) -> List[str]:
    result = []
    for regex in list_regex:
        for string in list_string:
            match = re.findall(regex, string)
            for i in range(0, len(match)):
                result.append(match[i])
    return list(set(result))


def ex_4(path_xml: str, attrs: dict) -> List[str]:
    result = []
    with open(path_xml, "r") as file:
        xml = file.read()
        for elem in re.findall(r"\w+.*?>", xml):
            if all([re.search(item[0] + r"\s*=\s*\"" + item[1] + "\"", elem) for item in attrs.items()]):
                result += [elem]
    return list(set(result))


def ex_5(path_xml: str, attrs: dict) -> List[str]:
    # in loc de all am folosit any
    result = []
    with open(path_xml, "r") as file:
        xml = file.read()
        for elem in re.findall(r"\w+.*?>", xml):
            if any([re.search(item[0] + r"\s*=\s*\"" + item[1] + "\"", elem) for item in attrs.items()]):
                result += [elem]
    return list(set(result))


def censorship(string):
    word = string.group(0).lower()
    if word[0] not in "aeiou" and word[-1] not in "aeiou":
        return string.group(0)
    return "".join([character if index % 2 == 0 else '*' for index, character in enumerate(string.group(0))])


def ex_6(text):
    return re.sub(r"\w+", censorship, text)


def ex_7(cnp) -> bool:
    """" de aici este preluat regex ul
    https://regex101.com/library/bpaE5K
    """
    if re.match(
            r"^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",
            cnp):
        return True
    return False


def ex_8(path_dir, regex):
    try:
        for root, directories, files in os.walk(path_dir):
            for f in files:
                name = os.path.join(root, f)
                data = open(name, "rt").read()
                if re.match(regex, f):
                    if re.match(regex, data):
                        print("<<" + name)
                    else:
                        print(name)
                if re.match(regex, data):
                    print(name)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(ex_1("Python2aa bb45 21a 21*"))
    print(ex_2(r"\d+", "Color from pixel 20,30 is 123", 2))
    print(ex_3(["Python34", "23", "ana34", "20*"], [r"\d+", r"[a-zA-Z0-9]+"]))
    print(ex_4("E:/pythonProject1/Laborator/file.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
    print(ex_5("E:/pythonProject1/Laborator/file.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
    print(ex_6("Anastasia are mere"))
    print(ex_7("5000310374534"))
    ex_8("E:/pythonProject1/Lab6", "Laborator")

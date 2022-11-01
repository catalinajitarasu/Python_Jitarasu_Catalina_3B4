from typing import List, Callable
import os
import sys


def ex_1(path: str) -> List[str]:
    """
    splitext imparte numele caii in perechi de root si ext; ext este de ex .txt
    """
    try:
        return sorted(list(set([os.path.splitext(el)[1][1:]
                                for el in os.listdir(path)
                                if os.path.isfile(os.path.join(path, el)) and os.path.splitext(el)[1] != ""])))
    except Exception as e:
        print(str(e))
        return []


def ex_2(directory: str, file: str):
    """"
    deschidem fisierul de la calea file doar pentru write (w)
    in care scriem pe cate o linie (linesep) abspath--calea absoluta a fiecărui fișier(f) din interiorul directorului
    daca acesta este fisier si incepe cu litera A
    """
    try:
        with open(file, "w") as fd:
            [fd.write(os.path.abspath(f) + os.linesep) for f in os.listdir(directory) if
             os.path.isfile(f) and f.startswith("a")]
    except Exception as e:
        print(str(e))


def ex_3(my_path):
    # verific daca este file
    # deschid fisierul cu functia de rb- read binary
    if os.path.isfile(my_path):
        with open(my_path, "rb") as f:
            file_size = os.path.getsize(my_path)
            assert (file_size >= 20), "File needs to have minim 20 characters"
            # cu functia seek setam pozitia pentru a ramane cu ultimele 20 caractere
            f.seek(file_size - 20)
            return f.read()
    elif os.path.isdir(my_path):
        lista = {}
        # am folosit functia os.walk (https://docs.python.org/3/library/os.html)
        # pentru a genera numele fisierelor intr-un arbore de directoare
        # root - directoare din target
        # directories - subdirectoare din root
        # files - toate fișierele din rădăcină și directoare
        for root, dirs, files in os.walk(my_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in lista:
                    lista[ext] += 1
                else:
                    lista[ext] = 1
        lista = lista.items()
        return sorted(lista, key=lambda el: el[1], reverse=True)
    else:
        raise Exception("Invalid parameter.")


def ex_4():
    try:
        assert (len(sys.argv) > 1), "Invalid number of parameters"
        assert (os.path.isdir(sys.argv[1])), "Invalid director"
        return sorted(list(set([os.path.splitext(el)[1][1:]
                                for el in os.listdir(sys.argv[1])
                                if os.path.isfile(os.path.join(sys.argv[1], el)) and os.path.splitext(el)[1] != ""])))
    except Exception as e:
        print(str(e))
        return []


def file_contains_to_search(target: str, to_search: str) -> bool:
    # cautam in fisier sa vedem daca contine to_search pt a o folosi in ex_5
    with open(target, "rt") as f:
        text = f.read()
        return to_search in text


def ex_5(target: str, to_search: str) -> List[str]:
    # verificam daca target este fisier
    if os.path.isfile(target):
        # daca da, verificam daca avem un fisier care sa contina to_Search, daca da returnam target (adaugam in lista)
        if file_contains_to_search(target, to_search):
            return [target]
        else:
            return []
    # verificam daca target director
    # daca da, cautam recursiv in toate fisierele din acel director
    elif os.path.isdir(target):
        to_return = []
        for root, directories, files in os.walk(target):
            # print(files)
            for f in files:
                name = os.path.join(root, f)
                if file_contains_to_search(name, to_search):
                    to_return += [name]
        return to_return
    else:
        raise ValueError("Target needs to be file/directory")


def error_callback(exception: Exception):
    """
    prints exception
    """
    print(exception)


def ex_6(target: str, to_search: str, callback: Callable):
    try:
        # folosesc functia scrisa la exercitiul 5
        return ex_5(target, to_search)
    except Exception as e:
        callback(e)
        return []


def ex_7(file_path: str) -> dict:
    try:
        # verific daca calea data este fisier sau director
        # daca este file adaug in dictionar folosind functiile si il returnez
        if os.path.isdir(file_path):
            raise Exception("Path is directory")
        return {
            "full_path": os.path.abspath(file_path),
            "file_size": os.path.getsize(file_path),
            "file_extension": os.path.splitext(file_path)[1],
            "can_read": os.access(file_path, os.R_OK),
            "can_write": os.access(file_path, os.W_OK),
        }
    except Exception as e:
        print(str(e))
        return {}


def ex_8(dir_path: str) -> List[str]:
    try:
        result = []
        for f in os.listdir(dir_path):
            if os.path.isfile(f):
                name = os.path.join(dir_path, f)
                result += [os.path.abspath(name)]
        return result
    except Exception as e:
        print(str(e))
        return []

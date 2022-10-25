from typing import List, Set, Tuple


def ex_1(a: list, b: list) -> List[set]:
    # punem set pentru a nu avea duplicate si folosim functiile
    a = set(a)
    b = set(b)
    return [a.intersection(b), a.union(b), a.difference(b), b.difference(a)]


def ex_2(string: str) -> dict:
    """
   folosim set pentru a avea in characters toate literele din sir( dar set are elemente unice, deci caracterele
   apar o singura data in characters)
   fiecare element din set este o cheie in dictionar
   numar de cate ori apare fiecare litera (keyy) in string(input)
  """
    characters = set(string)
    return dict([(keyy, string.count(keyy)) for keyy in characters])


def build_xml_element(tag: str, content: str, **elements) -> str:
    """"
    ex_4
    adaug pe rand in result
    apoi parcurg elements pentru a lua fiecare cheie pe care o adaug in result, adaug = si apoi adaug si elements[key]
    """
    result = "< "
    result += tag
    result += " "
    for key in elements:
        result = result + " " + key + "=" + "\"" + elements[key] + "\""
    result += ">"
    result += " " + content + " "
    result += "</"
    result += tag
    result += "> "

    return result


def validate_dict(rules: Set[tuple], dictionary: dict) -> bool:
    """"
    ex_5
    luam fiecare regula in parte si o verificam in dictionar astfel:
    prima data retinem valuare fiecarei chei din rules
    daca value in None (empty)--inseamna ca nu avem acea key in dictionary deci--fals
    apoi daca value(adica valoarea unei chei din dictionar) nu incepe cu rule[1],
    nu are rule[2] in interior, nu se termina cu rule[3] sau incepe sau se termina cu rule[2]--false
    daca am trecut de if uri inseamna ca este adevarat
    """
    for rule in rules:
        value = dictionary.get(rule[0])
        if value is None:
            return False
        if not value.startswith(rule[1]) \
                or not value.endswith(rule[3]) \
                or not rule[2] in value \
                or value.startswith(rule[2]) \
                or value.endswith(rule[2]):
            return False
        return True


def ex_6(input_list: list) -> (int, int):
    """"
    len(list)-- returneaza numarul de elemente din lista
    prin set(input_list)-- in set avem doar elemente unice
    len(set(input_list))- returneaza numarul de elemente din set
    """
    return len(set(input_list)), len(input_list) - len(set(input_list))


def apply_operation(set1: set, set2: set, operation: str) -> (str, set):
    """"
    functie care aplica fiecare operator
    afiseaza fiecare set ca un string, semnul ca un string dupa care efectueaza operatia
    """
    if operation == "|":
        return str(set1) + "|" + str(set2), set2 | set1
    if operation == "&":
        return str(set1) + "&" + str(set2), set2 & set1
    if operation == "-":
        return str(set1) + "-" + str(set2), set1 - set2
    if operation == "/":
        return str(set2) + "-" + str(set1), set2 - set1


def ex_7(*input_sets) -> dict:
    """"
    ex_7
    key sunt cele doua seturi impreuna cu semnul
    iar value este valoarea operatiei aplicate pe cele doua seturi
    aplicam fiecare operator pentru fiecare pereche de 2 seturi posibile ceea ce retinem cu x si y
    multimea operatorilor este |&-/
    """
    return {
        key: value for key, value in [apply_operation(sett[0], sett[1], operation)
                                      for sett in [(input_sets[x], input_sets[y])
                                                   for x in range(len(input_sets) - 1)
                                                   for y in range(x + 1, len(input_sets))]
                                      for operation in "|&-/"
                                      ]
    }


def ex_8(mapping: dict) -> list:
    """"
    luam o lista visited in care sa retinem keys care au fost vizitate
    in pos_current retinem cheia curenta pe care o actualizam cu mapping[pos_current]
    afisam lista in moemtul in care pos_curent a mai fost vizitata(se regaseste in visited)
    """
    visited = []
    pos_current = 'start'
    values = set()
    while True:
        if pos_current in visited:
            return list(values)
        visited.append(pos_current)
        pos_current = mapping[pos_current]
        values.add(pos_current)


def ex_9(*positions, **arguments) -> int:
    """"
    parcurg arg de pozitii, p un arg de pozitie, iar daca valoarea lui p se regaseste
    in valorile arg de cuv cheie atunci creste count ul
    accesam val arg de cuv cheie cu values()
    """
    count = 0
    for p in positions:
        if p in arguments.values():
            count += 1
    return count

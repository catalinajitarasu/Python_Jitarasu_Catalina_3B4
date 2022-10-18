from typing import List


def list_fibonacci(n: int) -> List[int]:
    """
    definim o lista cu un element 0 (primul termen a lui Fibonacci)
            apoi adaugam 1,1
            cu ajutorul unui while cu un index in care retinem cate numere am adaugat in lista generam numerele
            din sirul lui Fibonacci
            la fiecare pas adaugam in lista numarul generat
    """
    fibonacci_list = [0]
    a = 1
    b = 1
    index = 3
    fibonacci_list.append(a)
    fibonacci_list.append(b)
    while True:
        if index > n:
            return fibonacci_list
        c = a + b
        a = b
        b = c
        index = index + 1
        fibonacci_list.append(c)


def verification_prime(n: int) -> bool:
    """
    o functie care verifica daca un numar este prim si returneaza o valoare boolean (true sau false)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if int(n % 2) == 0:
        return False
    for i in range(3, int(n / 2)):
        if n % i == 0:
            return False
    return True


def prime_list_number(number_list: List[int]) -> List[int]:
    """
    verific fiecare element din lista daca indeplineste conditia de primalitate
    """
    return [x for x in number_list if verification_prime(x)]


def ex_4(notes: List[str], moves: List[int], start_position: int) -> List[str]:
    """"
    cream o noua lista in care adaug prima data nota de pe pozitia de start
    parcurc lista de miscari si calculez noua pozitie
    cu ajutorul forului extrag termenii din lista cu ajutor carora calculez noua pozitia
    """
    new_list = [notes[start_position]]
    for index in moves:
        start_position = start_position + index
        start_position = start_position % len(notes)
        new_list.append(notes[start_position])
    return new_list


def modify_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    stim ca elementele de sub diagonala principala sunt cele care indeplinesc conditia i>j
    numarul de linii este len(matrix), cu indecele i pt linii
    numarul de coloane esre len(matrix[0]), cu indecele j pentru coloane
    """
    return [[matrix[i][j] if i >= j else 0
             for i in range(len(matrix))]
            for j in range(len(matrix[0]))
            ]


def list_exactly_x_times(*lists: List, x: int) -> List:
    """
    cream o lista cu toate listele (united_list)
    verificam fiecare numar din united_list daca se regaseste de exact x ori (cu ajutorul functiei count)in lista si
     daca nu a fost deja adaugat, il adaugam
     la final returnam lista formata
    """
    united_lists = []
    new_list = []
    for i in lists:
        united_lists += i
    for i in united_lists:
        if united_lists.count(i) == x and i not in new_list:
            new_list.append(i)
    return new_list


def tuple_palindrome(number_list: List[int]) -> [int, int]:
    """
       am gasit pe internet ca [::-1] iti formeaza exact palindromul
       str(int) transforma int ul in string
       o expresie lambda care parcurge fiecare element din number_list si verifica conditia
       filter- pentru a crea o noua lista bazat pe expresia lambda
       """
    palindrome_list = list(filter(lambda x: str(x) == str(x)[::-1], number_list))
    return [len(palindrome_list), max(palindrome_list)]


def ex_11(tuple_list: List[tuple]) -> List[tuple]:
    """
    am folosit metoda sort impreuna cu expresia lambda (asemanator cu ce e in curs)
    x[1][2]
    [1]- al doilea cuvant din tuplu
    [2]- al treilea caracter al celui de-al doilea cuvant
    """
    tuple_list.sort(key=lambda x: x[1][2])
    return tuple_list

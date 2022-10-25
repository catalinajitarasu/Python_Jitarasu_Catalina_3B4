import main as testt

print(testt.ex_1(
    [1, 2, 3, 4, 5, 6, 4, 4, 3], [4, 5, 6, 7, 8, 8, 9]
))

print(testt.ex_2("Ana has apples"))

print(testt.build_xml_element("a", "Hello there", href=" https://python.org ", _class=" my-link ", id=" someid "))

print(testt.validate_dict(
    {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
    {"key1": "come inside, it's too cold out", "key2": "start middle this is not valid winter"}
))

print(testt.ex_7({1, 2, 4}, {2, 3, 4}, {1,2,4,5}))

print(testt.ex_8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

print(testt.ex_9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
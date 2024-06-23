from linkedlist.solution import LinkedList

def test_add_numbers_to_list():
    list = LinkedList()
    for i in range(100):
        list.append(i)

    print(list)
    assert list.tail.value == 99
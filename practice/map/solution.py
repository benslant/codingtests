from typing import List


class HashMapNode():

    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value

class HashMap():

    def __init__(self) -> None:
        self.storage: List[HashMapNode] = [None] * 16

    def get(self, key: str) -> object:
        pass

    def set(self, key: str, value: str):
        str_hash = key.__hash__()
        index = str_hash % 16
        node = HashMapNode(key, value)
        if not self.storage[index]:
            self.storage[index] = [node]
        else:
            items = self.storage[index]
            if node not in items:
                self.storage.append(node)
            else:
                for i in self.storage[index]:
                    if i.key == node.key:
                        i.value = value

    def get(self, key: str) -> str:
        str_has = key.__hash__()
        index = str_has % 16

        list = self.storage[index]
        for l in list:
            if l.key == key: return l.value

        raise




    def __hash(self, key: str):
        pass
        
import random
class RandomizedSet(object):

    def __init__(self,):
        self.list = []
        self.dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.list.append(val)
            self.dict[val]=val
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            self.list.append(val)
            self.dict[val]=val
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)


if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(1))
    print(obj.insert(2))
    print(obj.getRandom())

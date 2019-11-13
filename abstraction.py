#Data abstraction in python

class Superior:
    __id = 1;
    def __showid__(self):
        Superior.__id=2;
        print(Superior.__id)


obj = Superior()
obj.__showid__()
obj.__id

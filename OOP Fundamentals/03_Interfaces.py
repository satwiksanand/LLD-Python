from abc import ABC, abstractmethod

class DatabaseStorage(ABC):
    @abstractmethod
    def store(self, data: list[dict]):
        '''
        :param data: list[dict]
        :return: void

        accepts a list of {key, value} pairs, where
        :key is the attribute name
        :value is the data
        '''
        pass

class SQLDB(DatabaseStorage):
    def store(self, data: list[dict]):
        print("storing the data using SQL in MySQL.")

class MongoDB(DatabaseStorage):
    def store(self, data: list[dict]):
        print("storing data in mongodb")

if __name__ == "__main__":
    my_db = SQLDB()
    my_db.store([{"name": "Dev"}])
    my_db = MongoDB()
    my_db.store([{"name": "Dev"}])


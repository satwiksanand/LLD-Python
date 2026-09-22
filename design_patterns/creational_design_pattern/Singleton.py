# there are different variations of the singleton design pattern that we are going to see in this one.
import threading
from typing import Self


#? lazy singleton

class LazySingleton:
    _instance = None

    def __int__(self):
        pass # or just raise an error to use the get_instance method

    @staticmethod
    def get_instance():
        if LazySingleton._instance is None:
            LazySingleton._instance = LazySingleton()
        return LazySingleton._instance


#? Thread Safe Singleton Design Pattern
class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __int__(self):
        pass

    @staticmethod
    def get_instance():
        if ThreadSafeSingleton._instance is None:
            with ThreadSafeSingleton._lock:
                if ThreadSafeSingleton._instance is None:
                    ThreadSafeSingleton._instance = ThreadSafeSingleton()
        return ThreadSafeSingleton._instance

#? using __new__ method
# when we are creating a class obj = Singleton()
# behind the scenes something like this is executing:
# tobj = Singleton.__new__(Singleton)
# Singleton.__init__(tobj)
# obj = tobj
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __int__(self):
        pass

#? Decorator Singleton
def SingletonDecorator(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        if cls is not in instances.keys():
            with lock:
                if cls is not in instances.keys():
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@SingletonDecorator
class Singleton2:
    def __init__(self):
        pass


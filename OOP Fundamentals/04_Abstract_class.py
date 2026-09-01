# abstract class is used when a string contract is needed to be established but different classes need some shared data.
# for example consider the below renderData class, fetch is a common method that all the child classes share but each \
# of the child classes has their unique render method

from abc import ABC, abstractmethod

class RenderData(ABC):
    _content: str

    def __init__(self):
        self.fetch("https://somedata.com")

    def fetch(self, url: str):
        print(f"fetching data from {url}")
        self._content = "dummy data"

    @abstractmethod
    def render(self):
        pass

class MarkDownRenderer(RenderData):
    def render(self):
        print(self._content)
        print("rendering markdown data!")

class JSONRenderer(RenderData):
    def render(self):
        print(self._content)
        print("rendering JSON data!")

if __name__ == "__main__":
    obj = MarkDownRenderer()
    obj.render()
    obj = JSONRenderer()
    obj.render()
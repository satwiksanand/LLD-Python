# Define an abstract ExportFormat class. Its public render(events)
# method must handle empty input once, then call an abstract
# format(events) method for the format-specific work.
#
# Implement CsvFormat, SummaryFormat, and JsonFormat.
# EventExporter is provided. Do not modify it.
from abc import ABC, abstractmethod

class ExportFormat(ABC):
    @abstractmethod
    def render(self, events: list[str]):
        pass

class CsvFormat(ExportFormat):
    def render(self, events: list[str]):
        if len(events) == 0:
            return "INVALID"
        return ", ".join(events)

class SummaryFormat(ExportFormat):
    def render(self, events: list[str]):
        if len(events) == 0:
            return "INVALID"
        return f"{len(events)} events: " + " | ".join(events)

class JsonFormat(ExportFormat):
    def render(self, events: list[str]):
        if len(events) == 0:
            return "INVALID"
        return [event for event in events]

class EventExporter:
    def __init__(self):
        self._events: list[str] = []
        self._formats = {
            "csv": CsvFormat(),
            "summary": SummaryFormat(),
            "json": JsonFormat(),
        }

    def addEvent(self, name: str) -> bool:
        if not name:
            return False
        self._events.append(name)
        return True

    def exportAs(self, ft: str) -> str:
        exporter = self._formats.get(ft)
        if exporter is None:
            return "UNSUPPORTED"
        return exporter.render(self._events)

    def eventCount(self) -> int:
        return len(self._events)

# Your EventExporter object will be instantiated and called as such:
# obj = EventExporter()
# param_1 = obj.addEvent(name)
# param_2 = obj.exportAs(format)
# param_3 = obj.eventCount()

if __name__ == "__main__":
    obj = EventExporter()
    obj.addEvent(name="signup")
    obj.addEvent(name="login")
    obj.addEvent(name="logout")
    print(obj.exportAs("csv"))
    print(obj.exportAs("aiushfo"))
    print(obj.exportAs("summary"))
    print(obj.exportAs("json"))
# Task: replace the fat OfficeDevice interface with per-capability contracts, keeping behavior identical (Interface Segregation).
# - One interface per capability: printing (printDocument), scanning (scanPage), faxing (sendFax).
# - BasicPrinter implements only printing, FlatbedScanner only scanning, AllInOne all three.
# - Remove every "UNSUPPORTED" placeholder method and support flag from the device classes.
# - DeviceHub records which capabilities each device has (for example, a small entry holding the
#   optional printer, scanner, and faxer) and keeps its public API, including "UNSUPPORTED"
#   for unsupported operations and invalid indexes.

# class OfficeDevice(ABC):
#     @abstractmethod
#     def supportsPrint(self) -> bool:
#         ...
#
#     @abstractmethod
#     def supportsScan(self) -> bool:
#         ...
#
#     @abstractmethod
#     def supportsFax(self) -> bool:
#         ...
#
#     @abstractmethod
#     def printDocument(self, document: str) -> str:
#         ...
#
#     @abstractmethod
#     def scanPage(self) -> str:
#         ...
#
#     @abstractmethod
#     def sendFax(self, number: str) -> str:
#         ...
#
#
# class BasicPrinter(OfficeDevice):
#     def supportsPrint(self) -> bool:
#         return True
#
#     def supportsScan(self) -> bool:
#         return False
#
#     def supportsFax(self) -> bool:
#         return False
#
#     def printDocument(self, document: str) -> str:
#         return "PRINTED: " + document
#
#     def scanPage(self) -> str:
#         return "UNSUPPORTED"
#
#     def sendFax(self, number: str) -> str:
#         return "UNSUPPORTED"
#
#
# class FlatbedScanner(OfficeDevice):
#     def supportsPrint(self) -> bool:
#         return False
#
#     def supportsScan(self) -> bool:
#         return True
#
#     def supportsFax(self) -> bool:
#         return False
#
#     def printDocument(self, document: str) -> str:
#         return "UNSUPPORTED"
#
#     def scanPage(self) -> str:
#         return "SCANNED"
#
#     def sendFax(self, number: str) -> str:
#         return "UNSUPPORTED"
#
#
# class AllInOne(OfficeDevice):
#     def supportsPrint(self) -> bool:
#         return True
#
#     def supportsScan(self) -> bool:
#         return True
#
#     def supportsFax(self) -> bool:
#         return True
#
#     def printDocument(self, document: str) -> str:
#         return "PRINTED: " + document
#
#     def scanPage(self) -> str:
#         return "SCANNED"
#
#     def sendFax(self, number: str) -> str:
#         return "FAXED TO " + number
#
#
# class DeviceHub:
#     def __init__(self):
#         self._devices = []
#
#     def _at(self, index: int):
#         if index < 0 or index >= len(self._devices):
#             return None
#         return self._devices[index]
#
#     def addPrinter(self) -> int:
#         self._devices.append(BasicPrinter())
#         return len(self._devices) - 1
#
#     def addScanner(self) -> int:
#         self._devices.append(FlatbedScanner())
#         return len(self._devices) - 1
#
#     def addAllInOne(self) -> int:
#         self._devices.append(AllInOne())
#         return len(self._devices) - 1
#
#     def canPrint(self, index: int) -> bool:
#         device = self._at(index)
#         return device is not None and device.supportsPrint()
#
#     def canScan(self, index: int) -> bool:
#         device = self._at(index)
#         return device is not None and device.supportsScan()
#
#     def canFax(self, index: int) -> bool:
#         device = self._at(index)
#         return device is not None and device.supportsFax()
#
#     def printDoc(self, index: int, document: str) -> str:
#         device = self._at(index)
#         if device is None:
#             return "UNSUPPORTED"
#         return device.printDocument(document)
#
#     def scan(self, index: int) -> str:
#         device = self._at(index)
#         if device is None:
#             return "UNSUPPORTED"
#         return device.scanPage()
#
#     def fax(self, index: int, number: str) -> str:
#         device = self._at(index)
#         if device is None:
#             return "UNSUPPORTED"
#         return device.sendFax(number)

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def printDocument(self, document: str) -> str:
        ...

class Scanner(ABC):
    @abstractmethod
    def scanPage(self) -> str:
        ...

class Fax(ABC):
    @abstractmethod
    def sendFax(self, number: str) -> str:
        ...

class BasicPrinter(Printer):
    def printDocument(self, document: str) -> str:
        return "PRINTED: " + document

class FlatbedScanner(Scanner):
    def scanPage(self) -> str:
        return "SCANNED"

class AllInOne(Printer, Scanner, Fax):
    def printDocument(self, document: str) -> str:
        return "PRINTED: " + document

    def scanPage(self) -> str:
        return "SCANNED"

    def sendFax(self, number: str) -> str:
        return "FAXED TO " + number

class DeviceEntry:
    def __init__(self, printer: Printer | None= None, scanner: Scanner | None = None, fax: Fax | None = None):
        self.printer: Printer | None = printer
        self.scanner: Scanner | None = scanner
        self.fax_machine: Fax | None = fax

    def canPrint(self):
        return self.printer is not None

    def canScan(self):
        return self.scanner is not None

    def canFax(self):
        return self.fax_machine is not None

class DeviceHub:
    def __init__(self):
        self._devices: list[DeviceEntry] = []

    def _at(self, index: int) -> DeviceEntry | None:
        if index < 0 or index >= len(self._devices):
            return None
        return self._devices[index]

    def addPrinter(self) -> int:
        printer = BasicPrinter()
        entry = DeviceEntry(
            printer=printer
        )
        self._devices.append(entry)
        return len(self._devices) - 1

    def addScanner(self) -> int:
        scanner = FlatbedScanner()
        entry = DeviceEntry(
            scanner=scanner
        )
        self._devices.append(entry)
        return len(self._devices) - 1

    def addAllInOne(self) -> int:
        device = AllInOne()
        entry = DeviceEntry(
            printer=device,
            scanner=device,
            fax=device
        )
        self._devices.append(entry)
        return len(self._devices) - 1

    def canPrint(self, index: int) -> bool:
        device = self._at(index)
        return device is not None and device.canPrint()

    def canScan(self, index: int) -> bool:
        device = self._at(index)
        return device is not None and device.canScan()

    def canFax(self, index: int) -> bool:
        device = self._at(index)
        return device is not None and device.canFax()

    def printDoc(self, index: int, document: str) -> str:
        device = self._at(index)
        if device is None or not device.canPrint():
            return "UNSUPPORTED"
        return device.printer.printDocument(document)

    def scan(self, index: int) -> str:
        device = self._at(index)
        if device is None or not device.canScan():
            return "UNSUPPORTED"
        return device.scanner.scanPage()

    def fax(self, index: int, number: str) -> str:
        device = self._at(index)
        if device is None or not device.canFax():
            return "UNSUPPORTED"
        return device.fax_machine.sendFax(number)
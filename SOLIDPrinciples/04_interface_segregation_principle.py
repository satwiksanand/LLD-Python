# A class should not be forced to depend on methods it does not use.

#Bad Example

from abc import ABC, abstractmethod


class Printer(ABC):

    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

    @abstractmethod
    def fax_document(self, document):
        pass


class BadBasicPrinter(Printer):

    def print_document(self, document):
        print(f"Printing {document}")

    def scan_document(self, document):
        raise NotImplementedError

    def fax_document(self, document):
        raise NotImplementedError

# Good Example

from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def print_document(self, document):
        pass


class Scannable(ABC):

    @abstractmethod
    def scan_document(self, document):
        pass


class Faxable(ABC):

    @abstractmethod
    def fax_document(self, document):
        pass

class BasicPrinter(Printable):

    def print_document(self, document):
        print(f"Printing {document}")

class Scanner(Scannable):

    def scan_document(self, document):
        print(f"Scanning {document}")

class MultiFunctionPrinter(Printable, Scannable, Faxable):

    def print_document(self, document):
        print(f"Printing {document}")

    def scan_document(self, document):
        print(f"Scanning {document}")

    def fax_document(self, document):
        print(f"Faxing {document}")
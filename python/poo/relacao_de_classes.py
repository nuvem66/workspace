class Book:
    def __init__(self, name, closed = True) -> None:
        self.name = name
        self.closed = closed
        self.is_being_readed = False
    
    def abrir(self):
        if self.closed:
            self.closed = False
            print(f'{self.name} foi aberto.')
        else:
            print(f'{self.name} já estava aberto')

    def read(self):
        if not self.is_being_readed:
            self.is_being_readed = True
            print(f'{self.name} está sendo lido.')
        else:
            print(f'{self.name} já estava sendo lido.')

    def close(self):
        if not self.closed:
            self.is_being_readed = False
            self.closed = True
            print(f'{self.name} foi fechado e não está mais sendo lido.')
        else:
            print(f'{self.name} já estava fechado.')


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.is_reading = False
        self.last_book = ''
    
    def read(self, book):
        if not self.is_reading:
            self.last_book = book
            book.abrir()
            book.read()
            self.is_reading = True
            print(f'{self.name} abriu e está lendo {book.name}')

        else:
            self.last_book.close
            book.abrir()
            book.read()
            print(f'{self.name} estava lendo {self.last_book.name}. Agora está lendo {book.name}.')

        self.last_book = book

o_mundo_assombrado = Book("O Mundo Assombrado")
o_senhor_dos_aneis = Book("O Senhor dos Anéis")
julia = Person("Julia")

julia.read(o_mundo_assombrado)
julia.read(o_senhor_dos_aneis)


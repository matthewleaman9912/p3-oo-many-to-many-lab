class Author:
    
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return[contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return(contract)
    
    def total_royalties(self):
        contracts = [contract.royalties for contract in self.contracts()]
        return(sum(contracts))

class Book:
    
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return[contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return[contract.author for contract in self.contracts()]

class Contract:
    
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        if not isinstance(author, Author):
            raise Exception
        if not isinstance(book, Book):
            raise Exception
        if not isinstance(date, str):
            raise Exception
        if not isinstance(royalties, int):
            raise Exception
  
    @classmethod
    def contracts_by_date(cls, date):
        return[contract for contract in Contract.all if contract.date == date]

        

        
        

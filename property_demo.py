
class Card:
    def __init__(self, rank, suit, first_name, last_name):
        self.rank = rank
        self._suit = suit
        self._first_name = first_name
        self._last_name = last_name


    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def rank(self):  # getter property
        """
        rank of card

        A value from 2 through A (as a string)

        :return _type_: _description_
        """
        return self._rank
    
    @rank.setter
    def rank(self, value):  # setter property
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError(f"rank must be a str, not a {type(value).__name__}")

    # rank = property(rank)   # same as using '@'


    def get_rank(self):
        return self._rank

c1 = Card('8', 'Diamonds', 'John', 'Strickler')
c2 = Card('10', 'Clubs', 'Ferd', 'Berfel')

print(f"{c1._rank = }")

print(f"{c1.get_rank() = }")

print(f"{c1.rank = }")
print(f"{type(c1.get_rank) = }")

print(f"{type(Card.rank) = }")
print(f"{type(c1.rank) = }")

c1.rank = '9'
print(f"{c1.rank = }")

c1.rank = 9.239093023

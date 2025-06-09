class Country:

    def __init__(self, code: str, name: str, population: int = 0):
        self.code = code
        self.name = name
        self.population = population

    def __str__(self):
        return f"Country(code='{self.code}', name='{self.name}', population={self.population})"

class City:

    def __init__(
        self,
        id: int = None,
        name: str = "",
        country_code: str = "",
        population: int = 0,
    ):
        self.id = id
        self.name = name
        self.country_code = country_code
        self.population = population

    def __str__(self):
        return f"City(id={self.id}, name='{self.name}', country_code='{self.country_code}', population={self.population})"

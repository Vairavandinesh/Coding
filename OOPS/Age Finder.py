class Biodata:
    def __init__(self):
        name=None
        country=None
        year_of_birth=None
    def agefinder(self,year_of_birth):
        return 2025-year_of_birth
Harry=Biodata()
print(Harry.agefinder(2004))
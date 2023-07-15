from typing import List, Dict, Tuple
import ID_Functions as IDF



# Function programming
person = IDF.person()
creds = IDF.username_password(person)



class ID:
    def __init__(self) -> dict:
        self.first_name = person["First_Name"]
        self.last_name = person["Last_Name"]
        self.gender = person["Gender"]
        self.username = creds["Username"]
        self.password = creds["Password"]
        self.day = IDF.day()
        self.year = IDF.year()
        self.month = IDF.month()

    def __str__(self):
        gen_id_dict = self.output()
        return f"Generate_ID: {gen_id_dict}"


    """
    Generates exactly one ID
    """
    def generate(self) -> dict:
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "username": self.username,
            "password": self.password,
            "day": self.day,
            "year": self.year,
            "month": self.month
        }


    """
    Returns list of dicts of ID's generated
    by amount chosen.
    """
    def amount(self, amount:int) -> List[dict]:
       return [self.generate() for _ in range(0, amount)]



example = ID().generate()

print(example)





#class Json_Output()




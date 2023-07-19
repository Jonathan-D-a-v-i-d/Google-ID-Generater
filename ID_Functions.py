import random
import calendar
import string
from faker import Faker

# Hello Freaks
#
# This is the function file where all functions are stores and called for seamless 
# object oriented programming later on



#############
# Credentials
#############
class person:
    def __init__(self) -> None:
        # - Creating fake instance
        self.fake = Faker()

        # - Creating three person templates [Type: List[Dict]]
        self.templates = [
            { # Male
            "First_Name" : self.fake.first_name_male(),
            "Last_Name" : self.fake.last_name(),
            "Gender" : "Male"
            },
            { # Female
            "First_Name" :self. fake.first_name_female(),
            "Last_Name" : self.fake.last_name(),
            "Gender" : "Female"
            },
            {# Gen Z
            "First_Name" :self. fake.first_name(),
            "Last_Name" : self.fake.last_name(),
            "Gender" : "Rather not say"
            }
        ]

    def male(self) -> dict:
        # Returns male person template
        male = self.templates[0]
        return male

    def female(self) -> dict:
        # Returns female person template
        female = self.templates[1]
        return female
    
    def gen_z(self) -> dict:
        # Returns gen-z person template
        gen_z = self.templates[2]
        return gen_z


#####################   
# USERNAME & PASSWORD
#####################
def username_password(template) -> dict:
    first_name = template["First_Name"]
    last_name = template["Last_Name"]
    

    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    

    username = ""
    if first_name and last_name:
        # Generating Username Structures so as not to follow a common pattern with Identities
        username_structures = [
        #STRUCTURE 1 --- John.Doe.4578
        [             
        "{first_name}.{last_name}",
        ''.join(random.choices(string.digits, k=4)),
        ],
        #STRUCTURE 2 -- 566.John.Doe
        [    
        ''.join(random.choices(string.digits, k=3)),
        "{first_name}.{last_name}",
        ],
        #STRUCTURE 3 -- 86.John.Doe.67
        [    
        ''.join(random.choices(string.digits, k=2)),
        "{first_name}.{last_name}",
        ''.join(random.choices(string.digits, k=2))
        ],
        #STRUCTURE 4 -- John.77697
        [    
        "{first_name}",
        ''.join(random.choices(string.digits, k=5))
        ],
        #STRUCTURE 4 -- Doe.46896
        [    
        "{last_name}",
        ''.join(random.choices(string.digits, k=5))
        ],
    ]
        # Picking Random Structure From Structures
        for _ in range(len(username_structures)):
            username_structure = random.choice(username_structures)
            username_parts = [part.format(first_name=first_name, last_name=last_name) for part in username_structure]
            username = '.'.join(username_parts)

        obj = {
            "Username" : username,
            "Password" : password
        }

        return obj




###########
# BIRTHDAY
###########
def day ():
    # Gathering List Until 28 Days
    until_28 = [str(x) for x in range(1,28)]
    # Randomly Picking A Day
    day = random.choice(until_28)
    return day

def year ():
    minimum_age_30_max_age_45 = [str(x) for x in range(1978, 1993)]
    year = random.choice(minimum_age_30_max_age_45)
    return year

def month():
    months = list(calendar.month_name)
    months.remove("")
    month = random.choice(months)
    return month




import json
import random
from faker import Faker

fake = Faker("en_US")

def gen_user(quantity: int):
    users = []
    departments = ["Sells", "Engineering", "Marketing", "HR", "Financial"]
    plans = ["Basic", "Standard", "Premium"]
    
    for i in range(1, quantity+1):
        user = {
            "id": i,
            "name": fake.name(),
            "age": random.randint(18, 65),
            "email": fake.email(),
            "salary": round(random.uniform(2500, 15000), 2),
            "department": random.choice(departments),
            "accession_date": fake.date_between(start_date="-3y", end_date="today").isoformat(),
            "active": random.choice([True, False]),
            "plan": random.choice(plans)
        }
        users.append(user)
        
    with open("bigjson.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
        
    print("JSON file generated successfully!")

gen_user(10000)
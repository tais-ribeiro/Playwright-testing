from faker import Faker

fake = Faker()

def generate_random_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone_number": fake.phone_number(),
        "company_name": fake.company(),
        "email": fake.email()
    }

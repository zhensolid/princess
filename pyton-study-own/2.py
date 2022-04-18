from faker import Faker
fake = Faker("zh_CN")
i = 0
for i in range(10):
    print(fake.name(),fake.phone_number(),fake.ssn(min_age=18, max_age=90),fake.address())
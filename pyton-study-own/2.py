from faker import Faker

fake = Faker("zh_CN")
print(fake.profile())
print(fake.address())

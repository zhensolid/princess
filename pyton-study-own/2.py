from faker import Faker
fake = Faker("zh_CN")
i = 0
for i in range(10): #循环10次 获得名字、电弧号码、身份找、地址
    print(fake.name(),fake.phone_number(),fake.ssn(min_age=18, max_age=90),fake.address())
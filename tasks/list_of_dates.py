import datetime
import random_generator

current_date=datetime.date.today()

rand_num = random_generator.generate_random_number(3)

print([(current_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, rand_num+1)])
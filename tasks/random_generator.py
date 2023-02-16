import time

def generate_random_number(seed):
    current_time = time.time()
    random_num = int(current_time / seed) % 10

    if random_num == 0:
        return 1
    else:
        return random_num

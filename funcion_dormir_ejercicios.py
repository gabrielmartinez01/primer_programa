import random
from time import sleep

random_words = ["Hello", "Evening", "Morning", "Nuts", "Skeleton"]
SECONDS_BETWEEN_WORDS = 3
while True:
    sleep(SECONDS_BETWEEN_WORDS)
    print(random.choice(random_words) + " " + random.choice(random_words) + " " + random.choice(random_words) + " ")


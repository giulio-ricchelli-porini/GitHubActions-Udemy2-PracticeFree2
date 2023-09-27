import os
import random

name = os.environ["INPUT_NAME"]
secret = os.environ["INPUT_SECRET"]

print(f"I'm just giving a huge HELLO to {name}"}
print(f"The secret is: {secret}"}
with open(os.environ["GITHUB_OUTPUT"], "a") as o:
    print(f"random_number={random.random()}", file=o)

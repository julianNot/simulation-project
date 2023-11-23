import numpy as np

import numpy as np
import random

def generate_observation_vector():

    carbohydrates = round(random.uniform(0.1, 0.9), 1)
    temperature = random.randint(4, 45)
    competence = random.randint(0, 1000)
    ph = random.randint(0, 9)

    return [carbohydrates, temperature, competence, ph]

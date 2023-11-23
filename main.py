import matplotlib.pyplot as plt
import numpy as np

from Enviroment.Carbohydrate import carbohydrate_adjust
from Enviroment.Competence import competence_adjust
from Enviroment.Enviroment import generate_observation_vector
from Enviroment.PH import ph_adjust
from Enviroment.Temperatura import temperature_adjust
from agent.Bacterium import gompertz_function

valuek = 0.5
valuer = -0.01
values = []
iterations = list(range(1,501))
counter = 0

gompertz_values = []

for _ in iterations:
    values = generate_observation_vector()
    modifications = [
        carbohydrate_adjust(values[0]),
        temperature_adjust(values[1]),
        competence_adjust(values[2]),
        ph_adjust(values[3])
    ]

    kmodification = modifications[0] + modifications[1]
    rmodification = modifications[3] + modifications[2]

    i = gompertz_function(
        5,
        100,
        valuer + rmodification,
        valuek + kmodification,
        2
    )
    print(f"En el tiempo {counter} el cambio para k fue {kmodification} y para r fue {rmodification}")
    counter = counter + 1
    gompertz_values.append(i)


plt.plot(iterations, gompertz_values)
plt.xlabel('Iteración')
plt.ylabel('Valor de la función Gompertz')
plt.title('Poblation')
plt.show()

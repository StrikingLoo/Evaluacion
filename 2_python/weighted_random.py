import random
# version con errores
def weighted_random(values, weights):
    total_weight = sum(weights)
	# normaliza el array de pesos
    acum_weights = [w / total_weight for w in weights[:] ]
    
    for i in range(len(weights)):
        # duplica el array de pesos
        acum_weights[i] += acum_weights[i]
    
    rand = random.random()
    for value, weight in zip(values, acum_weights):
        # devuelve el valor de 'values' que cumpla que su acum_weights correspondiente vale mas que rand. Esto podria no pasar nunca.
        if weight > rand:
            return value

def normalize(weights):
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    return normalized_weights

def weighted_random_correcto(values, weights):
    normalized_weights = normalize(weights)
    rand = random.random()
    accum = 0
    for i, w in enumerate(normalized_weights):
        accum+=w
        if rand <= accum:
            return values[i] 
    #probabilidad 0 de llegar aca si no fuera por error numerico.
    return values[-1]

values = [0,1,2]
weights = [1,2,3]
res = [0,0,0]
for _ in range(1000):
    res[weighted_random_correcto(values, weights)]+=1
print("densidad generada: {}".format(normalize(res)))
print("densidad deseada: {}".format(normalize(weights)))
#IMPORTANTE: Solo va a andar en python3 por el uso de / para division de floats.


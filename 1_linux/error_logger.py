import time
import random
e = 0
while True:
    e+=1
    r = random.random()
    if r > 0.2:
        with open('errors_log', 'a') as log:
            log.write("\n ERROR: {}".format(e))
    time.sleep(5)



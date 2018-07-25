import time
import random
e = 0
while True:
    e+=1
    r = random.random()

    with open('errors_log', 'a') as log:
        if r > 0.4:
                log.write("\n ERROR: {}".format(e))
        else:
                log.write("\n OK: {}".format(e))

    time.sleep(5)



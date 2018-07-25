#El primer argumento es el filename para buscar la palabra Unix
#Si sacaramos el -o, veriamos cada linea en la que aparece la palabra, 
#Sin contar cada aparicion individual.
cat $1|grep -o 'Unix'|wc -l

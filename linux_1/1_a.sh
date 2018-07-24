#El primer argumento es el filename para buscar la palabra Unix
cat $1|grep -o 'Unix'|wc -l

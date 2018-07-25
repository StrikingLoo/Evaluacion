'''
Si entendi bien, nuestros JSON tienen la pinta
{
String : JSON | String | ArrayDeString
}

No me quedo claro si nos llegan en forma de String, o nos llegan como un diccionario con formato.

'''
#Comienzo haciendo la funcion que genera el output deseado, dado un diccionario como input
def print_msg(base, key):

    dott_join = ".".join(base)
    msg = "json_extract(msg, \'${0}.{1}\'),\n".format(dott_join, key)
    print(msg)

#Notese que python itera los dicts en orden alfabetico de las claves, asi que el orden del input no tiene por que preservarse.
# Imprime los mensajes requeridos, dado un JSON en forma de diccionario
def parse_json_dict(json,base = ['']):
    if str(json)==json:
        print_msg(base, json)
    else:
		for key in json:
		    try:
		        v = json[key]
		        print_msg(base, key)
		        parse_json_dict(v, base+[key])
		    except:
		        array = json
		        if array != str(array):
		            leaf = key
		            print_msg(base, leaf)

parse_json_dict({ "a":["de" ,"fg" , "hi", "jk"],
              "and_object":{"pq":"rs", "t":["u","v","w"]},
                  "b":"casd"
                   })




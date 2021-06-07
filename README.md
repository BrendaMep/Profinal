#Proyecto Final.

**Josue Jerezano, Eduado Pozos y Brenda Medina**

El siguiente proyecto implementa el metodo no heuristico, en el cual se estaran ejecutando las busquedas de amplitud, costo uniforme y de profundidad, para ello se seleccionaron algunas ciudades del estado de Veracruz y apartir de la ruta escogida se da un recorrido de acuerdo a sus necesidades.
 Recordemos que la busqueda no heuristica es tambien conocida como busquedas no informadas y son denominadas búsqueda a ciegas, y esto es porque no tienen información suficiente acerca de los estados. 
 
La informacion que se requirio solo fueron las ciudades, el costo de ir a una ciudad a otra y cuales de ellas tienen via de comunicacion. A partir de esta informacion se fueron creando las rutas. 

La ventana principal esta dividida en partes, en el lado izquierdo se encuentran las opciones a seleccionar, las cuales estan en un Qcombox. El primero es selccionar la salida, en el segundo es selecionar el pueblo al que deseamos visitar, despues se encuentra una pequeña descripcion de los formas de viajar, las cuales son amplitud, costo y profundidad.

En la opcion amplitud lo que se tiene es el recorrido mas rapido si es que lo deseas, el costo nos da la ruta con menor gasto si es que deseas viajar y no gastar mucho, por ultimo se muestra la opcion de profundidad, en este caso es una ruta mas larga, si es que se desea pasar por mas ciudades.

Una vez selecionado estas opciones, con el boton de ruta en la parte inferior nos dara una lista donde nos indicara por cuales ciudades debemos ir para llegar a nuestro destino final. En el apartado derecho se muestra un mapa, donde estan localizadas cada ciudad y los caminos que existen entre ciudades.

La funcion de amplitud lo que hace es una vez que tiene la salida y el destino, para la salida se buscaran las ciudades vecinas y a partir de ellos se iran extendiendo los nodos de manera horizontal, sin  repetir ciudades que ya se encuentren en el camino 

# Practica1Bloque4 - Adquisición de datos - IMAT
Creación de un PDF a través de HTML
Autor: Lara Ocón Madrid

En esta Práctica, vamos a aprovechar los dataframes que sacamos en la Practica 2 del Bloque 2 acerca de la Pizzería Maven Pizzas en 2016, para crear una serie de gráficos y más tarde agregarlos a un reporte ejecutivo en PDF.

Las imagenes ya están todas cargadas dentro de la carpeta imagenes, sin embargo, dentro del notebook crear_imagenes.ipynb se puede observar como se han ido creando (La primera parte del notebook sería la práctica 2, como tratamos los datos hasta poder analizarlos, y en la segunda parte ya comenzamos a crear visualizaciones con todos los dataframes que nos hemos ido creando).

Para lanzar el programa, existen dos opciones:

1) Hacerlo via docker: para ello basta con correr los siguientes scripts:

    ./creadocker.sh genera un docker llamado crearpdfp1b4 con las dependencias necesarias
    ./rundocker.sh lanza el docker que tiene el programa. Los pasos son:
    
            Nos aparece el #
            python3 ./crear_pdf.py

            Se genera el fichero correspondiente dentro del docker 
            Saldremos con "exit"
            

2) Hacerlo directamente en la máquina. Es necesario instalarse las librería especificadas en requirements.txt. Una vez hecho esto, podemos ejecutar el programa (para lo que basta con ejecutar python3 ./crear_pdf.py.) y obtendremos como salida reporte_ejecutivo.pdf.

# IDEAM_tratmiento_datos
Convierte las bases de datos diarias dadas por el IDEAM (Instituto de Hidrológica, Meteorologista y Estudios ambientales) en formato Comma Separated Values (CSV) por estaciones. El código genera lo siguiente:

-	Transpone la información para tener una base de datos organizados con una línea de tiempo vertical
-	Archivos CSV que los guarda en distintas carpetas según la variable que contenga, es decir, por ejemplo si hay 3 estaciones limnimetricas con datos de caudal, los datos de caudal de estas 3 estaciones se guardan en la carpeta caudales.
-	Si hay un dato faltante (verifica si hay algo contenido) agrega el valor distintivo “ -9999”, de lo contrario pone el dato que contiene, también identifica los meses en los cuales hay 28, 30 y 31 días y así no agregar intencionalmente este dato lo cual es incorrecto.
-	Genera un archivo txt que contiene el código de la estación y la ruta donde se ubica el archivo, se acumula si la estación contiene más de 1 variable, esto será útil para futuras aplicaciones.

Los archivos se guardan con el nombre de la estación y el código de la misma, en su interior contiene lo siguiente en formato CSV:

Año, mes, dato día 1, dato día 2, dato día 3, dato día 4, dato día ……

Cada salto de línea representa un mes de un año en específico. Además genera un archivo en la carpeta Estaciones que contiene los siguientes datos en formato txt:

Código de estación, ruta de almacenamiento de estación

Esto se añade para futuras aplicaciones.

Convierte archivos en forma de tabla que da el IDEAM al solicitarlos por la página: http://institucional.ideam.gov.co/jsp/loader.jsf?lServicio=Usuarios&lTipo=usuarios&lFuncion=login&. El formato que brinda esta página es el siguiente:
 
                       I D E A M  -  INSTITUTO DE HIDROLOGIA, METEOROLOGIA Y ESTUDIOS AMBIENTALES
                                                                                                              SISTEMA DE INFORMACION
                                    VALORES TOTALES DIARIOS DE PRECIPITACION (mms)                              NACIONAL AMBIENTAL

    FECHA DE PROCESO :  2019/04/29                    ANO  1987                              ESTACION : 21220050  ACEITUNO EL

    LATITUD    0421 N               TIPO EST    PM                   DEPTO      TOLIMA                  FECHA-INSTALACION   1969-ENE
    LONGITUD   7503 W               ENTIDAD     01  IDEAM            MUNICIPIO  IBAGUE                  FECHA-SUSPENSION
    ELEVACION  0680 m.s.n.m         REGIONAL    10  TOLIMA           CORRIENTE  OPIA

************************************************************************************************************************************
          DIA       ENERO *  FEBRE *  MARZO *  ABRIL *  MAYO  *  JUNIO *  JULIO *  AGOST *  SEPTI *  OCTUB *  NOVIE *  DICIE *
************************************************************************************************************************************

           01          .0       .0       .0                .0                                  .0       .0       .0     34.1
           02          .0       .0       .0                .0                                22.0       .0       .0       .0
           03          .0       .0      8.0              38.0                                  .0       .0       .0       .0
           04          .0       .0      5.0                .0                                  .0     38.0       .0      1.7
           05          .0       .0      5.0                .0                                  .0       .0       .0       .6
           06          .0       .0       .0              30.0                                  .0       .0       .0     46.5
           07          .0       .0       .0                .0                                  .0     10.0      8.0       .0
           08          .0       .0       .0                .0                                  .0     10.0       .0       .0
           09          .0      4.0       .0              10.0                                  .0       .0       .0       .3
           10        27.0       .0       .0                .0                                  .0     20.0       .0       .0
           11          .0       .0       .0                .0                                  .0       .0       .0       .0
           12          .0     45.0     12.0                .0                                  .0       .0       .0       .0
           13          .0       .0       .0                .0                                20.0       .0       .0       .0
           14          .0       .0       .0                .0                                28.0       .0       .0       .0
           15          .0       .0     67.0                .0                                  .0     10.0       .0       .0
           16          .0       .0      2.0              25.0                                  .0       .0       .0       .0
           17          .0       .0       .0                .0                                  .0     55.0       .0       .0
           18          .0       .0       .0                .0                                  .0       .0       .0       .0
           19          .0       .0       .0              32.0                                  .0       .0     50.3       .0
           20        37.0       .0       .0              45.0                                  .0     10.0     19.0       .0
           21          .0       .0       .0                .0                                  .0       .0       .0       .0
           22          .0       .0       .0                .0                                20.0     28.0       .0       .0
           23          .0       .0       .0              15.0                                  .0     40.0       .0       .0
           24          .0       .0       .0                .0                                  .0       .0      2.3       .0
           25          .0       .0       .0                .0                                  .0       .0       .0       .0
           26         9.0       .0       .0                .0                                  .0     40.0       .0       .0
           27          .0       .0       .0                .0                                  .0     89.0       .0       .0
           28          .0       .0       .0                .0                                28.0       .0       .0       .0
           29          .0              11.0                .0                                40.0       .0      2.4      6.1
           30          .0                .0                .0                                  .0       .0       .0     20.3
           31          .0                .0                .0                                           .0                .0

    TOTAL                73.0     49.0    110.0    190.3 8  195.0    109.5 8   59.2 8   68.3 8  158.0    350.0     82.0    109.6
    No DE DIAS LLUVIA       3        2        7                 7                                   6       11        5        7
    MAXIMA EN 24 Hrs     37.0     45.0     67.0              45.0                                40.0     89.0     50.3     46.5

    DATOS PRELIMINARES **              ***  VALORES  ANUALES  ***                                           ** ORIGENES DE DATO **

                                     TOTAL                  1553.9                                         8 : EST.  OTROS METODOS
                                     No DE DIAS LLUVIA          48
                                     MAXIMA EN 24 Hrs         89.0


Este ejemplo aplica para cualquier variable que este código pueda hacer (Ver Advertencias). Para poder ejecutar este código es necesario seguir los siguientes pasos:

1.	Tener instalado Python 3.x instalado en su ordenador.
2. Verificar si las variables son continuas, para evitar conflictos entre archivos si se tienen estaciones con variables de distintos años por el documento.
3.	En la primera línea poner un punto (.) con un salto de línea y poner el formato del archivo dado como .txt (por defecto esta como "test.txt").
4.	En la línea 48 ingresar el nombre del archivo con su formato, este debe estar contenido en la misma carpeta (esto se arreglara en futuras versiones).
5.	Tener creadas las carpetas en donde se exportarán las variables (esto se arreglará en otras versiones).
6.	Ejecutar el código.

                                                                        ADVERTENCIA
                                                                        
Este código contiene algunos bugs:

1.	Si hay errores en las tablas (tablas cortadas, incompletas) el programa mandará un error y este se tiene que corregir manualmente, buscando dentro del archivo el conflicto.
2.	Las variables que soporta son: Materiales en suspensión, Brillo solar, Caudales, Sedimentos en suspensión, Evaporación, Humedad relativa, Niveles, Precipitación, Recorrido del viento, Temperatura máxima, Temperatura media y Temperatura mínima. A pesar de que Velocidad del viento si soporta, las tablas no deben contener vectores de velocidad o dirección del viento, el código no tiene soporte para almacenar estos datos. Si aun así insiste en ingresar estos datos, ocurrirá un error de desbordamiento de memoria, además de que no se almacena ninguno de estos datos. No he trabajado con otros tipos de datos así que no sé cómo sea su comportamiento.
3.	No se debe cortar la parte superior de la tabla ni su contenido, el código toma por predeterminado que estos datos están en el mismo orden siempre (por defecto es así). De lo contrario pueden haber errores de desbordamiento de memoria o datos mal exportados.
4.	No tiene en cuenta los años bisiestos, por tanto los datos del 29 de febrero donde cumple esta característica no lo guarda, este error por experiencia no lo considero necesario. 
5.	La interpretación de los datos no son mi responsabilidad, es directamente parte del usuario del código.

Contacto:

Whatsapp: +57 3203633542
Facebook: https://www.facebook.com/parracuesta 

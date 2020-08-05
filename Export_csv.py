import pandas as pd
import numpy as np
#Crea el archivo R_Data_Estaciones, donde borra el contenido dentro
f=open("Estaciones\\R_Data_Estaciones.txt","w")
f.write("")
f.close()
#Funcion para limitar los bucles y evitar errores
def det_mes(mes):
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        dias=31
    if mes==4 or mes==6 or mes==9 or mes==11:
        dias=30
    if mes==2:
        dias=28
    return dias
#Identifica las principales caracteristicas de la tabla
def tab_data(fila):
    a=idtf.iloc[fila+2,0]
    t=a.find("(",64)
    data_basic={}
    data_basic["Variable"]=a[63:t-1]
    #Verifica que temperatura es
    if (data_basic["Variable"]=="TEMPERATURA"):
        if a.find("MINIMOS")>0:
            data_basic["Variable"]=data_basic["Variable"]+" MINIMA"
        if a.find("MAXIMOS")>0:
            data_basic["Variable"]=data_basic["Variable"]+" MAXIMA"
        if a.find("MEDIOS")>0:
            data_basic["Variable"]=data_basic["Variable"]+" MEDIA"
    a=idtf.iloc[fila+3,0]
    ano=float(a[59:63])
    data_basic["Codigo"]=a[104:112]
    data_basic["Nombre"]=a[114:]
    data_est=np.zeros((13,33))
    #Recolectando los datos
    for mes in range(1,13):
        data_est[mes][0]=ano
        data_est[mes][1]=mes
        dias=det_mes(mes)
        for dia in range(9,dias+9):
            a=idtf.iloc[fila+dia+1,0]
            try:
                data_est[mes][dia-7]=float(a[21+9*(mes-1):17+9*(mes)])
            except:
                data_est[mes][dia-7]=-9999.0
    return data_est,data_basic 
#-/-/-/-/-/-/-/-/-/-/-/-/Cambiar "test.txt" con la ruta del archivo los datos almacenados-/-/-/-/-/-/-/-/-/-/-/-/
idtf = pd.read_csv("test.txt",delimiter='\t')  
i=0
p=0
add=0
data_ano,data_est_1=tab_data(i)
data_total=np.zeros((841,33))
#------------Busca linea por linea el inicio de la tabla, esto por los tamaños variados de estas--------
while i<len(idtf):
    a=idtf.iloc[i,0]
    if (a.find("I D E A M")>0):
        data_ano,data_estb=tab_data(i)
        if (data_est_1==data_estb):
            for dia in range(0,33):
                for mes in range(p,p+12):
                    data_total[mes-add][dia]=data_ano[mes-p+1][dia]
        else:
            #--------------------Genera archivo de la estacion-----------------
            f=open("Estaciones\\"+data_est_1["Variable"]+"\\"+data_est_1["Nombre"]+" "+data_est_1["Codigo"]+".csv","w")
            for mes in range(0,p-add):
                dias=(p-add)%12
                for dia in range(0,33):
                    f.write(str(data_total[mes][dia])+",")
                f.seek(0,2)
                size=f.tell()
                f.truncate(size-1)
                f.write("\n")
            f.close()
            #--------------Pega el codigo y la ruta de la estacion--------------
            f=open("Estaciones\\R_Data_Estaciones.txt","a")
            f.write(data_est_1["Codigo"]+",\Estaciones\\"+data_est_1["Variable"]+"\\"+data_est_1["Nombre"]+" "+data_est_1["Codigo"]+".csv\n")
            f.close()
            data_total=np.zeros((841,33))
            data_est_1=data_estb
            add=p
            for dia in range(0,33):
                for mes in range(p,p+12):
                    data_total[mes-add][dia]=data_ano[mes-p+1][dia]
        p=p+12
    i=i+1
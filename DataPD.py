import pandas as pd
import requests
import numpy as np
import creds

tokeninegi = creds.tokeninegi

entidades={"Estados Unidos Mexicanos":-6999300,"Aguascalientes":1,"Baja California":2,"Baja California Sur":3,
           "Campeche":4,"Chiapas":7,"Chihuahua":8,"Ciudad de México":9,"Coahuila de Zaragoza":5,"Colima":6,
           "Durango":10,"Estado de México":15,"Guanajuato":11,"Guerrero":12,"Hidalgo":13,"Jalisco":14,
           "Michoacán de Ocampo":16,"Morelos":17,"Nayarit":18,"Nuevo León":19,"Oaxaca":20,"Puebla":21,
           "Querétaro":22,"Quintana Roo":23,"San Luis Potosí":24,"Sinaloa":25,"Sonora":26,"Tabasco":27,
           "Tamaulipas":28,"Tlaxcala":29,"Veracruz de Ignacio de la Llave":30,"Yucatán":31,"Zacatecas":32}

indi=["Grado promedio de escolaridad 15 años o más","Porcentaje de analfabetas total","Hasta 1 salario mínimo","Más de 1 hasta 2 salarios mínimos",
      "Más de 2 hasta 3 salarios mínimos","Más de 3 hasta 5 salarios mínimos","Más de 5 salarios mínimos",
      "Instrucción media superior 15 años o más","Instrucción superior 15 años o más","Sin escolaridad 15 años o más",
      "Escolaridad básica 15 años o más"]
listanum=[1005000038,3108001001,6200032080,6200032083,6200032086,6200032089,6200032092,6200240314,6200240365,6207019020,6207019031]
lstdfs=[]
lstobs=[]
datepob=["2005","2010","2015","2020"]
datepob=pd.to_datetime(datepob)

#For loop para descargar los datos de cada una de las entidades federativas, descargando desde la api de INEGI
#en formato JSON
for ent in entidades:
    repo_url = 'https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1005000038,3108001001,6200032080,6200032083,6200032086,6200032089,6200032092,6200240314,6200240365,6207019020,6207019031/es/0'+str(7000000+entidades[ent])+'/false/BISE/2.0/131977e4-566f-43f8-8e93-7cebd45807f0?type=json' 
    data = requests.get(repo_url).json()
    repo_urlpob = 'https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000001/es/0'+str(7000000+entidades[ent])+'/false/BISE/2.0/131977e4-566f-43f8-8e93-7cebd45807f0?type=json'
    datapob = requests.get(repo_urlpob).json()

    #Dataframe de la población de cada entidad federativa cada 5 años
    jsondfpob = pd.DataFrame(datapob["Series"][0]["OBSERVATIONS"])
    jsondfpob["TIME_PERIOD"] = pd.to_datetime(jsondfpob["TIME_PERIOD"])
    jsondfpob["OBS_VALUE"]=jsondfpob["OBS_VALUE"].astype(np.float64)
    
    #For loop que crea un dataframe para cada indicador, para los valores que son números en vez de porcentajes se
    #calcula un promedio anual para los 4 trimestres y divide este promedio entre el último dato de población 
    #disponible hasta ese momento. También crea una columna con el nombre del indicador y al final lo agrega
    #a una lista con todos los dataframes de los indicadores de la entidad.
    for j in range(len(data["Series"])):
        obsdf = pd.DataFrame(data["Series"][j]["OBSERVATIONS"])
        obsdf.drop(labels=["OBS_EXCEPTION","OBS_STATUS","OBS_SOURCE","OBS_NOTE","COBER_GEO"],axis=1,inplace=True)
        obsdf = obsdf.dropna()
        obsdf["OBS_VALUE"]=obsdf["OBS_VALUE"].astype(np.float64)
        if obsdf.loc[1,"OBS_VALUE"]>=100 or obsdf.loc[1,"OBS_VALUE"]<=0:
            obsdf["TIME_PERIOD"] = obsdf["TIME_PERIOD"].replace("/[0-9]*","",regex=True)
            obsdf["TIME_PERIOD"] = pd.to_datetime(obsdf["TIME_PERIOD"])
            obsdf = obsdf.groupby(["TIME_PERIOD"]).mean(numeric_only=True)
            obsdf = obsdf.reset_index()
            for i in range(len(datepob)):
                    if i < (len(datepob)-1):           
                        obsval = obsdf.loc[(obsdf["TIME_PERIOD"]>=datepob[i])&(obsdf["TIME_PERIOD"]<datepob[i+1]),"OBS_VALUE"]
                        pobval = jsondfpob.loc[jsondfpob["TIME_PERIOD"]==datepob[i],"OBS_VALUE"].iloc[0]
                        obsdf.loc[(obsdf["TIME_PERIOD"]>=datepob[i])&(obsdf["TIME_PERIOD"]<datepob[i+1]),"OBS_VALUE"] = obsval/pobval
                    else:
                        obsval = obsdf.loc[obsdf["TIME_PERIOD"]>=datepob[i],"OBS_VALUE"]
                        pobval = jsondfpob.loc[jsondfpob["TIME_PERIOD"]==datepob[i],"OBS_VALUE"].iloc[0]
                        obsdf.loc[(obsdf["TIME_PERIOD"]>=datepob[i]),"OBS_VALUE"] = obsval/pobval
        else:
            obsdf["TIME_PERIOD"] = pd.to_datetime(obsdf["TIME_PERIOD"])
            obsdf.loc[:,"OBS_VALUE"]=obsdf.loc[:,"OBS_VALUE"]/100
        obsdf = obsdf.assign(INDICADOR=indi[j])
        lstobs.append(obsdf)
    
    #Concatena los dataframes de los indicadores de la entidad, se le agrega una columna con el nombre de la
    #entidad y agrega esta entidad a una lista con todos los dataframes de las entidades
    jsondf = pd.concat(lstobs, ignore_index=True)
    lstobs=[]
    jsondf = jsondf.assign(ENTIDAD=ent)
    lstdfs.append(jsondf)

#Concatena los dataframes de las entidades y exporta este dataframe final a csv
inegidf=pd.concat(lstdfs, ignore_index=True)
lstdfs=[]
inegidf.to_csv("INEGI_DF.csv",encoding='utf-8', index=False)

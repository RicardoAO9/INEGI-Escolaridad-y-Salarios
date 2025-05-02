# INEGI-Escolaridad-y-Salarios

## Descripción del proyecto
En este proyecto se analiza el nivel de escolaridad y de ingresos de la población mexicana desde el año 2005 hasta la actualidad para poder comprender la relación entre estas dos variables y su comportamiento alrededor de las entidades federativas del país. A partir de este análisis las entidades gubernamentales correspondientes pueden tomar decisiones dirigidas a las entidades relevantes. Se realizó un dashboard dinámico que se puede consultar en el siguiente enlace: https://lookerstudio.google.com/reporting/f187db02-7aef-4fd6-bd5d-a3fa497c321d

## Descripción de los datos 
Se utilizaron datos del Instituto Nacional de Estadística y Geografía (INEGI), los cuales se consultaron a través de la API del banco de indicadores. Se incluyeron datos a nivel nacional y por entidad federativa de los siguientes indicadores:
- Grado promedio de escolaridad de la población de 15 y más años
- Porcentaje de analfabetas total
- Porcentaje de población de 15 años y más sin escolaridad
- Porcentaje de población de 15 años y más con escolaridad básica
- Porcentaje de la población de 15 años y más con instrucción media superior
- Porcentaje de la población de 15 años y más con instrucción superior
- Población ocupada con ingresos de hasta un salario mínimo
- Población ocupada con ingresos de más de 1 hasta 2 salarios mínimos
- Población ocupada con ingresos de más de 2 hasta 3 salarios mínimos
- Población ocupada con ingresos de más de 3 hasta 5 salarios mínimos
- Población ocupada con ingresos de más de 5 salarios mínimos

Cada indicador tiene una temporalidad distinta, partiendo de 1970 a la actualidad. La limpieza y transformación de los datos se realizó usando la herramienta de Pandas en Python.

## Resumen ejecutivo
La capacidad económica de los ciudadanos es una variable multifactorial. Durante los últimos años los niveles de ingresos han bajado drásticamente en todo el país a pesar de un ligero aumento en los niveles de escolaridad, por lo que otros factores como un aumento del salario mínimo por parte del gobierno sin un verdadero aumento en los salarios por parte de las empresas, o el periodo de la pandemia de Covid-19 podrían estar teniendo un mayor impacto.  A pesar de esto, podemos notar una relación entre el nivel de ingresos y el nivel de escolaridad al compararlos por cada uno de los estados. La Ciudad de México y varios estados del norte del país presentan más de un 40% de población con instrucción media superior o instrucción superior y menos de un 20% de población con ingresos de hasta un salario mínimo, mientras que en la mayoría de los estados del suroeste y oriente del país alrededor del 30% de la población posee instrucción media superior o instrucción superior y todos superan el 20% de población con ingresos de hasta un salario mínimo. Son estas últimas regiones en las que debe haber un mayor enfoque para generar un cambio positivo en sus habitantes.

## Insights y análisis

<img width="949" alt="Dashboard1" src="https://github.com/user-attachments/assets/de728898-22ce-4cc6-a652-baccf0865542" />

El grado promedio de escolaridad en México es 9.74, representando que el mexicano promedio termina sus estudios hasta la escuela secundaria. El nivel de escolaridad aumentó ligeramente entre el 2015 y el 2020, aumentando la instrucción superior y la instrucción media superior alrededor de un 3%. Sin embargo, el porcentaje de personas con ingresos de hasta 1 salario mínimo incrementó considerablemente de un 5.86% a un 17.79%, y las que perciben ingresos entre 2 y 3, 3 y 5 y más de 5 salarios mínimos decayeron del 20% al 5% en conjunto aproximadamente.

<img width="330" alt="Regiones1" src="https://github.com/user-attachments/assets/f95a2e2f-e1d0-4bf9-bc3b-827e397cfa6b" />
<img width="330" alt="Regiones2" src="https://github.com/user-attachments/assets/9c890adf-5979-4c69-a582-b790bf258362" />
<img width="330" alt="Regiones3" src="https://github.com/user-attachments/assets/1e890024-e238-4eca-8212-52728dd5a582" />
<img width="330" alt="Regiones4" src="https://github.com/user-attachments/assets/7fbcbc7f-e03f-4e60-b8b6-dcdd00d62891" />
<img width="330" alt="Regiones5" src="https://github.com/user-attachments/assets/47cdfd41-6987-4519-8953-53fad3960080" />

Podemos confirmar la discrepancia entre salarios comparando la tendencia al alza de la población con salarios bajos y la tendencia a la baja en los salarios más altos. Al comparar regiones, el porcentaje de personas que perciben hasta 1 salario mínimo ha aumentado de manera casi paralela entre estas. Sin embargo, al observar ingresos más altos en las últimas dos gráficas podemos observar que la diferencia entre regiones se ha acortado bastante, denotando que el número de personas con niveles de ingresos más altos están disminuyendo alrededor de todo el territorio nacional, aumentando altamente la desigualdad. 

El suroeste (Chiapas, Guerrero y Oaxaca) y el oriente (Hidalgo, Puebla, Tlaxcala y Veracruz) del país aparecen como las regiones con menores ingresos constantemente a través de los años, mientras que el noroeste (Baja California, Baja California Sur, Chihuahua, Durango, Sinaloa y Sonora) y el noreste (Coahuila, Nuevo León y Tamaulipas) se mantienen como las regiones con mayores ingresos.

<img width="338" alt="País1" src="https://github.com/user-attachments/assets/50c22cc4-c672-4d41-a91a-6ba693a0a4cf" />
<img width="339" alt="País2" src="https://github.com/user-attachments/assets/ed095f1e-a853-4955-bc4d-80d121612129" />
<img width="339" alt="País3" src="https://github.com/user-attachments/assets/5d7eb898-79a5-4246-88aa-ea543ad9971e" />
<img width="339" alt="País4" src="https://github.com/user-attachments/assets/255df916-6229-448e-93ab-814296f58af0" />

El estado con menor nivel de escolaridad en el último periodo registrado fue Chiapas con un 13% de personas de 15 años o más sin escolaridad, seguido de los otros dos estados del suroeste: Guerrero (12%) y Oaxaca (10%). Los estados con menor nivel de salarios se concentran más en el oriente, siendo el primero Tlaxcala con un 25% de personas con ingresos de hasta 1 salario mínimo, y Puebla (23%), Veracruz (22%) e Hidalgo (21%) estando dentro de los primeros lugares. Fuera de esta región, Chiapas es el segundo lugar con un resultado del 24%.

En el caso del mayor nivel de escolaridad, la Ciudad de México tiene mucha ventaja con un 35% de personas de 15 años o más con instrucción superior, estando en el segundo lugar Sinaloa y Querétaro con el 27%. Los estados con mayor nivel de salarios son la Ciudad de México con un 2% de personas con ingresos de más de 5 salarios mínimos, Baja California Sur (2%) y Nuevo León (1%). Varios de los estados en este rubro no llegan ni al 1%.

<img width="896" alt="Chiapas" src="https://github.com/user-attachments/assets/938847a1-0031-4325-89a2-47f57224a0cc" />

A pesar de que Tlaxcala sea el primer lugar en personas con ingresos bajos en el último año registrado, Chiapas es el primero si consideramos el promedio de los últimos 20 años, manteniendo constantemente un porcentaje mayor al 10%, y sobrepasando el 20% desde 2022. Aunque el nivel de escolaridad en general aumentó del 2015 al 2020, las personas que solo tiene escolaridad básica siguen conformando más de la mitad de la población del estado, y las personas con escolaridad superior son las mismas que las personas sin escolaridad en 2020. Chiapas también es el estado con el mayor porcentaje de analfabetas del país con 14.84% y el menor grado promedio de escolaridad, la persona promedio no pasa del segundo año de secundaria.

<img width="889" alt="CDMX" src="https://github.com/user-attachments/assets/e939d51f-ab9a-40ec-bb2a-79b9c8cb784f" />

En la Ciudad de México encontramos una gran diferencia en comparación a Chiapas. El porcentaje de analfabetas es mínimo, de 1.48%, y la persona promedio cursa hasta el segundo año de preparatoria. El nivel de escolaridad ha aumentado ligeramente y un tercio de la población mayor a 15 años tiene una instrucción superior y más de la mitad tiene al menos una instrucción media superior. Sin embargo, las personas con ingresos de hasta un salario mínimo también han aumentado de un 3.56% en 2005 a un alarmante 18.30% en 2024.



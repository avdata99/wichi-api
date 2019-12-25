# Pruebas sobre el API de Wichi 

Primeras pruebas luego de analizar el portal de transparencia y ver el API que la página consume.  

Ejecutar pruebas:

```
python3 req.py
```

Este script lee las consultas predefinidas en la [carpeta queries](querires/) y descarga los datos.  

URL base de las llamadas POST **http://wichi.siu.edu.ar/pentaho/plugin/cda/api/doQuery?**.  
Parámetros de ejemplo:
```
"paramprm_ej_academ": 2016,
"path": "/home/SIU-Wichi/Portal Transparencia/cda/5_academica.cda",
"dataAccessId": "tablero_26",
```

Cada archivos CDA en el servidor pentaho define los recursos de datos que serán expuesto en el API REST.  

Documentación del API Pentaho: https://help.pentaho.com/Documentation/8.1/Developer_Center/REST_API  
Archivos CDA (Community Data Access): https://community.hitachivantara.com/s/article/community-data-access  


# 🎮 Pokémon Popularity Analysis 📊

![Pokémon Banner](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png)  

### 🔍 Análisis de la Popularidad Competitiva de los Pokémon en Smogon y VGC

Este proyecto tiene como objetivo analizar la popularidad de los Pokémon en el competitivo, basándose en datos de **Smogon Showdown** y torneos oficiales de **VGC Worlds** de los últimos años. Se han recopilado, limpiado y analizado datos de múltiples fuentes para generar un dataset integral y crear visualizaciones que ayuden a entender tendencias en el metajuego.

## 🚀 Objetivos del Proyecto

✔ **Obtener datos históricos** de Smogon Showdown y torneos oficiales de VGC Worlds.  
✔ **Comparar la popularidad de los Pokémon** entre ambos formatos.  
✔ **Visualizar tendencias** en el uso de Pokémon competitivos a lo largo de los últimos años.  
✔ **Explorar diferencias en popularidad** según categorías como legendarios, tipos y generación.  


## 📂 Estructura del Repositorio




## 📊 Dataset y Fuentes de Datos

Para realizar este análisis, se obtuvieron datos de las siguientes fuentes:

- **Smogon Showdown** (Datos de uso en VGC en formato .txt)
- **VGC World Championships** (2022, 2023 y 2024)
- **PokeAPI** (Características y atributos de los Pokémon)
  
El dataset final se encuentra en `data/pokemon_dataset_full_merged.csv`, donde se han integrado los datos de Smogon y VGC para facilitar su análisis.

## 📈 Análisis Exploratorio y Visualizaciones

Durante el análisis de los datos, se generaron diversas visualizaciones clave:

### 🏆 **Top 10 Pokémon más usados en Smogon y VGC**
📊 Histograma que muestra los Pokémon más frecuentes en cada formato.

### 📌 **Comparación Smogon vs. VGC (Scatter Plot)**
🎯 Gráfico de dispersión que muestra la relación entre el uso en Smogon y en VGC.

### 🔥 **Comparación de los Pokémon más dominantes en cada formato**
📊 Histograma que destaca a los Pokémon más utilizados en cada metajuego.

### 📉 **Relación entre uso en Smogon y VGC Worlds**
🔍 Gráfico de dispersión que revela qué Pokémon tienen mayor presencia en ambos formatos.

### ⚔️ **Comparación de Pokémon con mayores diferencias de uso entre Smogon y VGC**
📊 Histograma que muestra qué Pokémon son populares en un formato pero no en el otro.

### 🏅 **Comparación del uso de Pokémon legendarios vs no legendarios**
🥇 Gráfico de pastel que divide el uso entre legendarios y Pokémon estándar.

### 🌿 **Comparación del uso de Pokémon por tipo (Smogon vs VGC Worlds)**
🔬 Visualización que muestra la diferencia de uso entre los diferentes tipos de Pokémon en ambos formatos.

## 🔧 Instalación y Uso

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. **Clona el repositorio**

   git clone https://github.com/danielsmdev/pokemon-popularity-analysis.git
   
   cd pokemon-popularity-analysis

3. **Instala las dependencias**
4. 
   pip install -r requirements.txt

5. **Ejecuta los notebooks Abre los archivos en notebooks/ y ejecuta los análisis en Jupyter Notebook.**

## 🎯 Conclusiones

✔ **Se han identificado patrones claros** en la popularidad de los Pokémon en ambos formatos.  
✔ **El uso de Pokémon legendarios** es significativamente mayor en **VGC** que en **Smogon**.  
✔ **Existen Pokémon con alto dominio en un formato pero baja presencia en otro**.  
✔ **Se ha logrado construir un dataset unificado** que permite estudiar tendencias en el competitivo.  

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**. Puedes usarlo libremente con atribución. ⚖️  

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el análisis o quieres expandir el dataset, sigue estos pasos:

1. **Haz un fork del proyecto** 🍴
   
2. **Crea una nueva rama**
   
   git checkout -b feature-nueva
   
3. **Realiza tus cambios y haz commit**
   
   git commit -m "Añadir nueva funcionalidad"
   
4. **Haz push a tu fork**
   
   git push origin feature-nueva
   
5. **Abre un Pull Request 📩**

## 📬 Contacto

Si tienes preguntas o sugerencias, puedes contactar conmigo en GitHub

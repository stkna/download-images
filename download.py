import urllib.request
import os

# Nombre del archivo que contiene la lista de URLs
file_name = "lista_urls.txt"

# Crea una carpeta para guardar las imágenes descargadas
if not os.path.exists("imagenes"):
    os.makedirs("imagenes")

# Inicializa el contador en 1
counter = 1

# Abre el archivo en modo lectura
with open(file_name, "r") as f:
    # Lee cada línea del archivo
    for line in f:
        # Elimina el caracter de nueva línea al final de cada línea
        line = line.strip()

        # Si la línea no está vacía
        if line:
            # Genera el nombre de la imagen utilizando el contador
            file_name = f"imagen_{counter}.jpg"

            # Descarga la imagen y la guarda en la carpeta "imagenes"
            urllib.request.urlretrieve(line, "imagenes/" + file_name)

            # Incrementa el contador
            counter += 1

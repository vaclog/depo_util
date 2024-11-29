import os
import time
from datetime import datetime, timedelta

def delete_old_files(folder_path, days):
    """
    Elimina archivos en el directorio especificado que son anteriores a la fecha actual menos X días.

    :param folder_path: Ruta de la carpeta donde buscar los archivos.
    :param days: Número de días a mantener los archivos (archivos más antiguos se eliminarán).
    """
    # Fecha límite
    cutoff_date = datetime.now() - timedelta(days=days)
    
    # Iterar sobre los archivos en la carpeta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Verificar si es un archivo (no carpeta)
        if os.path.isfile(file_path):
            # Obtener la fecha de modificación del archivo
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            # Comparar con la fecha límite
            if file_mod_time < cutoff_date:
                try:
                    # Eliminar archivo
                    os.remove(file_path)
                    print(f"Eliminado: {file_path}")
                except Exception as e:
                    print(f"Error al eliminar {file_path}: {e}")

# Ruta de la carpeta y días a mantener
folder_to_clean = "C:\LOGS"
days_to_keep = 30  # Por ejemplo, mantener archivos de los últimos 30 días

delete_old_files(folder_to_clean, days_to_keep)

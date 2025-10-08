from PIL import Image

def eliminar_fondo_por_color(input_path, output_path, color_fondo_rgb=(255, 255, 255)):
    """
    Elimina el fondo de una imagen PNG basándose en un color sólido.

    Args:
        input_path (str): Ruta de la imagen PNG de entrada.
        output_path (str): Ruta donde se guardará la imagen de salida con fondo transparente.
        color_fondo_rgb (tuple): Una tupla RGB (ej. (255, 255, 255) para blanco) que representa el color del fondo.
    """
    try:
        # Abrir la imagen
        img = Image.open(input_path)
        img = img.convert("RGBA") # Asegurar que la imagen tenga un canal alfa (transparencia)

        # Obtener los datos de los píxeles
        data = img.getdata()

        nuevos_datos = []
        for item in data:
            # Comprobar si el píxel es del color del fondo
            # Se usa un rango de tolerancia para capturar pequeñas variaciones de color
            tolerancia = 10
            if (abs(item[0] - color_fondo_rgb[0]) <= tolerancia and
                abs(item[1] - color_fondo_rgb[1]) <= tolerancia and
                abs(item[2] - color_fondo_rgb[2]) <= tolerancia):
                # Si es el color del fondo, hacerlo transparente (canal alfa en 0)
                nuevos_datos.append((255, 255, 255, 0))
            else:
                # Si no, mantener el píxel como está
                nuevos_datos.append(item)

        # Actualizar la imagen con los nuevos píxeles
        img.putdata(nuevos_datos)

        # Guardar la imagen con fondo transparente
        img.save(output_path, "PNG")
        print(f"¡Imagen guardada en {output_path} con fondo transparente!")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {input_path}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso de la función
# Reemplaza 'imagen_con_fondo.png' con tu archivo
# Reemplaza 'imagen_sin_fondo.png' con el nombre de tu archivo de salida
# y ajusta el color del fondo según tu imagen
# eliminar_fondo_por_color('imagen_con_fondo.png', 'imagen_sin_fondo.png', color_fondo_rgb=(255, 255, 255))
eliminar_fondo_por_color('C:\\Users\\marti\\Desktop\\Curso gob\\Talento Tech Full Stack JS\\Pre-entrega\\imagenes\\Violeta.png', 'Prueba-7.png', color_fondo_rgb=(90, 50,96))
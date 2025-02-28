import random
def generar_insert_sql(nombre_archivo="Data.sql", cantidad=50000): try: with open(nombre_archivo, "w") as archivo: archivo.write("INSERT INTO xprueba.sensor VALUES\n")
        valores_lista = []
        for _ in range(cantidad):
            temp = random.randint(1, 99)
            hr = random.randint(1, 11)
            pat = random.randint(16, 26)
            alt = random.randint(16, 26)
            iuv = random.randint(16, 26)
            lov = random.randint(16, 26)
            loi = random.randint(16, 26)
            pll = random.randint(1, 99)
            vv = random.randint(1, 11)
            dv = random.randint(16, 26)
            nc = random.randint(16, 26)
            il = random.randint(16, 26)
            valores = f"(null, current_timestamp, {temp}, {hr}, {pat}, {alt}, {iuv}, {lov}, {loi}, {pll}, {vv}, {dv}, {nc}, {il}, 1)"
            valores_lista.append(valores)
        archivo.write(",\n".join(valores_lista) + ";\n")
    print("Archivo SQL generado con éxito.")
except Exception as e:
    print(f"Error al escribir el archivo: {e}")
if name == "main": generar_insert_sql()

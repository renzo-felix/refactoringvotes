"Renzo Felix Aponte y Rodrigo Meza Félix Gavilán"
import csv


"""separe la funcion leer documento por que count_votes hacia muchas cosas aparet que en si el leer un texto puede tener muchas fallas """
def leer_documento(file_path )  :
    datos=[]
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            next(reader)  # Skip the header

            for row in reader:
                city = row[0]
                candidate = row[1]
                """ simplificaciond e lugar 
                try:
            	votes = int(row[2])
            except:  
                votes = 0"""
                votes = int(row[2]) if row[2].isdigit() else 0
                datos.append((city, candidate, votes))
    except FileNotFoundError:
        print("el archivo no se encontro en la ruta")
    except csv.Error as e :
        print("error al procesar ",e )

    return datos


"separe la funcion por que mas adelante podria servirme para debugear y por que count_votes tiene muchas responsabilidades  "
def imprimir_votos( results):
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

"separe la funcion por que mas adelante podria servirme para debugear y por que count_votes tiene muchas responsabilidades  "
def imprimir_ganador(results):
    sortedbyvotes = sorted(results.items(), key=lambda item: item[1], reverse=True)
    print(f"winner is {sortedbyvotes[0][0]}")
    return 0

def count_votes(file_path):
    datos = leer_documento(file_path)
    results = {}
    "restructuracion d ela forma de la forma de contar"
    for city, candidate, votes in datos:
        results[candidate] = results.get(candidate, 0) + votes
    imprimir_votos(results)
    imprimir_ganador(results)

# Example usage
count_votes('votes.csv')

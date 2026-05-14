# "¡El apocalipsis zombie ha llegado! Eres el encargado de suministros de un refugio. 
# Tu misión es crear un programa que calcule cuánto tiempo podrá sobrevivir un grupo de personas con los recursos actuales."
# Instrucciones del ejercicio
# Define las siguientes variables con valores inventados:
# personas: Número de personas en el refugio.
# raciones_por_persona: Cuántas raciones come una persona al día.
# total_raciones: Cuántas raciones hay en el almacén en total.
# El programa debe calcular y mostrar:
# Cuántas raciones se consumen en un día en total.
# Para cuántos días exactos alcanza la comida.
# Si cada día se desperdicia un 10% de la comida por culpa de las ratas, ¿cuántas raciones se pierden al día?
# Define las variables
personas = 10
raciones_por_persona = 3
total_raciones = 200
# Calcula el consumo diario total
consumo_diario_total = personas * raciones_por_persona
# Calcula cuántos días exactos alcanza la comida
dias_exactos = total_raciones // consumo_diario_total
# Calcula las raciones perdidas al día por las ratas
raciones_perdidas_diarias = total_raciones * 0.10
raciones= (total_raciones * 10)/100
# Muestra los resultados
print(f"Consumo diario total: {consumo_diario_total} raciones")
print(f"Días exactos que alcanza la comida: {dias_exactos} días")
print(f"Raciones perdidas al día por las ratas: {raciones_perdidas_diarias} raciones")

# ============================================================
#  HDT2 — Parte 5: Integrador  (15 pts)
#  CineData GT 2026 — Sistema de Análisis de Cines
# ============================================================

# ============================================================
#  Sistema de Taquilla — Menú Interactivo
# ============================================================
# Construye un sistema de taquilla interactivo donde TODA la lógica
# esté dentro de funciones. El único código "suelto" permitido es
# la llamada a la función principal al final del archivo.
#
# === DATOS INICIALES ===
# Usa estas variables como datos base. Se pasan como parámetros a
# las funciones, NO como variables globales.
#
# === FUNCIONES REQUERIDAS ===
#
# 1) `mostrar_menu()` — IMPRIME el menú y RETORNA la opción elegida (str).
#
# 2) `mostrar_cartelera(peliculas)` — IMPRIME la cartelera numerada.
#    Formato: "[N] Título (Género) — ★ Rating — QXX.XX"
#    Usa enumerate().
#
# 3) `comprar_entrada(peliculas, compras)` — Pide al usuario:
#    - Número de película (validar rango con while)
#    - Cantidad de entradas
#    Calcula el total (precio * cantidad).
#    Si cantidad > 4, aplica 10% de descuento.
#    Agrega a `compras` una lista: [titulo, cantidad, precio_unitario, total]
#    IMPRIME la confirmación de compra.
#
# 4) `mostrar_compras(compras)` — IMPRIME las compras realizadas.
#    Si no hay compras: "No hay compras registradas."
#    Si hay: tabla con # | Película | Cant | Total
#    Al final, mostrar el gran total.
#    Calcular totales con for (SIN sum()).
#
# 5) `resumen_estadisticas(compras)` — IMPRIME estadísticas:
#    - Total gastado (con for, SIN sum())
#    - Total de entradas compradas (con for, SIN sum())
#    - Compra más cara (con for, SIN max())
#    - Promedio por compra (SIN len() sobre la lista)
#    Si no hay compras: "No hay datos para mostrar."
#
# 6) `sistema_taquilla(peliculas)` — Función principal.
#    Inicializa la lista de compras vacía.
#    Ejecuta el ciclo while con el menú.
#    Llama a las funciones correspondientes según la opción.
#    Opción "5" = salir con mensaje de despedida y total gastado.
#    Opción inválida = "Opción no válida. Intenta de nuevo."
#
# === RESTRICCIONES ===
# - TODA la lógica en funciones (nada suelto excepto la llamada final)
# - NO usar variables globales (todo se pasa por parámetro)
# - SIN usar sum(), max(), min(), len() como built-in
# - SIN librerías externas

# --- Datos iniciales (NO modificar) ---
peliculas = [
    ("Dune: Parte 3", "Sci-Fi", 8.7, 85.0),
    ("Inside Out 3", "Animación", 8.9, 55.0),
    ("Paddington en Guatemala", "Comedia", 9.1, 50.0),
    ("El Contador 3", "Acción", 7.2, 60.0),
    ("Nosferatu 2", "Terror", 6.8, 65.0),
]

# --- Tu código aquí ---

def mostrar_menu():
    print("\n==============================")
    print("            CINEDATA GT 2026")
    print("==============================")
    print("1. Ver cartelera")
    print("2. Comprar entrada")
    print("3. Ver mis compras")
    print("4. Estadísticas")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def mostrar_cartelera(peliculas):
    print("\n=== CARTELERA ===")
    for i, pelicula in enumerate(peliculas, start=1):
        titulo = pelicula[0]
        genero = pelicula[1]
        rating = pelicula[2]
        precio = pelicula[3]
        print(f"[{i}] {titulo} ({genero}) - ★ {rating} - Q{precio:.2f}")

def comprar_entrada(peliculas, compras):
    print("\n=== COMPRAR ENTRADA ===")
    numero = int(input(f"Elige pelicula (1-{len(peliculas)}): "))
    while numero < 1 or numero > len(peliculas):
        numero = int(input(f"Opción inválida. Elige película (1-{len(peliculas)}): "))
    cantidad = int(input("Cantidad de entradas: "))
    titulo = peliculas[numero - 1][0]
    precio_unitario = peliculas[numero - 1][3]
    subtotal = precio_unitario * cantidad
    descuento = 0.0

    if cantidad > 4:
        descuento = subtotal * 0.10
        print("Descuento 10% por volumen (>4 entradas)")
    total = subtotal - descuento
    compras.append([titulo, cantidad, precio_unitario, total])
    if descuento > 0:
        print(f"✓ Compra: {cantidad}x {titulo} - Q{precio_unitario:.2f} c/u - Desc: Q{descuento:.2f} - Total: Q{total:.2f}")
    else:
        print(f"✓ Compra: {cantidad}x {titulo} - Q{precio_unitario:.2f} c/u - Total: Q{total:.2f}")

def mostrar_compras(compras):
    print("\n=== MIS COMPRAS ===")
    if compras == []:
        print("No hay compras registradas.")
        return
    gran_total = 0
    for i, compra in enumerate(compras, start=1):
        titulo = compra[0]
        cantidad = compra[1]
        total = compra[3]
        print(f"#{i} {titulo} | {cantidad} entradas | Q{total:.2f}")
        gran_total += total
    print("---")
    print(f"TOTAL: Q{gran_total:.2f}")

def resumen_estadisticas(compras):
    print("\n=== ESTADÍSTICAS ===")

    if compras == []:
        print("No hay datos para mostrar.")
        return
    total_gastado = 0
    total_entradas = 0
    compra_mas_cara_titulo = compras[0][0]
    compra_mas_cara_total = compras[0][3]
    conteo_compras = 0
    for compra in compras:
        titulo = compra[0]
        cantidad = compra[1]
        total = compra[3]
        total_gastado += total
        total_entradas += cantidad
        conteo_compras += 1
        if total > compra_mas_cara_total:
            compra_mas_cara_total = total
            compra_mas_cara_titulo = titulo
    
    promedio = total_gastado / conteo_compras
    print(f"Total gastado      : Q{total_gastado:.2f}")
    print(f"Total entradas     : {total_entradas}")
    print(f"Compra más cara    : {compra_mas_cara_titulo} (Q{compra_mas_cara_total:.2f})")
    print(f"Promedio por compra: Q{promedio:.2f}")

def sistema_taquilla(peliculas):
    compras = []
    opcion = ""

    while opcion != "5":
        opcion = mostrar_menu()
        if opcion == "1":
            mostrar_cartelera(peliculas)
        elif opcion == "2":
            comprar_entrada(peliculas, compras)
        elif opcion == "3":
            mostrar_compras(compras)
        elif opcion == "4":
            resumen_estadisticas(compras)
        elif opcion == "5":
            total_gastado = 0
            for compra in compras:
                total_gastado += compra[3]
            print(f"¡Gracias por visitar CineData GT! Total gastado: Q{total_gastado:.2f}")
        else:
            print("Opción no válida. Intenta de nuevo.")

sistema_taquilla(peliculas)


# === Ejemplo de interacción esperada ===
#
# ========================================
#        CINEDATA GT 2026
# ========================================
# 1. Ver cartelera
# 2. Comprar entrada
# 3. Ver mis compras
# 4. Estadísticas
# 5. Salir
# Elige una opción: 1
#
# === CARTELERA ===
# [1] Dune: Parte 3 (Sci-Fi) — ★ 8.7 — Q85.00
# [2] Inside Out 3 (Animación) — ★ 8.9 — Q55.00
# [3] Paddington en Guatemala (Comedia) — ★ 9.1 — Q50.00
# [4] El Contador 3 (Acción) — ★ 7.2 — Q60.00
# [5] Nosferatu 2 (Terror) — ★ 6.8 — Q65.00
#
# Elige una opción: 2
# === COMPRAR ENTRADA ===
# Elige película (1-5): 1
# Cantidad de entradas: 6
# Descuento 10% por volumen (>4 entradas)
# ✓ Compra: 6x Dune: Parte 3 — Q85.00 c/u — Desc: Q51.00 — Total: Q459.00
#
# Elige una opción: 2
# === COMPRAR ENTRADA ===
# Elige película (1-5): 3
# Cantidad de entradas: 2
# ✓ Compra: 2x Paddington en Guatemala — Q50.00 c/u — Total: Q100.00
#
# Elige una opción: 3
# === MIS COMPRAS ===
# #1 Dune: Parte 3              | 6 entradas | Q459.00
# #2 Paddington en Guatemala    | 2 entradas | Q100.00
# ---
# TOTAL: Q559.00
#
# Elige una opción: 4
# === ESTADÍSTICAS ===
# Total gastado       : Q559.00
# Total entradas      : 8
# Compra más cara     : Dune: Parte 3 (Q459.00)
# Promedio por compra : Q279.50
#
# Elige una opción: 5
# ¡Gracias por visitar CineData GT! Total gastado: Q559.00

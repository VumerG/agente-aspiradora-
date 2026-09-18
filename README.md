# Agente Aspiradora (Simulación de IA)

Este proyecto en Python simula el comportamiento de un agente inteligente reactivo en un entorno compuesto por dos habitaciones (A y B). El agente percibe el estado actual de la habitación donde se encuentra y toma una decisión según reglas condicionadas.

## Características

* **Entorno de 2 habitaciones:** Maneja los estados Sucia y Limpia.
* **Ciclo de percepción-acción:** Evalúa la habitación actual antes de decidir.
* **Toma de decisiones:**
  * Si la habitación actual está **Sucia** -> la **Limpia**.
  * Si la habitación actual está **Limpia** -> se **Mueve** a la otra habitación.

---

## Estructura del Código

| Método / Sección | Descripción |
| :--- | :--- |
| `__init__()` | Inicializa la posición inicial en "A" y ambas habitaciones como "Sucia". |
| `percibir()` | Retorna el estado de la habitación actual ("Sucia" o "Limpia"). |
| `actuar()` | Determina la acción a ejecutar según el estado percibido. |
| **Bucle Principal** | Ejecuta 6 ciclos de simulación e imprime el estado final. |

---

## Uso e Instalación

1. Clona o copia el código en un archivo llamado `agente_aspiradora.py`.
2. Ejecuta el script con Python 3:

```bash
python agente_aspiradora.py

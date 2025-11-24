# Fundamentos de Inteligencia Artificial - Connect-4

Juan David Cetina, Mariana Salas, Santiago Sabogal

## Descripción

Este proyecto implementa un agente inteligente para el juego Connect-4 basado en aprendizaje por refuerzo con Q-learning tabular.

El agente fue entrenado desde cero jugando 12 000 partidas contra un oponente heurístico fuerte, utilizando exploración UCB (Upper Confidence Bound) para equilibrar explotación de acciones conocidas y exploración de nuevas posibilidades. Tras cada episodio se actualiza la Q-table y, al finalizar el entrenamiento, se guarda el conocimiento aprendido en el archivo connect4_model.json.

La política final del agente combina tres componentes para tomar decisiones óptimas:
- Búsqueda táctica inmediata de victorias y bloqueos forzados.
- Consulta directa a los Q-values aprendidos para estados visitados.
- Heurística de centralidad del tablero como respaldo en estados nunca vistos.

## Requisitos

### Entorno

- Python: Versión 3.13.1 o superior.
- SO: Compatible con Windows, macOS o Linux.

### Dependencias principales

- Numpy
- os
- json

## Guía de uso

### Clonación del repositorio

Clona el repositorio en tu máquina local:
```bash
git clone https://github.com/MariSalas23/Fundamentos-de-IA---Connect4.git
cd Fundamentos-de-IA---Connect4
```

### Instalación de dependencias para usar policy.py

Se debe ejecutar el siguiente comando:

```bash
pip install numpy
```

*Los archivos *policy.py y connect4_model.json son los únicos que se requieren para competir con nuestro agente entrenado**

Existen otros archivos como train_UCB.py que son archivos para entrenar a nuestro modelo, y otros como policy_mcts.py que se tratan de agentes descartados que se usan solo para la comparación en el Notebook.


---


### Dependencias para validaciones

- Matplotlib
```bash
pip install matplotlib
```

- Seaborn (para el mapa de calor)
```bash
pip install seaborn
```
# Fundamentos de Inteligencia Artificial - Connect-4
## Descripción
Este proyecto implementa un agente inteligente para el juego Connect4 basado en aprendizaje por refuerzo con Q-learning tabular.
El agente fue entrenado desde cero jugando 12 000 partidas contra un oponente heurístico fuerte, utilizando exploración UCB (Upper Confidence Bound) para equilibrar explotación de acciones conocidas y exploración de nuevas posibilidades. Tras cada episodio se actualiza la Q-table y, al finalizar el entrenamiento, se guarda el conocimiento aprendido en el archivo connect4_model.json.
La política final del agente combina tres componentes para tomar decisiones óptimas:
- Búsqueda táctica inmediata de victorias y bloqueos forzados.
- Consulta directa a los Q-values aprendidos (para estados visitados.
- Heurística de centralidad del tablero como respaldo en estados nunca vistos.

## Requisitos
### Entorno
- *Python:* Versión 3.8 o superior.
- *SO:* Compatible con Windows, macOS o Linux.

### Dependencias principales
- Numpy
```bash
pip install numpy
```

### Dependencias para validaciones
- Matplotlib
```bash
pip install matplotlib
```
- Seaborn (para el mapa de calor)
```bash
pip install seaborn
```

## Guía de uso
### Clonación del reposotorio
Clona el repositorio en tu máquina local:
```bash
git clone https://github.com/MariSalas23/Fundamentos-de-IA---Connect4.git
cd Fundamentos-de-IA---Connect4
```

### Instalación de dependencias
Ejecuta el comando de instalación mencionado en la sección anterior.

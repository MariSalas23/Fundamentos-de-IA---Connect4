import json
import numpy as np
from connect4.connect_state import ConnectState
from connect4.policy import Policy

# ------------------ RANDOM POLICY ------------------

class RandomPolicy(Policy):
    def mount(self):
        self.rng = np.random.default_rng(911)

    def act(self, s: np.ndarray) -> int:
        available = [c for c in range(7) if s[0, c] == 0]
        return int(self.rng.choice(available))

# ========================= JUGAR UNA PARTIDA =========================

def jugar_partida(policy_red: Policy, policy_yellow: Policy):
    state = ConnectState()

    policy_red.mount()
    policy_yellow.mount()

    while not state.is_final():
        if state.player == -1:
            a = policy_red.act(state.board)
        else:
            a = policy_yellow.act(state.board)

        if not state.is_applicable(a):
            legal = state.get_free_cols()
            if not legal:
                break
            a = legal[0]

        state = state.transition(a)

    return state.get_winner()   # -1, 0, +1

# ========================= TEST A UN AGENTE =========================

def test_agente(nombre, policy_class, n=25):
    print("\n=======================================================")
    print(f"  TEST: {nombre} vs RANDOM")
    print(f"  TOTAL: {n} partidas como ROJO + {n} como AMARILLO")
    print("=======================================================\n")

    agente = policy_class()
    rnd = RandomPolicy()

    stats = {
        "como_rojo": {"ganadas": 0, "perdidas": 0, "empates": 0, "total": n},
        "como_amarillo": {"ganadas": 0, "perdidas": 0, "empates": 0, "total": n}
    }

    # ---------------------------- COMO ROJO ----------------------------
    print(f"\n=========== {nombre} COMO ROJO ===========")
    for i in range(1, n + 1):
        res = jugar_partida(agente, rnd)

        if res == -1:
            stats["como_rojo"]["ganadas"] += 1
            r = "GANÓ"
        elif res == +1:
            stats["como_rojo"]["perdidas"] += 1
            r = "PERDIÓ"
        else:
            stats["como_rojo"]["empates"] += 1
            r = "EMPATÓ"

        print(f"[{nombre} | ROJO] Partida {i}/{n} → {r}")

    # ---------------------------- COMO AMARILLO ----------------------------
    print(f"\n=========== {nombre} COMO AMARILLO ===========")
    for i in range(1, n + 1):
        res = jugar_partida(rnd, agente)

        if res == +1:
            stats["como_amarillo"]["ganadas"] += 1
            r = "GANÓ"
        elif res == -1:
            stats["como_amarillo"]["perdidas"] += 1
            r = "PERDIÓ"
        else:
            stats["como_amarillo"]["empates"] += 1
            r = "EMPATÓ"

        print(f"[{nombre} | AMARILLO] Partida {i}/{n} → {r}")

    # WINRATES
    stats["como_rojo"]["winrate"] = stats["como_rojo"]["ganadas"] / n
    stats["como_amarillo"]["winrate"] = stats["como_amarillo"]["ganadas"] / n

    return stats

# ========================= COMPARACIÓN COMPLETA =========================

if __name__ == "__main__":
    from policy_mcts import MctsUcbPolicy
    from policy import CetinaSalasSabogal   # tu otro agente

    resultados = {
        "MCTS": test_agente("MCTS-UCB1", MctsUcbPolicy, n=25),
        "CETINA": test_agente("CETINA-SALAS-SABOGAL", CetinaSalasSabogal, n=25),
    }

    with open("comparacion_agentes_vs_random.json", "w") as f:
        json.dump(resultados, f, indent=4)

    print("\n=======================================================")
    print(" Resultados guardados en comparacion_agentes_vs_random.json")
    print("=======================================================\n")

    print(json.dumps(resultados, indent=4))
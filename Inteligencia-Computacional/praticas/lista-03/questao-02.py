# ____________________________LETRA A)_______________________________


def get_successors(k):
    """
    Retorna os dois sucessores de um estado k:
    2k e 2k+1
    """
    return [2 * k, 2 * k + 1]


print(f"Sucessores de 1: {get_successors(1)}")
print(f"Sucessores de 3: {get_successors(3)}")
print(f"Sucessores de 7: {get_successors(7)}")

# ____________________________LETRA B)_______________________________


def get_successors(k):
    """Retorna os sucessores 2k e 2k+1."""
    return [2 * k, 2 * k + 1]


def run_bfs(start_node, goal_node):
    """Executa BFS e retorna a ordem de visita."""
    queue = [start_node]
    visited_order = []

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited_order:
            visited_order.append(current_node)

            if current_node == goal_node:
                print(f"BFS: Objetivo {goal_node} encontrado!")
                return visited_order

            for successor in get_successors(current_node):
                if successor <= 15:
                    queue.append(successor)

    return visited_order


def run_dls(start_node, goal_node, limit):
    """Executa DLS e retorna a ordem de visita."""
    visited_order = []

    def recursive_dls(current_node, depth):
        visited_order.append(current_node)

        if current_node == goal_node:
            print(f"DLS: Objetivo {goal_node} encontrado!")
            return "goal_found"

        if depth == limit:
            return "limit_reached"

        for successor in get_successors(current_node):
            if successor <= 15:
                status = recursive_dls(successor, depth + 1)
                if status == "goal_found":
                    return "goal_found"

        return "continue"

    recursive_dls(start_node, 0)
    return visited_order


start = 1
goal = 11
depth_limit = 3

print("--- Executando Busca em Largura (BFS) ---")
bfs_order = run_bfs(start, goal)
print(f"Ordem de visita (BFS): {bfs_order}")

print("\n--- Executando Busca com Profundidade Limitada (DLS) ---")
dls_order = run_dls(start, goal, depth_limit)
print(f"Ordem de visita (DLS, Limite={depth_limit}): {dls_order}")

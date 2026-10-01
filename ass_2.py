tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': 3, 'I': 12, 'J': 8, 'K': 2,
    'L': 4, 'M': 6, 'N': 14, 'O': 5
}

types = {
    'A': 'MAX', 'B': 'MIN', 'C': 'MIN',
    'D': 'MAX', 'E': 'MAX', 'F': 'MAX', 'G': 'MAX'
}

# 1. Minimax алгоритмі
minimax_count = 0

def minimax(node):
    global minimax_count
    minimax_count += 1
    if isinstance(tree[node], int):
        return tree[node]
    
    if types[node] == 'MAX':
        return max(minimax(child) for child in tree[node])
    else:
        return min(minimax(child) for child in tree[node])

# 2. Alpha-Beta алгоритмі
alphabeta_count = 0

def alphabeta(node, alpha, beta, reverse=False):
    global alphabeta_count
    alphabeta_count += 1
    if isinstance(tree[node], int):
        return tree[node]
    
    children = list(reversed(tree[node])) if reverse else tree[node]
    
    if types[node] == 'MAX':
        v = float('-inf')
        for child in children:
            v = max(v, alphabeta(child, alpha, beta, reverse))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = float('inf')
        for child in children:
            v = min(v, alphabeta(child, alpha, beta, reverse))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

# --- Есептеулерді орындау және Нәтижесін шығару ---

# 1. Minimax
minimax_val = minimax('A')

# 2. Alpha-Beta (Солдан оңға қарай)
alphabeta_count = 0
ab_lr_val = alphabeta('A', float('-inf'), float('inf'), reverse=False)
ab_lr_count = alphabeta_count

# 3. Alpha-Beta (Оңнан солға қарай)
alphabeta_count = 0
ab_rl_val = alphabeta('A', float('-inf'), float('inf'), reverse=True)
ab_rl_count = alphabeta_count

# Экранға нәтижелерді шығару:
print(Practice)
print(f"Minimax мәні: {minimax_val}, Бағаланған түйіндер саны: {minimax_count}")
print(f"Alpha-Beta (Солдан оңға) мәні: {ab_lr_val}, Түйіндер саны: {ab_lr_count}, Кесілген түйіндер: {minimax_count - ab_lr_count}")
print(f"Alpha-Beta (Оңнан солға) мәні: {ab_rl_val}, Түйіндер саны: {ab_rl_count}, Кесілген түйіндер: {minimax_count - ab_rl_count}")

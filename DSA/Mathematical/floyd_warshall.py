def floyd_warshall_algorithm(distance, infinty: int) -> None:
    dim = len(distance)
    for k in range(0, dim):
        for i in range(0, dim):
            for j in range(0, dim):
                if distance[i][k] < infinty and distance[k][j] < infinty:
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]


def print_matrix(matrix) -> None:
    dim = len(matrix)
    for i in range(0, dim):
        for j in range(0, dim):
            print(matrix[i][j], end='  ')
        print()


if __name__ == "__main__":
    inf = 1000
    matrix = [
    [  0,   3,   6, inf, inf, inf, inf],
    [  3,   0,   2,  -1, inf, inf, inf],
    [  6,   2,   0,   1,   4,   2, inf],
    [inf,   1,   1,   0,   2, inf,   4],
    [inf, inf,   4,   2,   0,   2,   1],
    [inf, inf,   2, inf,  -2,   0,   1],
    [inf, inf, inf,   4,   1,   1,   0]
    ]
    floyd_warshall_algorithm(matrix, inf)
    print_matrix(matrix)

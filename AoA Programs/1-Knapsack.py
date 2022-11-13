def knapsack(p, w, total_weight):
    result = [0 for _ in range(len(p))]
    k = [[0]*(total_weight+1) for _ in range(len(p)+1)]

    for ix in range(1, len(p)+1, 1):
        for jx in range(1, total_weight+1, 1):
            if jx >= w[ix-1]:
                k[ix][jx] = max(p[ix-1]+k[ix-1][jx-w[ix-1]], k[ix-1][jx])
            else:
                k[ix][jx] = k[ix-1][jx]

    ix, jx = len(p), total_weight
    while(ix > 0 and jx > 0):
        if (k[ix][jx] != k[ix-1][jx]):
            result[ix-1] = 1
            jx = jx - w[ix-1]
        ix -= 1

    return result

# if __file__ == "__main__":
print(knapsack([1,2,5,6], [2,3,4,5], 8))

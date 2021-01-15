def edit_distance(s, t):
    distances  = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    
    for i in range(len(s) + 1):
        distances[i][0] = i
    for j in range(len(t) + 1):
        distances[0][j] = j

    s = "_" + s
    t = "_" + t

    for m in range(1, len(t)):
        for n in range(1, len(s)):
            insertion = distances[n][m - 1] + 1
            deletion  = distances[n - 1][m] + 1
            mismatch  = distances[n - 1][m - 1] + 1
            match     = distances[n - 1][m - 1]
            if s[n] == t[m]:
                distances[n][m] = min(insertion, deletion, match)
            else:
                distances[n][m] = min(insertion, deletion, mismatch)
    
    return distances[len(s) - 1][len(t) - 1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

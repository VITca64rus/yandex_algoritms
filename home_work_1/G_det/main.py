str_data = input()
N, K, M = str_data.split()
N = int(N)
K = int(K)
M = int(M)

result = 0
if M <= K:
    while N >= K:
        kol_zag = int(N / K)
        N_ost = N % K
        kol_det_s_zag = int(K / M)
        izl = K % M
        result += kol_zag * kol_det_s_zag
        N = N_ost + (izl * kol_zag)


print(result)

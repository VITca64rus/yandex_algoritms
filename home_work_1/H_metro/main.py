a = int(input())
b = int(input())
n = int(input())
m = int(input())


f_l_sl = (a+1)*n - a
f_h_sl = (a+1)*n + a

s_l_sl = (b+1)*m - b
s_h_sl = (b+1)*m + b


if s_l_sl>f_h_sl or f_l_sl>s_h_sl:
    print(-1)
else:
    print(max(f_l_sl, s_l_sl),min(f_h_sl,s_h_sl))
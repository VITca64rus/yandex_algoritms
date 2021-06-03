import math
str_data = input()
K1, M, K2, P2, N2 = str_data.split()

def get(K1, M, K2, P2, N2):
    num_room_on_floor = math.ceil(int(K2)/((int(P2)-1)*int(M)+int(N2)))


    if (int(N2) == 1) and (int(P2) == 1):
        if int(int(K2)/int(K1))+1<int(M):
            P1 = 1
        else:
            P1 = 0
        if int(M) == 1 or int(K2)>int(K1):
            N1 = 1
        else:
            N1 = 0
    else:
        P1 = int((int(K1)-1)/(int(M)*num_room_on_floor))+1
        N1 = int((int(K1)-1)%(int(M)*num_room_on_floor)/num_room_on_floor)+1

        if (num_room_on_floor+1)*(int(N2)) > int(K2) and (num_room_on_floor+1)*(int(N2)-1) < int(K2):

            if int((int(K1)-1)%(int(M)*num_room_on_floor)/num_room_on_floor)+1 == int((int(K1)-1)%(int(M)*(num_room_on_floor+1))/(num_room_on_floor+1))+1:
                N1 = int((int(K1)-1)%(int(M)*num_room_on_floor)/num_room_on_floor)+1
            else:
                N1 = 0

            if int((int(K1)-1)/(int(M)*num_room_on_floor))+1 == int((int(K1)-1)/(int(M)*(num_room_on_floor+1)))+1:
                P1 = int((int(K1)-1)/(int(M)*num_room_on_floor))+1
            else:
                P1 = 0


    return (P1, N1)


ret = get(K1, M, K2, P2, N2)

if ret[0] != 0 and ret[1] != 0:
    check = get(K2, M, K1, ret[0], ret[1])
    if (check[0] == int(P2) and check[1] == int(N2)) or int(K2)>int(K1):
        print(ret[0], ret[1])
    else:
        print(-1, -1)
else:
    print(ret[0], ret[1])


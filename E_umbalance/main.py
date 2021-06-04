import math
str_data = input()
K1, M, K2, P2, N2 = str_data.split()

def get(K1, M, K2, P2, N2):
    num_room_on_floor = []
    """
        Узнаем предположительное количесвто квартир на этаже 
        (может быть не один вариант количества - поэтому внесем это в массив)
        Обработаем случай этаж второй квартиры = 1
    """
    result = [0, 0]
    num_room_on_fl = math.ceil(int(K2)/((int(P2)-1)*int(M)+int(N2)))
    num_room_on_floor.append(num_room_on_fl)
    if (N2 == 1) and (P2 == 1):
        if K1<=K2:
            return (1, 1)
        else:
            if math.ceil(K1/K2) <= M:
                result[0] = 1
            else:
                result[0] = 0
            result[1] = 0
    else:
        while (math.ceil(K2 / num_room_on_fl) == N2):
            num_room_on_floor.append(num_room_on_fl)
            num_room_on_fl += 1
        if len(num_room_on_floor) == 0:
            return (-1, -1)

    #print('Кол-во квартир на этаже может быть - ', num_room_on_floor)

        """
            Узнаем подъезд и этаж для каждого варианта кол-ва квартир на этаже
        """

        pods = []
        flors = []
        for num_room in num_room_on_floor:
            pods.append(int((int(K1) - 1) / (int(M) * num_room)) + 1)
            flors.append(int((int(K1)-1)%(int(M)*num_room)/num_room)+1)

        #print('Возможные подъезды - ', pods)
        #print ('Возможные этажи - ', flors)

        if len(set(pods)) == 1:
            result[0] = pods[0]
        else:
            result[0] = 0

        if len(set(flors)) == 1:
            result[1] = flors[0]
        else:
            result [1] = 0

    """
        Частные случаи
    """
    if M==1:
        result[1] = 1;

    return result


ret = get(int(K1), int(M), int(K2), int(P2), int(N2))
if ret[0] != 0 and ret[1] != 0:
    check = get(int(K2), int(M), int(K1), int(ret[0]), int(ret[1]))
    if (check[0] == int(P2) and check[1] == int(N2)) or int(K2)>int(K1):
        print(ret[0], ret[1])
    else:
        print(-1, -1)
else:
    print(ret[0], ret[1])

"""
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
    """

"""
if ret[0] != 0 and ret[1] != 0:
    check = get(K2, M, K1, ret[0], ret[1])
    if (check[0] == int(P2) and check[1] == int(N2)) or int(K2)>int(K1):
        print(ret[0], ret[1])
    else:
        print(-1, -1)
else:
    print(ret[0], ret[1])

"""
linhas = [0, 1, 2, 3, 4]
desenhos = ["  #", "#  ", "###", "# #"]

numeros = input()
nums = list(numeros)

for i in linhas:
    print("")
    for numero in nums:
        if i == 0:
            if numero == "1":
                print(desenhos[0], end="  ")
            elif numero == "4":
                print(desenhos[3], end="  ")
            else:
                print(desenhos[2], end="  ")
        if i == 1:
            if numero == "5" or numero == "6":
                print(desenhos[1], end="  ")
            elif numero == "4" or numero == "8" or numero == "9" or numero == "0":
                print(desenhos[3], end="  ")
            else:
                print(desenhos[0], end="  ")
        if i == 2:
            if numero == "0":
                print(desenhos[3], end="  ")
            elif numero == "1" or numero == "7":
                print(desenhos[0], end="  ")
            else:
                print(desenhos[2], end="  ")
        if i == 3:
            if numero == "8" or numero == "0" or numero == "6":
                print(desenhos[3], end="  ")
            elif numero == "2":
                print(desenhos[1], end="  ")
            else:
                print(desenhos[0], end="  ")
        if i == 4:
            if numero == "1" or numero == "4" or numero == "7" or numero == "9":
                print(desenhos[0], end="  ")
            else:
                print(desenhos[2], end="  ")

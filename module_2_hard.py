num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

otvet = []
delitel = 0
para = 0


for i in num:
#    print(i)
#    print()
delitel = 0
para = 0
    for j in range(2, 21):
        if j > i:
            break
        else:
            print(f'i={i} j={j}')
            delitel = i % j
            if delitel == 0:
                for k in range(1, 10):
                    para = delitel - k



                



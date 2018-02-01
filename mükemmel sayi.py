while True:
    sayi = int(input("Sayi:"))
    toplam=0


    for i in range(sayi-1,0,-1): 
        if sayi%i==0:
            toplam+=i
    if toplam==sayi:
        print(sayi,"Sayisi Mükemmel Sayidir..")
    else:
        print(sayi,"Sayisi Mükemmel Sayi Degil")

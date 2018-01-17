while True:
    sayi = int(input("Sayý:"))
    toplam=0


    for i in range(sayi-1,0,-1): #girilen sayýyý geriye doðru sýralýyacak.
        if sayi%i==0:
            toplam+=i
    if toplam==sayi:
        print(sayi,"Sayýsý Mükemmel Sayýdýr..")
    else:
        print(sayi,"Sayýsý Mükemmel sayý deðil")
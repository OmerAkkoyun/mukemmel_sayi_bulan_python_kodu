while True:
    sayi = int(input("Say�:"))
    toplam=0


    for i in range(sayi-1,0,-1): #girilen say�y� geriye do�ru s�ral�yacak.
        if sayi%i==0:
            toplam+=i
    if toplam==sayi:
        print(sayi,"Say�s� M�kemmel Say�d�r..")
    else:
        print(sayi,"Say�s� M�kemmel say� de�il")
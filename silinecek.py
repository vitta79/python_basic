from silinecekSinif import silineceksinif
test=[
    "Hangisi kahve?\nA) Hot chocolate\nB) Latte\nC) Blacktee\n",
    "Hangisi dizi?\nA) La Casa De Papel\nB) I am the Legend\nC) Mask\n",
    "Hangisi Kore?\nA) Lucifer\nB) Joker\nC) Vincenzo\n"
]
sorular=[
    silineceksinif(test[0],"B"),
    silineceksinif(test[1],"A"),
    silineceksinif(test[2],"C")
]
def soruOynat(gelensoru):
    score=0
    for soru in gelensoru:
        cevap=input(soru.soru+"Cevap: ")
        if cevap==soru.cevap:
            score+=1
    print("Test Sonucu: "+str(score)+" dogru "+str(len(gelensoru)-score)+" yanlis")
soruOynat(sorular)
#Χρησιμοποιείστε τον κώδικα που έχουμε φτιάξει για “21” και
#υπολογίστε σε πόσα από τα 100 παιχνίδια κερδίζει ο πρώτος παίκτης,
#σε πόσα ο δεύτερος, και σε πόσα έχουμε ισοπαλία. Στην συνέχεια,
#πειράξτε το μοίρασμα ώστε ο πρώτος παίκτης να ξεκινάει με 10 ή φιγούρα (J,Q, K)
#και ο δεύτερος ποτέ με 10 ή φιγούρα.
#Υπολογίστε τα νέα στατιστικά για 100 τυχαία παιχνίδια,
#δηλαδή πόσα κερδίζει ο πρώτος παίκτης, πόσα ο δεύτερος, και σε πόσα έχουμε ισοπαλία.



import random
#μεταβλητή για νίκες πρώτου δεύερου και ισοπαλείες
p1=0
p2=0
d=0
for i in range (200):
    #μετά τα 100 παιχνίδια εκχωρούνται οι νίκες του κάθε
    #παίχτη σε νέες μεταβλητές και μηδενίζονται οι υπάρχουσες
    if i==100:
        p1a=p1
        p2a=p2
        da=d
        p1=0
        p2=0
        d=0
    #Δημιουργία τράπουλας
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    #Πρώτος παίχτης
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        
        player1.append(xartia.pop())
        #το i είναι μεταβλητή string
        #μετά το εκατοστό παιχνίδι ισχύει ότι ο πρώτος παίχτης
        #ξεκινάει με 10 η φιγούρα
        if i>"99":
            if player1[0][0]!='Q' and player1[0][0]!='J' and player1[0][0]!='K' and player1[0][0]!=10:
                #αν δεν είναι φιγούρα η 10 η κάρτες επιστρέφουν
                #στην τράπουλα και επιλέγει ξανά χαρτί
                xartia.append(player1[0])
                player1.pop(0)
                random.shuffle(xartia)
        #Υπολογισμός βαθμών
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    #Περίπτωση που ο βαθμός είναι μεγαλύτερος του 21
    if sum1>21:
        p2+=1
    else:
        #Ξεκινά να παίζει ο δεύτερος παίχτης
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            #μετά το εκατοστό παιχνίδι ισχύει ότι ο δεύτερος παίχτης
            #ξεκινάει με αριθμό εκτός του 10
            if i>"99":
                if player2[0][0]=='Q' or player2[0][0]=='J' or player2[0][0]=='K' or player2[0][0]==10:
                    xartia.append(player2[0])
                    player2.pop(0)
                    random.shuffle(xartia)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        #Περίπτωση που ο βαθμός είναι μεγαλύτερος του 21
        if sum2>21:
            sum2=0
        #Αποτελέσματα
        if sum1>sum2:
            p1+=1
        elif sum2>sum1:
            p2+=1
        else:
            d+=1

print("Ta prwta 100 paixnidia exoun apotelesma: o prwtos: ",p1a," o deyteros",p2a," isopaleies",da)
print("Ta alla 100 paixnidia exoun apotelesma:: o prwtos: ",p1," o deyteros",p2," isopaleies",d)


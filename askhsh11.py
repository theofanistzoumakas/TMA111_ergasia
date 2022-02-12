#H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/
#προσφέρει τυχαίους αριθμούς.Χρησιμοποιείστε αρχικά την διεύθυνση
# https://drand.cloudflare.com/public/latest για να βρείτε
#ποιος είναι ο τελευταίος γύρος  και στην συνέχεια πάρτε
#τις τιμές (πεδίο randomness) των 20 τελευταίων γύρων
#μέσα από το https://drand.cloudflare.com/public/{round}.
#Μετατρέψτε αυτές τις τιμές σε ένα δεκαεξαδικό κείμενο
#και υπολογίστε την εντροπία του.
#Η εντροπία υπολογίζεται ως το αρνητικό άθροισμα
#της πιθανότητας εμφάνισης ενός συμβόλου (εδώ δεκαεξαδικού ψηφίου) επί 
#τον λογάριθμο αυτής της πιθανότητας
#(https://en.wikipedia.org/wiki/Entropy_(information_theory))







from urllib.request import Request, urlopen
import json
import urllib
import math




req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

data=data.decode()

d=json.loads(data)

#Εκχώρηση σε μεβλητές τις τιμές randomness και round


n=d["randomness"]
rl=d["round"]
print ("O teleutaios gyros einai o: ",rl)
#μετατροπή του αριθμού σε δεκαεξαδικό
n2=int(n,16)
n3=hex(n2)

#μετατρπή του αριθμού σε κείμενο
n4=str(n3)

for i in range (1,20):
    #Επανάληψη της παραπάνω διαδικασία για άλλες 19 φορές
    #Εύρεση των προηγούμενων 20 τιμών round
    r=d["round"]-i
    #Ενσωμάτωση της παραπάνω μεταβλητής στο κείμενο url
    urll='https://drand.cloudflare.com/public/'+str(r)
    req = Request(urll, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data=data.decode()
    d=json.loads(data)

    n=d["randomness"]
    n2=int(n,16)
    
    n3=hex(n2)
    n32=str(n3)
    n4+=n32
#πίνακας με τα επιπλέων γράμματα που χρησημοποιούνται στον δεκαεξαδικό
letters=["a","b","c","d","e","f"]
#διάσπαση του κειμένου με βάση το 0x
x=n4.split("0x")
#αφαίρεση τυχών κενών
for i in x:
    if i=='':
        x.remove(i)
#λίστα που εκχωρούνται πόσα γράμματα έχει ο κάθε δεκαεξαδικός αριθμός
p_letters=[]
#λίστα που εκχωρείται το μήκος του αριθμού
p_all=[]


for i in x:
    #μεταβλητή που εκχωρεί πόσα γράμματα έχει ο κάθε δεκαεξαδικός
    m=0
    for j in letters:
        #εκχωρεί πόσες φορές έχει το συγκεκριμένο γράμμα ο κάθε δεκαεξαδικός
        g=i.count(j)
        m+=g
    p_letters.append(m)
    p_all.append(len(i))

#υπολογισμός της εντροπίας. Η εντροπία υπολογίζεται ως
#το αρνητικό άθροισμα της πιθανότητας εμφάνισης ενός
#συμβόλου (εδώ δεκαεξαδικού ψηφίου) επί τον λογάριθμο αυτής
#της πιθανότητας
#(https://en.wikipedia.org/wiki/Entropy_(information_theory))    
entropia=0
for i in range (20) :
    pithanothta=p_letters[i]/p_all[i]
    logarithmos=math.log(pithanothta)
    entropia+=pithanothta*logarithmos
entropia=entropia*(-1)
#εμφάνιση αποτελεσμάτων
print("Exei entropia: ",entropia)

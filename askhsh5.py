#Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες.
#Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει
#κείμενο με μόνο πεζά γράμματα (μετατρέπετε τα κεφαλαία σε πεζά) και
#τον κενό χαρακτήρα (space).Αρχικά, χωρείστε αυτό το κείμενο σε λέξεις
#σύμφωνα με το κενό. Στις λέξεις που έχετε υπολογίστε τα ακόλουθα στατιστικά:
#α) ποιες είναι οι δέκα δημοφιλέστερες λέξεις; Αν κάποιες
#εμφανίζονται το ίδιο πλήθος και βγαίνουν παραπάνω από δέκα,
#κρατείστε όποιες νομίζετε εσείς ή στην τύχη.
#β) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων
#που αρχίζουν οι περισσότερες λέξεις; γ) Επαναλάβετε το ίδιο για τρία γράμματα.







import string

#άνοιγμα αρχείου
f = open('two_cities.txt', encoding="utf8")
lista=[]
fores=[]
#για κάθε μία σειρά του κειμένου
for line in f:
    #κάνει όλα τα γράμματα πεζά
    line = line.lower()
    for character in string.punctuation:
        #αφαιρεί σημεία στίξης
        line = line.replace(character, '')
        line=line.replace("«","")
        line=line.replace("»","")
        line=line.replace("\n","")
    #χωρίζει το κείμενο με βάση το κενό και τοποθετεί τις λέξεις σε λίστα
    x=line.split(" ")
    #αν η σειρά δεν είναι κενή να ενσωματώνεται στην λίστα η λίστα x
    if x!=[]:
        lista.extend(x)
#αφαρεί τυχόν επιπλέον κενά
for i in lista:
    if i=='':
        lista.remove(i)
#μετράει πόσες φορές υπάρχει η κάθε λέξη στο κείμενο και προσθέτει
#αυτόν τον αριθμό στην λίστα fores
for i in lista:
    p=lista.count(i)
    fores.append(p)
#ταξινομεί σε φθίνουσα σειρά την λίστα
fores.sort()
fores.reverse()

fores2=[]

#αφαιρεί τους αριθμούς των φορών που είναι παραπάνω απο δύο φορές
for i in fores:
    if i not in fores2:
        fores2.append(i)

lekseis=[]

#ελέγχει αν η κάθε λέξη του κειμένου είναι τόσες φορές όσες
#είναι ο αριθμός της λίστας fores2
for i in range(len(fores2)):
    for j in lista:
        if lista.count(j)==fores2[i] and j not in lekseis:
            lekseis.append(j)

#Τυπώνει τις 10 πρώτες/δημοφιλέστρες λέξεις
print("Oi 10 dhmofilestres lekseis einai: ")
for i in range (10):
    print(lekseis[i])


print("--------------------")


#λίστες που θα εκχωρηθούν οι συνδιαμσοί των δύο και τρίων γραμμάτων
pinakas_me_2_grammata=[]
pinakas_me_3_grammata=[]

#για κάθε μία λέξη την διασπά σε γράμματα  και εκχωρεί σε
# μεταβλητή τα δύο πρώτα γράμματα που θα προστεθεί σε λίστα
for i in lista:
    leksi=list(i)
    #έλεγχος αν είναι η λέξη πάνω από ένα γράμμα
    if len(i)>1:
        grammata2=leksi[0]+leksi[1]
        pinakas_me_2_grammata.append(grammata2)
        #έλεγχος αν είναι πάνω από δύο γράμματα
        if len(i)>2:
            grammata3=leksi[0]+leksi[1]+leksi[2]
            pinakas_me_3_grammata.append(grammata3)
#πίνακας που δείχνει πόσες φορές εμφανίζεται ο συγκεκριμένος συνδοιασμός
fores_2=[]
#μετράει πόσες φορές είναι ο συνδοιασμός και εκχωρεί αυτόν τον αριθμό
#σε λίστα
for i in range (len(pinakas_me_2_grammata)):
    fores=pinakas_me_2_grammata.count(pinakas_me_2_grammata[i])
    fores_2.append(fores)
#πίνακας που δείχνει πόσες φορές εμφανίζεται ο συγκεκριμένος συνδοιασμός
fores_3=[]
#μετράει πόσες φορές είναι ο συνδοιασμός και εκχωρεί αυτόν τον αριθμό
#σε λίστα
for i in range (len(pinakas_me_3_grammata)):
    fores=pinakas_me_3_grammata.count(pinakas_me_3_grammata[i])
    fores_3.append(fores)
#ταξινόμιση των συνδοιασμών με βάση πόσες φορές υπάρχει ο κάθε συνδοιασμός
for i in range(len(pinakas_me_2_grammata)):
    for j in range(len(pinakas_me_2_grammata) - 1):
        if fores_2[j] < fores_2[j+1]:
            fores_2[j], fores_2[j+1] = fores_2[j+1], fores_2[j]
            pinakas_me_2_grammata[j], pinakas_me_2_grammata[j+1] = pinakas_me_2_grammata[j+1], pinakas_me_2_grammata[j]
#ταξινόμιση των συνδοιασμών με βάση πόσες φορές υπάρχει ο κάθε συνδοιασμός
for i in range(len(pinakas_me_3_grammata)):
    for j in range(len(pinakas_me_3_grammata) - 1):
        if fores_3[j] < fores_3[j+1]:
            fores_3[j], fores_3[j+1] = fores_3[j+1], fores_3[j]
            pinakas_me_3_grammata[j], pinakas_me_3_grammata[j+1] = pinakas_me_3_grammata[j+1], pinakas_me_3_grammata[j]

#αφαίρεση επαναλαμβανόμενων συνδοιασμών σε νέα λίστα
array_me_2_grammata=[]
for i in pinakas_me_2_grammata:
    if i not in array_me_2_grammata:
        array_me_2_grammata.append(i)

array_me_3_grammata=[]
for i in pinakas_me_3_grammata:
    if i not in array_me_3_grammata:
        array_me_3_grammata.append(i)
#εμφάνιση αποτελεσμάτων
print("Oi 2 dhmofilesteroi syndoiasmoi twn 2 grammatwn einai: ",array_me_2_grammata[0],",",array_me_2_grammata[1])
print("Oi 2 dhmofilesteroi syndoiasmoi twn 3 grammatwn einai: ",array_me_3_grammata[0],",",array_me_3_grammata[1])

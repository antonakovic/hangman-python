from itertools import count
import random
import time
          
def this_function_put_dashes(i,the_main_random_word,missing_words,word_seperated_in_letters):
    the_word_with_dashes=''
    for char in the_main_random_word:
        if i not in loops:
            the_word_with_dashes+=char
        else:
            the_word_with_dashes+="_"
            missing_words.append(char)
        word_seperated_in_letters.append(char)
        i+=1
    return the_word_with_dashes

def level(x):
    if  x==1:
        return 6
    elif x==2:
        return 4
    elif x==3:
        return 2
    else:
        return 1

words=["ΑΓΑΛΛΙΑΣΗ","ΑΓΓΕΛΛΩ", "ΑΝΑΓΓΕΛΛΩ", "ΑΓΓΕΛΟΣ","ΑΠΑΓΓΕΛΛΩ", "ΠΑΛΙΚΑΡΙ","ΑΔΕΛΦΟΠΟΙΤΟΣ","ΠΕΡΙΒΑΛΛΟΝ","ΑΚΑΤΟΝΟΜΑΣΤΟΣ","ΑΜΠΕΧΟΝΟ",
"ΑΚΡΙΤΟΜΥΘΙΑ","ΑΛΛΗΛΕΓΓΥΗ","ΑΛΛΟΠΡΟΣΑΛΛΟΣ","ΑΛΛΙΩΣ","ΑΛΛΟΙΩΣΗ","ΑΛΟΝΝΗΣΟΣ","ΒΕΡΙΚΟΚΟ","ΒΕΒΑΡΗΜΕΝΟΣ","ΑΜΟΙΒΗ","ΔΥΣΦΗΜΗΣΗ","ΔΙΑΦΗΜΙΣΗ","ΑΝΑΖΩΟΓΟΝΩ",
"ΑΝΑΚΑΙΝΙΣΗ","ΑΝΑΣΤΗΛΩΣΗ","ΑΝΕΛΛΙΠΩΣ","ΑΝΕΞΙΘΡΗΣΚΙΑ","ΑΝΔΡΕΙΑ","ΑΝΙΔΙΟΤΕΛΗΣ","ΑΝΤΙΚΡΙΖΩ","ΑΝΤΙΚΡΙΣΜΑ","ΑΝΤΙΡΡΗΣΗ","ΑΠΡΟΣΚΟΠΤΟΣ", "ΑΣΟΣ","ΠΑΡΑΠΤΩΜΑ","ΒΔΕΛΥΡΟΣ","ΒΛΕΜΜΑ","ΓΙΑΤΡΕΙΑ",
"ΩΦΕΛΩ", "ΩΦΕΛΗΜΑ", "ΩΦΕΛΙΜΟΣ",
"ΩΦΕΛΙΜΙΣΤΗΣ","ΟΦΕΙΛΩ", "ΟΦΕΙΛΗ","ΟΦΕΛΟΣ","ΟΦΕΙΛΕΤΗΣ","ΓΛΑΦΥΡΟΣ","ΔΙΑΡΡΟΗ","ΔΙΑΧΕΙΡΙΣΗ","ΕΓΧΕΙΡΗΣΗ","ΤΑΛΙΡΟ","ΤΑΞΙΔΙ","ΤΕΣΣΕΡΑ","ΤΕΣΣΕΡΙΣ","ΤΕΤΡΙΜΜΕΝΟΣ","ΤΗΒΕΝΝΟΣ","ΤΟΥΑΛΕΤΑ", 
"ΤΥΡΑΝΝΙΑ", "ΤΥΡΑΝΝΟΣ","ΥΠΕΡΗΦΑΝΕΙΑ","ΦΑΚΕΛΟΣ","ΦΑΡΑΓΓΙ","ΧΛΩΜΟΣ","ΨΕΜΑ","ΦΩΡΙΑΜΟΣ","ΧΕΙΜΑΡΡΟΣ","ΧΡΕΟΚΟΠΙΑ","ΧΛΑΜΥΔΑ","ΑΣΥΖΗΤΗΤΙ","ΑΥΘΩΡΕΙ","ΑΥΤΟΛΕΞΕΙ","ΒΙΟΠΟΙΚΙΛΟΤΗΤΑ", 
"ΒΙΟΤΙΚΟΣ", "ΒΙΩΜΑ", "ΒΙΩΜΑΤΙΚΟΣ", "ΒΙΩΣΙΜΟΣ", "ΒΡΑΔΙΑ", "ΒΡΑΔΙΝΟΣ", "ΒΡΑΔΥ", "ΓΡΑΜΜΑΤΕΑΣ", "ΓΡΑΜΜΕΝΟΣ","ΕΛΛΕΙΨΗ", "ΕΛΛΕΙΜΜΑ", "ΕΠΙΡΡΟΗ", "ΕΠΗΡΕΑΖΩ", "ΕΠΗΡΕΙΑ", "ΕΠΙΧΕΙΡΗΣΗ", 
"ΕΠΙΧΕΙΡΗΜΑΤΙΚΟΤΗΤΑ", "ΕΥΡΙΠΙΔΗΣ","ΕΥΡΩΣΤΟΣ","ΕΥΦΥΪΑ","ΕΧΕΓΓΥΟ","ΕΤΑΙΡΕΙΑ","ΕΥΦΥΪΑ","ΚΑΛΛΙΡΡΟΗ", "ΚΑΛΛΙΤΕΧΝΗΣ", "ΚΑΛΛΙΜΑΡΜΑΡΟ", "ΚΑΛΛΙΦΩΝΟΣ", "ΚΑΤΑΡΡΑΚΩΝΩ","ΚΑΤΑΡΡΕΥΣΗ","ΚΑΤΑΡΡΙΠΤΩ",
"ΚΑΤΑΤΕΘΕΙΜΕΝΟΣ", "ΚΛΟΤΣΙΑ", "ΚΡΟΚΟΔΕΙΛΟΣ","ΚΡΥΜΜΕΝΟΣ","ΚΡΥΣΤΑΛΛΟ","ΚΥΠΕΛΛΟ","ΚΥΤΤΑΡΟ", "ΙΔΙΟΡΡΥΘΜΟΣ","ΊΛΙΓΓΟΣ","ΙΣΟΡΡΟΠΙΑ","ΛΑΡΥΓΓΙ","ΛΕΙΤΟΥΡΓΙΑ", "ΜΠΑΛΑ","ΜΥΓΑ","ΜΥΓΙΑΓΓΙΧΤΟΣ",
"ΜΥΤΙΛΗΝΗ", "ΝΕΟΤΕΡΟΣ","ΝΗΠΕΝΘΗΣ","ΝΗΦΑΛΙΟΣ","ΝΙΑΤΑ","ΝΙΩΘΩ"]

missing_words=[]#The word that user have to find
loops=[] #The list that computer replace the words with dashes 
word_seperated_in_letters=[]
print("HELLO. WELCOME TO HANGMAN")
username=input('WHAT IS YOUR NAME ?:')
print("HELLO",username)
difficult=int(input("SELECT THE DIFFICULT OF THE GAME: 1.EASY 2.MEDIUM 3.HARD 4.GODMODE (TYPE EITHER 1 OR 2 OR 3 OR 4 TO SELECT.):"))
the_main_random_word=random.choice(words)
i=0
while i<len(the_main_random_word)//2:
    put_dash=random.randint(0,len(the_main_random_word)-1)
    loops.append(put_dash)
    i+=1
i=0
word_with_dashes=this_function_put_dashes(i,the_main_random_word,missing_words,word_seperated_in_letters)
tries=level(difficult)
print("Here we are. your missing word is ",word_with_dashes)
laps=1
missing_attempts=0
words_or_letters_that_you_said_and_was_false=[]
while missing_attempts!=tries and missing_words!=[]:
    print("ATTEMPT ",laps,"/ MISSING ATTEMPTS: ",missing_attempts,"/",tries)
    print("-----------------------------")
    print(word_with_dashes)
    print("-----------------------------")
    print("~~~~~~~~")
    if words_or_letters_that_you_said_and_was_false==[]:
        print('words or letters that you said and was false: None something yet')
    else:
        print('words or letters that you said and was false:',words_or_letters_that_you_said_and_was_false)
    print("~~~~~~~~")
    user_attempt=input("TAKE A GUESS: ")
    print("...")
    time.sleep(1.5)
    loop2=[]
    the_word_with_dashes=''
    if user_attempt in missing_words:
        counter=missing_words.count(user_attempt)
        for i in range(counter):
            missing_words.remove(user_attempt)
        i=0
        for char in the_main_random_word:
            if user_attempt==the_main_random_word[i] or word_with_dashes[i]==the_main_random_word[i]:
                loop2.append(i)
            i+=1
        
        i=0
        for char in the_main_random_word:
            if i in loop2:
                the_word_with_dashes+=char
            else:
                the_word_with_dashes+="_"
            i+=1
        word_with_dashes=the_word_with_dashes
        print("Your guess is true")    
    else:
        if user_attempt==the_main_random_word:
            missing_words=[]
        else: 
            print("Your guess is false.")
            words_or_letters_that_you_said_and_was_false.append(user_attempt)
            missing_attempts+=1
    laps+=1
    if missing_attempts==tries or missing_words==[]:
        print("-----------------")
        print("GAME OVER")
        print("-----------------")
if missing_attempts==tries:
    print("THE MISSING WORD WAS:",the_main_random_word)
    print("YOU LOSE")
else:
    print("YOU FOUND THE WORD:",the_main_random_word)
    print("YOU WIN")

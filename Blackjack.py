from random import randint

#Tworzenie talii
def card_deck():
       figura = []
       with open('figury.txt') as figury:
           for linia in figury:
               figura.append(linia.strip())
       kolor = []
       with open('kolory.txt') as kolory:
           for linia in kolory:
               kolor.append(linia.strip())
       deck = []
       for i in kolor:
           for j in figura:
               deck.append(j + ' ' + i)
       return deck

#Przypisywanie wartości do karty
#kto: 1-gracz | 2-krupier
def card_value(card,kto):
       if card[:1] in ('W','D','K','1'):
           return int(10)
       elif card[:1] in ('2','3','4','5','6','7','8','9'):
           return int(card[:1])
       elif card[:1] == 'A':
           if kto == 1:
               print ("\n"+ str(card))
               as_wartosc = input("Wybierz wartość asa (1 lub 11): ")
               while as_wartosc !='1' or as_wartosc !='11':
                   if as_wartosc == '1':
                       return int(1)
                   elif as_wartosc == '11':
                       return int(11)
                   else:
                       as_wartosc = input("Wybierz wartość asa (1 lub 11): ")
           elif kto == 2:
               if dealer_total+11<=21:
                   return int(11)
               elif dealer_total+11>21:
                   return int(1)

#Losowanie karty
def new_card(deck):
       return deck[randint(0,len(deck)-1)]

#Usuwanie karty z talii
def remove_card(deck,card):
       return deck.remove(card)

#Rozgrywka
wyniki = []
with open('Wyniki.txt') as tab_wynikowa:
    for linia in tab_wynikowa:
        wyniki.append(linia.strip())
wyniki[0]=int(wyniki[0])
wyniki[1]=int(wyniki[1])
play_again = ''
while play_again != 'EXIT':
       new_deck = card_deck()
       card1 = new_card(new_deck)
       remove_card(new_deck,card1)
       card2 = new_card(new_deck)
       remove_card(new_deck,card2)
       print ("\n" + card1 + " i " + card2)
       value1 = card_value(card1,1)
       value2 = card_value(card2,1)
       total = value1 + value2
       print("Wartość kart w twojej ręce: " + str(total) )

       #Krupier
       dealer_card1 = new_card(new_deck)
       remove_card(new_deck,dealer_card1)
       dealer_card2 = new_card(new_deck)
       remove_card(new_deck,dealer_card2)
       dealer_total=0
       dealer_value1 = card_value(dealer_card1,2)
       dealer_total=dealer_value1
       dealer_value2 = card_value(dealer_card2,2)
       dealer_total = dealer_value1 + dealer_value2

       #Dobieranie i wynik
       czy = 0
       if total == 21:
           print("BLACKJACK!!! Wygrałeś")
           wyniki[0]=wyniki[0]+1
           play_again = input("\nWciśnij ENTER aby kontynuować lub wpisz EXIT aby zakończyć grę\n")
       else:
           print('\nKrupier odsłania jedną kartę')
           print("Jest nią " + dealer_card1 + "\nDruga karta jest zasłonięta")
           while total < 21:
               if czy == 0:
                   pytanie = input("\nDokonaj wyboru (wpisz liczbę)\n1-Dobierz kartę\n2-Nie dobieraj karty\n")
               if pytanie.lower() == '1':
                   more_card = new_card(new_deck)
                   remove_card(new_deck,more_card)
                   more_value = card_value(more_card,1)
                   total += int(more_value)
                   print ("Twoja nowa karta: " + more_card + " \nNowa wartość kart w ręce: " + str(total))
                   if total > 21:
                       print("Przekroczyłeś 21 punktów. Przegrałeś")
                       wyniki[1]=wyniki[1]+1
                       play_again = input("\nWciśnij ENTER aby kontynuować lub wpisz EXIT aby zakończyć grę\n")
                   elif total == 21:
                       print("BLACKJACK!!! Wygrałeś")
                       wyniki[0] = wyniki[0] + 1
                       play_again = input("\nWciśnij ENTER aby kontynuować lub wpisz EXIT aby zakończyć grę\n")
                   else:
                       continue
               elif pytanie.lower() == '2':
                   czy = 1
                   print("Krupier odsłania drugą kartę, którą jest ")
                   print( dealer_card2 + ", więc suma punktów krupiera wynosi " + str(dealer_total))
                   if dealer_total < 17:
                       print("Krupier dobiera karte.")
                       dealer_more = new_card(new_deck)
                       more_dealer_value = card_value(dealer_more,2)
                       print("Nowa karta: " + str(dealer_more))
                       dealer_total += int(more_dealer_value)
                       if dealer_total > 21 and total <=21:
                           print("Krupier ma ponad 21 punktów \nGratulacje, WYGRANA")
                           wyniki[0] = wyniki[0] + 1
                       elif dealer_total < 21 and dealer_total > total:
                           print("Krupier ma " + str(dealer_total) + " punktów. Przegrywasz")
                           wyniki[1] = wyniki[1] + 1
                       else:
                           continue
                   elif dealer_total == total:
                       print("Remis")
                   elif dealer_total < total:
                       print("Wygrywasz")
                       wyniki[0] = wyniki[0] + 1
                   else:
                       print("Przegrywasz")
                       wyniki[1]=wyniki[1]+1
                   play_again = input("\nWciśnij ENTER aby kontynuować lub wpisz EXIT aby zakończyć grę\n")
                   break
print("Dziękuje za gre. Wyniki zostały zapisane do pliku Wyniki.txt")
with open('Wyniki.txt', "w") as podsumowanie:
    podsumowanie.write(str(wyniki[0]))
    podsumowanie.write("\n")
    podsumowanie.write(str(wyniki[1]))
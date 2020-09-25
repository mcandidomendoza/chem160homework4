from cards import *
ntrials=10000
difference=53*[0]
for i in range(ntrials):
    adeck=deck()
    adeck.shuffle()
    bdeck=deck()
    bdeck.shuffle()
    ascore=0
    bscore=0
    while adeck.cardsleft()>0 :
          acard=adeck.dealcard()
          bcard=bdeck.dealcard()
          if acard.value() > bcard.value():
              ascore+=2
          if bcard.value() > acard.value():
              bscore+=2
          if acard.value() == bcard.value():
            ascore+=1
            bscore+=1
    diff=abs(ascore - bscore)
    difference[diff]+=1
for i in range(0,53,2):
    print(i, difference[i]/ntrials)

        
        
    

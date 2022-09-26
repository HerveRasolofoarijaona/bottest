import random

listeS = ['Hey', 'Salut', 'Heyy', 'Coucou'] 
listejust = ['Juste pour te dire que ','Franchement,'] 
listesound =['tes sons','tes musiques']  
listest = ['sont vraiment ','sont '] 
listes = ['incroyable','magnifique','archi lourd'] 
ex = '!' 
listeste = ['Ce serais cool de','Ce serait sympa de','Tu devrais vraiment'] 
listestee = ['les poster','les distribuer']  
sur ='sur' 
listesteee = ['les plateformes de streaming.','Spotify, Napster, Deezer... '] 
listesteeee = ['Il y a','Je connais'] 
compte = '@kicklabel'  
listesteeeee = ['qui le fait','qui te le fait'] 
gratis = 'gratuitement.' 
listesteeeeee = ['tu devrais testé! ','si tu cherches!'] 

#  print(listeS[x]+' '+listejust[y] + ' ' + listesound[z])
# print("------------------------------------------------------------------------------")
# random.shuffle(listejust)

# print("liste originale:", listeS)

fichier = open("infos/messages2.txt", "a")

x=4

while x < 4:
    y = 0
    while y < 2:        
        z=0
        while z < 2:
            a=0
            while a < 2:
                b=0
                while b < 3:
                    c=0
                    while c < 3:
                        d=0
                        while d < 2:
                            e=0
                            while e < 2:
                                f=0
                                while f < 2:
                                    g=0
                                    while g < 2:
                                        h=0
                                        while h <2 :
                                            str = '\n'+listeS[x]+' '+listejust[y] + ' ' + listesound[z] +' '+ listest[a]+''+ listes[b]+' '+ex +' '+ listeste[c]+' '+ listestee[d]+' '+sur+' '+ listesteee[e]+' '+ listesteeee[f]+' '+compte+' '+ listesteeeee[g]+' '+gratis+' '+ listesteeeeee[h]
                                            fichier.write(str)
                                            # print(str)
                                            h=h+1
                                        g=g+1
                                    f=f+1
                                e=e+1
                            d=d+1
                        c=c+1
                    b=b+1
                a=a+1
            z=z+1
        y = y + 1
    x = x + 1

fichier.close()
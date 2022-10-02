import random

listeS = ['Hey', 'Salut', 'Heyy', 'Coucou']
listejust = ['Juste pour te dire que ', 'Franchement,']
listesound = ['tes sons', 'tes musiques']
listest = ['sont vraiment ', 'sont ']
listes = ['incroyable', 'magnifique', 'archi lourd']
ex = '!'
listeste = ['Ce serais cool de', 'Ce serait sympa de', 'Tu devrais vraiment']
listestee = ['les poster', 'les distribuer']
sur = 'sur'
listesteee = ['les plateformes de streaming.', 'Spotify, Napster, Deezer... ']
listesteeee = ['Il y a', 'Je connais']
compte = '@kicklabel'
listesteeeee = ['qui le fait', 'qui te le fait']
gratis = 'gratuitement.'
listesteeeeee = ['tu devrais testé! ', 'si tu cherches!']

fichier = open("infos/messages.txt", "a")

x = 0

while x < 10:
    str_listS = str(random.choice(listeS))
    str_listejust = random.choice(listejust)
    # print(str_listS)
    str_inter = '\n'+str_listS+' '+str_listejust+' '+str(random.choice(listesound))+' '+str(random.choice(listest))+''+str(random.choice(listes))+' '+ex+' '+str(random.choice(listeste))+' '+str(
        random.choice(listestee))+' '+sur+' '+str(random.choice(listesteee))+' '+str(random.choice(listesteeee))+' '+compte+' '+str(random.choice(listesteeeee))+' '+gratis+' '+str(random.choice(listesteeeeee))
    fichier.write(str(str_inter))
    # print(str_inter)
    x = x + 1
fichier.close()

# print('Hey Franchement,tes sons sont magnifique! \n \n Ce serais cool de les poster sur les plateformes de streaming. \n Il y a  @kicklabel  qui te le fait gratuitement . \n tu devrais testé!')


str = 'Hey Juste pour te dire que  tes sons sont vraiment incroyable ! Ce serais cool de les poster sur les plateformes de streaming. Il y a @kicklabel qui le fait gratuitement. tu devrais testé! '

x = str.replace("! ", "!\n")
x = x.replace("gratuitement. ","gratuitement.\n\n")
x = x.replace("Hey ", "Hey\n\n")

print(x)

#  def replaceStr(str):
#         x = str.replace("! ", "!\n")
#         x = x.replace("gratuitement. ","gratuitement.\n\n")
#         x = x.replace("Hey ", "Hey\n\n")
#         x = x.replace("Salut ", "Salut\n\n")
#         x = x.replace("Heyy ", "Heyy\n\n")
#         x = x.replace("Coucou ", "Coucou\n\n")
#         return x
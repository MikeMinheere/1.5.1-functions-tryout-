opnieuw = ''
while opnieuw == '':
    naam = input('wat is uw naam? ')
    leeftijd = input('hoe oud bent u? ')

    def naamEnLeeftijd():
        print('hallo ' + naam + ', uw leeftijd is ' + leeftijd + ' jaar.')
        opnieuw = input("als u opnieuw iets wil invoeren, klik dan op enter, anders kunt u 'stop' typen. ")
        if opnieuw == '':
            print('oke, u gaat nu opnieuw alles invullen.')
        else:return True

    if naamEnLeeftijd() == True:
        break
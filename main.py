userDB="hidrotech123"
passwordDB="admin123*"

print('Software Tech Hidroituango')
print('**************************')
usarName=input('Digita tu usuario: ')
userPassword=input('Digite su contraseña:')

if userDB==usarName and passwordDB==userPassword:
    print('exito en su usuario')
else:
    print('fallaste')

'''print('exito en tu usuario') if userDB==usarName and passwordDB==userPassword else print('fallaste')'''




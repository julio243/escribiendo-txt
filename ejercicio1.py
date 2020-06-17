f = open('archivo.txt','w')
 
lines=[]
op=""
while op !='t':
    if op == 'a':
        line = input("escriba el texto: ")
        lines.append(line + '\n')
    op =input('para añadir  texto (a) o terminar(t) ')
f.writelines(lines)
f.close()
f1 = open('archivo.txt','r')   
print('el texto es: ')

for line in f1:
    print(line)
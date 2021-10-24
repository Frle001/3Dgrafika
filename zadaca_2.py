import math

def coordinates_baza(): 
    l = []
    for i in range (0, 12):
        x = round(math.cos(i*2*math.pi/12), 6)
        y = round(math.sin(i*2*math.pi/12), 6)
        l.append((x,y,0))
    return l

def cordinates_gornja_baza():
    lis=[]
    for i in range (0, 12):
        x = round(math.cos(i*2*math.pi/12), 6)
        y = round(math.sin(i*2*math.pi/12), 6)
        lis.append((x,y,2))
    return lis

def normals_baze (A, z):
    lista = []
    for i in range(0,12):
        Vx = A[i][0]-0
        Vy = A[i][1]-0
        Vz = A[i][2]-z
        normV = math.sqrt(Vx*Vx + Vy*Vy + Vz*Vz)
        lista.append((round(Vx/normV,6),round(Vy/normV,6),round(Vz/normV,6)))
    return lista

def normale_ukoso (A, B):
    listica = []
    for i in range(0,12):
        x = B[i][0] - A[i][0]
        y = B[i][1] - A[i][0]
        z = B[i][2] - A[i][0]
        normaV = math.sqrt(x*x + y*y + z*z)
        listica.append((round(x/normaV,6),round(y/normaV,6),round(z/normaV,6)))
    return listica

def main():
    lista_za_bazu = coordinates_baza()
    lista_za_gr_bazu = cordinates_gornja_baza()
    lista_normala_baze = normals_baze (lista_za_bazu, 0)
    lista_normala_vertikalnih = normale_ukoso(lista_za_bazu,lista_za_gr_bazu)
    f = open("cylinder.obj", "w")
    f.write("v 0 0 0\n")
    for i in range(0, 12):
        f.write("v" + " " + str(lista_za_bazu[i][0]) + " " + str(lista_za_bazu[i][1]) + " " + str(lista_za_bazu[i][2]) + "\n")
    f.write("v 0 0 2\n")
    for i in range(0, 12):
        f.write("v" + " " + str(lista_za_gr_bazu[i][0]) + " " + str(lista_za_gr_bazu[i][1]) + " " + str(lista_za_gr_bazu[i][2]) + "\n")
    f.write("\n")
    f.write("vn 0 0 1\n")
    f.write("vn 0 0 -1\n")
    for i in range (0,12):
        f.write("vn " + str(lista_normala_baze[i][0]) + " " + str(lista_normala_baze[i][1]) + " " + str(lista_normala_baze[i][2]) + "\n")
    for i in range (0,12):
        f.write("vn " + str(-lista_normala_baze[i][0]) + " " + str(-lista_normala_baze[i][1]) + " " + str(-lista_normala_baze[i][2]) + "\n")
    for i in range (0,12):
        f.write("vn " + str(lista_normala_vertikalnih[i][0]) + " " + str(lista_normala_vertikalnih[i][1]) + " " + str(lista_normala_vertikalnih[i][2]) + "\n")
    for i in range (0,12):
        f.write("vn " + str(-lista_normala_vertikalnih[i][0]) + " " + str(-lista_normala_vertikalnih[i][1]) + " " + str(-lista_normala_vertikalnih[i][2]) + "\n")
    f.write("\n")
    """
    tocka = 1
    tocka2 = 2
    tocka3 = 3
    for i in range(0,11):
        f.write("f " + str(tocka) + "/" + str(tocka2) + "/" + str(tocka3) + "\n")
        tocka2 += 1
        tocka3 += 1
    f.write("f 1/13/2\n")
    tocka=14
    tocka2 = 15
    tocka3 = 16
    for i in range(0,11):
        f.write("f " + str(tocka) + "/" + str(tocka2) + "/" + str(tocka3) + "\n")
        tocka2 += 1
        tocka3 += 1
    f.write("f 14/26/15\n")
    tocka = 2
    prevtocka = 2
    tocka2 = 15
    tocka3 = 16
    for i in range(0,11):
        f.write("f " + str(tocka) + "/" + str(tocka2) + "/" + str(tocka3) + "\n")
        prevtocka = tocka
        tocka += 1
        f.write("f " + str(tocka3) + "/" + str(prevtocka) + "/" + str(tocka) + "\n")
        tocka2 += 1
        tocka3 += 1
    f.write("f 13/26/15\n")
    f.write("f 15/13/2\n")"""
    f.close()


if __name__ == "__main__":
    main()
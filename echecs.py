echiquier = []  # contient les colonnes
for i in range(8):
    echiquier.append(8*['*'])


def pos_vers_coord(c, l):
    # E -> 4 et 1 -> 7
    
    return (7-"12345678".index (l),"ABCDEFGH".index (c))

def modif_echiquier(echiquier, pos_l, pos_c, piece):
    coord_l, coor_c = pos_vers_coord(pos_l, pos_c)
    echiquier[coord_l][coor_c] = piece
    return echiquier

echiquier = modif_echiquier(echiquier, 'E', '1', 'k')
echiquier = modif_echiquier(echiquier, 'D', '1', 'q')
echiquier = modif_echiquier(echiquier, 'A', '1', 't1')
echiquier = modif_echiquier(echiquier, 'B', '1', 'h1')
echiquier = modif_echiquier(echiquier, 'C', '1', 'c1')
echiquier = modif_echiquier(echiquier, 'H', '1', 't2')
echiquier = modif_echiquier(echiquier, 'G', '1', 'h2')
echiquier = modif_echiquier(echiquier, 'F', '1', 'c2')

echiquier = modif_echiquier(echiquier, 'E', '2', 'p5')
echiquier = modif_echiquier(echiquier, 'D', '2', 'p4')
echiquier = modif_echiquier(echiquier, 'A', '2', 'p1')
echiquier = modif_echiquier(echiquier, 'B', '2', 'p2')
echiquier = modif_echiquier(echiquier, 'C', '2', 'p3')
echiquier = modif_echiquier(echiquier, 'H', '2', 'p8')
echiquier = modif_echiquier(echiquier, 'G', '2', 'p7')
echiquier = modif_echiquier(echiquier, 'F', '2', 'p6')


echiquier = modif_echiquier(echiquier, 'E', '8', 'Q')
echiquier = modif_echiquier(echiquier, 'D', '8', 'K')
echiquier = modif_echiquier(echiquier, 'A', '8', 'T1')
echiquier = modif_echiquier(echiquier, 'B', '8', 'H1')
echiquier = modif_echiquier(echiquier, 'C', '8', 'C1')
echiquier = modif_echiquier(echiquier, 'H', '8', 'T2')
echiquier = modif_echiquier(echiquier, 'G', '8', 'H2')
echiquier = modif_echiquier(echiquier, 'F', '8', 'C2')

echiquier = modif_echiquier(echiquier, 'E', '7', 'P5')
echiquier = modif_echiquier(echiquier, 'D', '7', 'P4')
echiquier = modif_echiquier(echiquier, 'A', '7', 'P1')
echiquier = modif_echiquier(echiquier, 'B', '7', 'P2')
echiquier = modif_echiquier(echiquier, 'C', '7', 'P3')
echiquier = modif_echiquier(echiquier, 'H', '7', 'P8')
echiquier = modif_echiquier(echiquier, 'G', '7', 'P7')
echiquier = modif_echiquier(echiquier, 'F', '7', 'P6')


                 
<TABLE BORDER="9"> 
  <CAPTION> Echec </CAPTION> 
  <TR> 
 <TH> Titre A1 </TH> 
 <TH> Titre A2 </TH> 
 <TH> Titre A3 </TH> 
 <TH> Titre A4 </TH> 
  </TR> 
  <TR> 
 <TH> Titre B1 </TH> 
 <TD> Valeur B2 </TD> 
 <TD> Valeur B3 </TD> 
 <TD> Valeur B4 </TD> 
  </TR> 
</TABLE> 
                 
for x in range(8):
    print(echiquier[x])

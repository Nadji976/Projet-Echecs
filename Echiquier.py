import http.server
import urllib.parse

ENTETE = '''<!DOCTYPE html>
<html>
    <head>
        <title>Où apparaît ce titre ?</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    <body>'''
PIED = '''</body></html>'''
FORMULAIRE = '''<form action="/" method="get">
    <input type="text" name="ld"/>
    <input type="text" name="cd"/>
    <input type="text" name="la"/>
    <input type="text" name="ca"/>
    <input type="submit" />
    </form>'''

echiquier = []  # contient les colonnes
for i in range(8):
    echiquier.append(8*['*'])

def pos_vers_coord(c, l):
    # E -> 4 et 1 -> 7
    return (7-"12345678".index (l),"ABCDEFGH".index (c))

def modif_echiquier(echiquier, pos_l, pos_c, piece):
    coord_l, coor_c = pos_vers_coord(pos_l, pos_c)
    echiquier[coord_l][coor_c] = piece

modif_echiquier(echiquier, 'E', '1', 'k')
modif_echiquier(echiquier, 'D', '1', 'q')
modif_echiquier(echiquier, 'A', '1', 't1')
modif_echiquier(echiquier, 'B', '1', 'h1')
modif_echiquier(echiquier, 'C', '1', 'c1')
modif_echiquier(echiquier, 'H', '1', 't2')
modif_echiquier(echiquier, 'G', '1', 'h2')
modif_echiquier(echiquier, 'F', '1', 'c2')

modif_echiquier(echiquier, 'E', '2', 'p5')
modif_echiquier(echiquier, 'D', '2', 'p4')
modif_echiquier(echiquier, 'A', '2', 'p1')
modif_echiquier(echiquier, 'B', '2', 'p2')
modif_echiquier(echiquier, 'C', '2', 'p3')
modif_echiquier(echiquier, 'H', '2', 'p8')
modif_echiquier(echiquier, 'G', '2', 'p7')
modif_echiquier(echiquier, 'F', '2', 'p6')


modif_echiquier(echiquier, 'E', '8', 'Q')
modif_echiquier(echiquier, 'D', '8', 'K')
modif_echiquier(echiquier, 'A', '8', 'T1')
modif_echiquier(echiquier, 'B', '8', 'H1')
modif_echiquier(echiquier, 'C', '8', 'C1')
modif_echiquier(echiquier, 'H', '8', 'T2')
modif_echiquier(echiquier, 'G', '8', 'H2')
modif_echiquier(echiquier, 'F', '8', 'C2')

modif_echiquier(echiquier, 'E', '7', 'P5')
modif_echiquier(echiquier, 'D', '7', 'P4')
modif_echiquier(echiquier, 'A', '7', 'P1')
modif_echiquier(echiquier, 'B', '7', 'P2')
modif_echiquier(echiquier, 'C', '7', 'P3')
modif_echiquier(echiquier, 'H', '7', 'P8')
modif_echiquier(echiquier, 'G', '7', 'P7')
modif_echiquier(echiquier, 'F', '7', 'P6')

def to_html(echiquier):
    html = '''<TABLE BORDER="9">
  <CAPTION> Echiquier </CAPTION>'''
    for i in range(8):
        html = html + "<TR>\n"
        for j in range(8):
            piece = echiquier[i][j]
            html = html + "<TD>" + piece + "</TD>\n"
        html = html + "</TR>\n"
    html = html + '''
</TABLE>  '''
    return html

def deplacer(echiquier, pos_l, pos_c, pos2_l, pos2_c):
    coord_l, coor_c = pos_vers_coord(pos_l, pos_c)
    piece = echiquier[coord_l][coor_c]  
    modif_echiquier(echiquier, pos2_l, pos2_c, piece)
    modif_echiquier(echiquier, pos_l, pos_c, '*')

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/style.css':
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            file = open("style.css", "r")
            style = file.read()
            self.wfile.write(bytes(style, 'UTF-8'))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Écriture du contenu de la réponse.
            html = ENTETE
            html = html + FORMULAIRE
            if '?' in self.path:
                path, query_string = self.path.split('?', 1)
                params = urllib.parse.parse_qs(query_string)
                deplacer(echiquier ,params['ld'][0], params['cd'][0], params['la'][0],params['ca'][0])
            html = html + to_html(echiquier)
            html = html + '<a href="raz">Réinitialiser</a>'
            self.wfile.write(bytes(html, 'UTF-8'))

s = http.server.HTTPServer(("localhost", 8000), TestHandler)
print("Starting server. Ctrl+C to quit.")
s.serve_forever()

__author__ = "Sehrum"
__date__ = "$17 mars 2015 14:45:04$"

def constructionArbrePrefixe(seq,k):
    print (coucou);
    print (bastien);
    



def inserer(Arb,mot):
    print (mot[len(mot)-1]);
    if mot[len(mot)-1] != '$':
        mot = mot+'$';
    if len(mot)>0:
        if Arb=={}:
            res={'val':mot[0],'FG':{},'FD':{}};
            res['FG']=inserer({},mot[1:]);
        else:
            if mot[0]<Arb['val']:
                res={'val':mot[0],'FG':{},'FD':Arb};
                res['FG']=inserer(res['FG'], mot[1:]);
            elif mot[0]==Arb['val']:
                res=Arb;
                res['FG']=inserer(res['FG'],mot[1:]);
            else: #mot[0]>Arb['val']
                res=Arb;
                res['FD']=inserer(res['FD'],mot);
    else:
        res={};
    return res;

def affichageArbreSuffixe (Arb):
    if (Arb!={}):
        affichage(Arb['FG']);
        affichage(Arb['FD']);
        print (Arb['val']);
__author__ = "Sehrum"
__date__ = "$17 mars 2015 14:45:04$"

def constructionArbrePrefixe(seq,k):
    
    seqList=[];
    j=0;
    for i in seq:
        seqList.append(j);
        if j!=len(seq):
            if j<k :
                seqList[j]=seq[0:j+1];
            else:
                seqList[j]=seq[j+1-k:j+1];
        else:
            exit;
        j=j+1;
    return (seqList);
            
seqList=constructionArbrePrefixe("ATGCA",3);
print(seqList);
# -*- coding:Utf-8 -*-
import sys, os, os.path
os.chdir('/Users/raoul/Documents/slib-lewis/')

les_zeros=["","0","0.","0:"]
les_deux=["","2","2.","2:"]
les_quatres=["","4","4.","4:"]
les_six=["","6","6.","6:"]
#elements=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
elements=["X","?","K","Ca"]

filename = 'lewis'
opfile = filename + '.tex'
with open('lewis.txt', 'r',encoding='utf-8') as fichier_preambule:
    preambule = fichier_preambule.read()

i=0
for element in elements:
    for zero in les_zeros:
        for deux in les_deux:
            for quatre in les_quatres:
                for six in les_six:
                    i=i+1
                    formule=zero+deux+quatre+six
                    print("\n\n\n\n",i,":",formule,"\n\n\n\n")
    
                    with open('lewis.tex', 'w',encoding='utf-8') as outfile:
                        for ligne in preambule:
                            outfile.writelines(ligne)
                        outputname="lewis{"+formule+","+element+"}"
                        formule="\n\\"+outputname
                        outfile.writelines(formule)
                        outfile.writelines("\n\end{document}")
                        outfile.close()
                    os.system("/usr/local/texlive/2015/bin/universal-darwin/xelatex "+opfile)
                    os.rename("lewis.pdf",outputname+".pdf")

    
    

    
    
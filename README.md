# slib-lewis

Représentation de Lewis pour wims

Permet d'affichier des fichiers lewis.pdf contenant la représentation de Lewis des 20 premiers éléments du tableau périodique.
Chaque fichier fait un peu moins de 2K et a été généré par le script python lewis.py qui fait appel au package chemfig de Christian Tellechea pour LaTeX. Des fichiers associés aux éléments fictifs "X" et "?" ont également été générés.

L'ensemble des fichiers lewis.pdf est à placer dans un dossier "lewis" dans la partie "data" des "scripts" wims : 
/var/lib/wims/public_html/scripts/data/lewis

Changer ensuite les permissions pour qu'elles soient identiques à celle des autres data.


La syntaxe s'inpire de celle donnée dans la documentation de chemfig: lewis[n1 n2 ... ni,atome]
où les n1...ni représentent les positions (en multiples de 45°) désirées autour de l’atome. Ces entiers doivent être compris entre 0 et 7.
Si au lieu d’une paire représentée par une ligne, on souhaite deux points, on fait suivre l’entier par « : ».
Si on veut dessiner un électron, il suffit de le faire suivre par un « . ». Exemple: \lewis[0.2.4.6.,C]
Seuls les entiers pairs (angles de 90°) ont été générés par le script lewis.py



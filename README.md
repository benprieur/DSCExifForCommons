# DSCExifForCommons

Ce code ajoute le paramètre "heading:" au template "Location dec" à une image de Wikimedia Commons issue d'une catégorie donnée.

Pour cela :
- On récupère les données EXIF de l'image en ligne ;
- On vérifie que GPSImgDirectionRef = 'T' ("vrai Nord) et non 'M' (Nord magnétique). Dans ce dernier cas, on ne fait rien ;
- On récupère la direction DSC dans GPSImgDirection que l'on place dans le nouveau paramètre "heading:" ;
- On sauve la page modifiée.

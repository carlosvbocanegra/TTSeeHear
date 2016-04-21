***********README**************

Pasos
Reinstalar foox

$cd foox-master
Desintalar foox:
$sudo python setup.py install --record files.txt
 # inspect files.txt to make sure it looks ok. Then:
$tr '\n' '\0' < files.txt | xargs -0 sudo rm -f --


Correr SeeHearMain

$ python SeeHearMain.py -i lisa.jpg -e 'Serenidad' -o 0

-i inputfile (imagen de entrada)
-e emotion (emoción devulta por la red neuronal)
-o instropt (Opción de instrumento: 0=all instruments, 1=no chords, 2=just piano)

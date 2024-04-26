# PlaneGame

VideoLink: https://youtu.be/7wtWToxH_54?feature=shared

Hallo dies ist ein Spiel mit dem namen "PlaneGame", das mit der Programmiersprache Python entwickelt wurde. Das Spiel wurde objektorientiert programmiert und verwendet die pygame-Bibliothek.

Im dritten Semester habe ich mich für das Fach "Signal und System" angemeldet. In dieser Veranstaltung werden wir ein wenig Python-Kenntnisse verwenden. Wir werden die Bibliotheken scipy und numpy verwenden, um Fourier-Transformationen, Laplace-Transformationen usw zu berechnen, und die Ergebnisse mit matplotlib darstellen, um das Verständnis der Veranstaltung zu vertiefen.

Ähnlich wie bei dem Spiel "KongFuKing", nachdem ich ein wenig Python-Kenntnisse erlangt habe, möchte ich auch ein Spiel erstellen, um mein Interesse zu wecken und meine Fähigkeiten in diesem Bereich weiterzuentwickeln.


<div align=center>
    <img src="https://github.com/myry07/PlaneGame/blob/main/docs/game01.PNG" width="500" height="315“>
</div>


Das ist das Spiel allgemain. Feindliche Flugzeuge werden zufällig innerhalb eines bestimmten Bereichs generiert und können nur seitwärts bewegt werden. Außerdem feuern sie zufällig Projektile ab. Die Steuerung unseres Flugzeugs erfolgt mit den Tasten WASD, während die Taste J benutzt wird, um Projektile abzufeuern.

<div align=center>
    <img src="https://github.com/myry07/PlaneGame/blob/main/docs/over.PNG" width="500" height="315“>
</div>

Sobald ein feindliches Flugzeug getroffen wird, erhält der Spieler einen Punkt. Wenn das Spielerflugzeug von einem feindlichen Flugzeug getroffen wird, endet das Spiel.


<div align=center>
    <img src="https://github.com/myry07/PlaneGame/blob/main/docs/score.PNG" width="500" height="315“>
</div>

Die Punktzahlen jeder Spielrunde werden in einem separaten Ordner namens "record" gespeichert. Mit Hilfe der matplotlib-Bibliothek werden diese Punktzahlen in einer anderen Hauptmethode visualisiert.


<div align=center>
    <img src="https://github.com/myry07/PlaneGame/blob/main/docs/draw.PNG" width="500" height="315“>
</div>

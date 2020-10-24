# ThisNoAll-DL-HomeWork

# Estimating the distance between people on public spaces based on neural networks
I. mérföldkő: 7. hét (október 25. 23:59)
Adatok beszerzése, adatfeltárás, vizualizáció (ha szükséges) és előkészítés tanításhoz.
Eredmény: tanító, validációs és teszt adatbázisok

# Kutatási háttér:
Ebben a témában számos megoldás van már, viszont ezek a megoldások nem tudják egyértelműen lekezelni azokat az eseteket amikor egy tároság van a képen, vagy egy család, ahol a gyermek rohangál. Ezért ezeket a megoldásokat valós körülmények között nem lehetne használni, hiszen számos esetben jelezne amikor nem lenne szükséges. 

# Adatok beszerzése:
A videófelvételek a Times Square-en (New York) elhelyezett nyilvános webkameráról általunk rögzített tartalom. A 3 óra 15 perces felvétel nem statikus olyan értelemben, hogy több különböző nagyítás és eltolás történik a videófelvételen. A videón főként gyalogosok, zenészek és utcai maskarás emberek láthatóak, valamint a videófelvétel szélén látható még egy forgalmas utca, de mi a gyalogosokra fogunk ezekből koncentrálni. A Times Squaren gyakoriak a maszkarák mint például Micy Mouse, ezért érdemes lehet az ilyen esetek lekezelése tovább tanítani az általunk kiválasztott modellt. Az élő kamera folyamatosan elérhető az alábbi URL-en https://www.youtube.com/watch?v=oSFAIEOeIpE

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/capture.png?raw=true)

# Felhasználható modellek:
Maga az emberek felismerése megtud történni már előre elkészített modellek segítségével, kettő kiemelkedően jó pontossággal rendelkező modelt felhasználva is megnézzük a teljesítményét az eszköznek. A két modell

(1) https://github.com/tensorflow/models/tree/master/research/object_detection

(2) https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md

Saját modellt ebben a témában nincs lehetőségünk alkotni a feladatra rendelkezésre álló idő rövidsége miatt, valamint nem rendelkezünk kellő számítási kapacitásra az optimalizálásához ezeknek. 

# Transfer Learning:
A modellt ami képes felismerni az embert meg kell tanítani, hogy feltudja ismerni a maszkarás személyeket, valamint a gyermekeket a felnőttektől eltudja különíteni. Ezt Transfer Learning segítségével fogjuk megtenni. A jelenlegi hálónkat lefagyasztjuk és hozzá adunk egy plussz kimeneti réteget. Ezután a teszt és validációs adatainkkal feltanítjuk a hálót. Miután elértük a kívánt eredményt levesszük a Freeze-t a hálóról és egy pár epochig tanítjuk a teljes modellt. Az így módosított hálónk remélhetőleg már fel fogja tudni ismerni a gyermekeket és az utcán lévő maszkarás embereket.

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/kids.png?raw=true)
![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/maszkara.png?raw=true)

# Tanító adatok:
A Transfer Learninghez készítünk egy tanító adathalmazt gyermekekről, valamint opcionálisan a legnépszerűbb Disney karakterek jellemzéről. 

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/kid.jpg?raw=true)
![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/minnine.jpg?raw=true)

# Távolság mérése:
Miután felismertük az egyes személyeket a videófelvételen meg kell határozni az ők egymástól vett távolságát. A személyeket ha körbe rajzoljuk egy 2D-ben elhelyezkedő téglalappal akkor azt mondhatjuk hogy a talp középpontjától vett  távolság a másik ember középpontjához fogja megadni számunka a distance értéket. Ezek a következő képen jól szemléltetve láthatóak:

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/distance.jpg?raw=true)

Ennek a distance értéknek a kiszámítása nem fog másképp történni mint a 2D kép 3D-s rekonstrukciójával. Ehhez szükséges a kamerának a fókusz távolsága, viszont ez esetünkben adott és minden bolt esetén ismeretes. Ekkora az átskálázott X és Y értékek a következőek lesznek, ahol f a fókusztávolság.

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/X-Y_scaling.png?raw=true)

Ezek után az euklideszi térben alkalmazott számításoknak megfelelően megkapjuk a két ember közötti tényleges távolságot.

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/euklideszi.png?raw=true)

# Családok/társoságok megállapítása:
Abban az esetben ha családtagok, vagy társoságok mennek egymáshoz a megadott távolságtartási küszöbön belül a rendszernek nem kell azt jeleznie, hiszen rájuk a távolságtartás nem vonatkozik. Ezért akik a kamera képbe egymáshoz egy T threshold értéken belül (centiméter) jönnek be a képbe, vagyis amikor a kamera képen megjelenne és a threshold értékén belül találhatóak és a következő pár méter folyama során közelítőleg hasonló távolságra sétálnak egymást együttesen fogjuk őket kezelni. Valamint le kell azt az esetet is megfelelően kezelni, amikor a családban a gyermek elrohan a szülőktöl meg vissza. 

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/kids.png?raw=true)

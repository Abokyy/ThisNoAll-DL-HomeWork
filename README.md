# ThisNoAll-DL-HomeWork

Contirbutors (name, NEPTUN, workload):

Makara László Árpád G5YPX8 33%

Varsányi Botond AJ0PTT 33%

Sáfrán Gergely FT6QWV 33%

# Running procedure:

First run the Setup part of the notebook. After these steps are finished it requires to restart the environment. After restarting the environment you can simply use shift + enter to run all the following blocks. They will autimatically download the dataset from github and from Google Drive.


# English version:

# Estimating the distance between people on public spaces based on neural networks
I. milestone: week 7. (october 25. 23:59)
Collect data, prepare data for training, visualization (if needed).
Result: training, validation and test database

# Research background:
There are plenty of solutions around this, but they can not handle group of friends or a family, where a kid is just running around. So these solutions can not be used, because the number of false positives would be high.

# Collecting data:
The video footage is from a public CCTV camera placed on the Times Square, New York. The 3 hour and 15 minute long video is not static, meaning that there are some zooming and rotating on the recording. In the video the our focus is on the pedestrians, street musicians and street mascots and not on the street. It is common in the Time Square that people put on customes or mascots, Micky Mouse for example, so we should train our model to handle this. The live footage is available here: https://www.youtube.com/watch?v=oSFAIEOeIpE

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/capture.png?raw=true)

# Models that can be used:
Recognizing people can be done with already finished models. Two highly accurate model:

(1) https://github.com/tensorflow/models/tree/master/research/object_detection

(2) https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md

Creating our own model is not an option due the lack of time and computing capacity for opimization.

# Transfer Learning:

The models that can detect humans should recognize mascots and also should distinguish children from adults. This will be done with Transfer Learning. We freeze our current network and attach an additional output layer. Then we train our network with the test and validation data. After we achieve the desired result we unfreeze the network and train  the whole model for some epochs. The changed network will recognize children and mascots. 

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/kids.png?raw=true)
![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/maszkara.png?raw=true)

# Training data:
We create a dataset of children for the Transfer Learning, and optionally one about the most famous Disney characters.

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/kid.jpg?raw=true)
![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/minnine.jpg?raw=true)

For that we can use the following datasets:

http://buff.is.tue.mpg.de/
http://faust.is.tue.mpg.de/

Or we can choose any other from this, beacause this is for research purposes:

http://homepages.inf.ed.ac.uk/rbf/CVonline/Imagedbase.htm#people

# Measure the distance:
After we detect the people on the video we have to determine the distance between them. If we draw a rectangle around every people, we can say that the center of the bottom side is where they are, so the distances between these centers are the distances between the people. A picture for demonstration:

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/distance.jpg?raw=true)

To calculate the distance we have have to reconstruct the 2D picture to 3D. For this we have to know the camera's focus distance. The the rescaled X and Y values will be the next, where f is the focus distance:

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/X-Y_scaling.png?raw=true)

The distance after we do the calculations in the euclidean space:

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/euklideszi.png?raw=true)

# Recognizing families and groups:
If families or groups walk together the system should not go off, because they don't have to do social distancing. Therefore those who come in to the camera's vision below a T threshold, given in centimeter, and then keep this distance for some meters will be handled as a group. Also, we have to handle the cases where children are running around.

![alt text](https://github.com/Abokyy/ThisNoAll-DL-HomeWork/blob/main/assets/kids.png?raw=true)

# Magyar változat

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

from collections import namedtuple

Kordinat = namedtuple("Kordinat", ["x", "y"])
titik1 = Kordinat(x=2, y=4)

# menggunakan indeks
print("Kordinat absis titik1 teletak pada ", titik1[0])
# menggunakan nama atribut
print("Kordinat ordinat titik1 terletak pada", titik1.y)
# menggunakan getattr
print("Kordinat absis titik1 terletak pada", getattr(titik1, "x"))

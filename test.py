class Rectangle1:
  def hitungluas(panjang):
    nilai = panjang*panjang
    print("Luas Persegi", nilai)
 
class RectangleConstructor:
  def __init__(self, panjang):
    self.pjg = panjang
  
  def hitungluas(self):
    nilai = self.pjg * self.pjg
    print("Luas Persegi", nilai)

class Lingkaran:
  phi = 22/7

  def __init__(self, rad):
    self.luas = self.phi * rad * rad
    self.keliling = 2 * self.phi * rad

  def cetak(self):
    print("Luas Linkaran: ", self.luas)
    print("Luas Keliling: ", self.keliling)
    
class Driver:
  def main():
		kelas = Lingkaran(21)
		kelas.cetak()

Driver.main()

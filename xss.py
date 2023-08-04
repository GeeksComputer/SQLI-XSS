# import mechanize

# url = input("Enter the full url >> ")
# attack_no = 1
   
# with open ('vectors_XSS.txt') as x:
#    for line in x:
#       browser = mechanize.Browser()
#       browser.open(url)
#       browser.select_form(nr = 0)
#       browser["id"] = line
#       res = browser.submit()
#       content = res.read()

# if content.find(line) > 0:
#    print("Possible XSS")

# output = open('response/' + str(attack_no) + '.txt', 'w')
# output.write(content)
# output.close()
# print (attack_no)
# attack_no += 1

# Mengimpor library
import mechanize
import subprocess

# Menginsialisasikan sebuah fungsi untuk menampung proses
def xss():
   # Menginisialisasikan variabel bertipe data string untuk melakukukan masukkan atau inputan url target
   url = str(input("Enter the full url of target >> "))
   
   # Menginisalisasikan variabel dengan hasil berupa integer atau angka
   attackNumber = 1
   
   # Membuka file atau berkas dengan eksistensi .txt
   with open ('xss.txt') as x:
      for line in x:
         br = mechanize.Browser() # Menginiasilisasikan variabel dengan hasil berupa pemanggilan method dari librari mechanize agar bisa berinteraksi dengan browser
         br.open(url) # Method dari library mechanize untuk mulai membuka website berdasarkan alamat yang telah dimasukkan
         br.select_form(nr = 0) # Method untuk mulai melakukan interaksi dengan form
         br["id"] = line # Variabel dengan parameter "id" yang merupakan sebuah nama dari form yang telah dipilih dengan hasil berupa file yang berisi payload
         response = br.submit() # Variabel dengan hasil berupa method untuk melakukan interaksi submit pada form yang telah diisi payload
         content = response.read() # Variabel dengan hasil berupa method untuk proses pembacaan
   
   subprocess.run('clear', shell=True) # Memanggil perintah untuk membersihkan layar
   
   # Pengkondisian if untuk menemukan vulnerability xss pada baris lembar website
   if content.find(line) > 0:
      print("Possible XSS") # Mencetak peringatan
      
   output = open('response/' + str(attackNumber) + '.txt', 'w') # Variabel dengan hasil method untuk melakukan pembukaan terhadap variabel attackNumber dengan membuat file baru dengan eksistensi .txt 
   output.write(content) # Method untuk melakukan proses penulisan terhadap file eksistensi .txt yang telah dibuat
   output.close() # Method untuk menghentikan proses pembuatan dan penulisan file .txt
   print(attackNumber) # Menampilkan variabel attackNumber
   attackNumber += 1 # Menjumlahkan hasil dari variabel attackNumber setiap kali melakukan perulangan

# Pengkondisian if untuk menjalankan program   
if __name__ == "__main__":
   xss() # Memanggil fungsi untuk menjalankan proses
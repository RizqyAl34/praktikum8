class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nim, gender, nilai):
        self.data_mahasiswa.append({'nama': nama, 'nim': nim, 'L/P?': gender, 'nilai': nilai})
        print("=" * 62)
        print(f"|    Data mahasiswa '{nama}' berhasil ditambahkan    |")
        print("=" * 62)

    def tampilkan(self):
        if not self.data_mahasiswa:
            print()
            print("=" * 37)
            print("|    Tidak ada data mahasiswa     |")
            print("=" * 37)
        else:
            print("\n              Daftar Nilai Mahasiswa              ")
            print("=" * 49)
            print("| NO |       NAMA       |    NIM    |L/P| NILAI |")
            print("-" * 49)
            for i, mhs in enumerate(self.data_mahasiswa, start=1):
                print(f"|{i:3}.| {mhs['nama']:16} | {mhs['nim']:9} | {mhs['L/P?']:1} | {mhs['nilai']:6}|")
            print("=" * 49)

    def hapus(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs['nama'] == nama:
                self.data_mahasiswa.remove(mhs)
                print("=" * 59)
                print(f"|    Data mahasiswa '{nama}' berhasil dihapus     |")
                print("=" * 59)
                return
        print("=" * 67)
        print(f"|   Data mahasiswa dengan nama '{nama}' tidak ditemukan   |")
        print("=" * 67)

    def ubah(self, nama, nim, gender, nilai_baru):
        for mhs in self.data_mahasiswa:
            if mhs['nama'] == nama:
                mhs['nim'] = nim
                mhs['L/P?'] = gender
                mhs['nilai'] = nilai_baru
                print("=" * 55)
                print(f"|   Data mahasiswa '{nama}' berhasil diubah   |")
                print("=" * 55)
                return
        print("=" * 67)
        print(f"|   Data mahasiswa dengan nama '{nama}' tidak ditemukan   |")
        print("=" * 67)


if __name__ == "__main__":
    daftar = DaftarNilaiMahasiswa()

    while True:
        
        print("\n        MENU        ")
        print("=" * 20)
        print("| 1. Tambah data   |")
        print("| 2. Tampilkan data|")
        print("| 3. Hapus data    |")
        print("| 4. Ubah data     |")
        print("| 5. Keluar        |")
        print("=" * 20)
        
        pilihan = input("Pilih Nomor Menu (1 - 5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nim = int(input("Masukkan nim: "))
            gender = input("Masukkan gender: ")
            nilai = float(input("Masukkan nilai: "))
            daftar.tambah(nama, nim, gender, nilai)
        elif pilihan == "2":
            daftar.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
            daftar.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang diubah: ")
            nim = int(input("Masukan nim mahasiswa yang diubah: "))
            gender = input("Masukan gender mahasiswa yang diubah: ")
            nilai_baru = float(input("Masukkan nilai baru: "))
            daftar.ubah(nama, nim, gender, nilai_baru)
        elif pilihan == "5":
            print("=" * 42)
            print("|    Program selesai. Terima kasih     |")
            print("=" * 42)
            break
        else:
            print("=" * 50)
            print("|    Pilihan tidak valid, silakan coba lagi    |")
            print("=" * 50)
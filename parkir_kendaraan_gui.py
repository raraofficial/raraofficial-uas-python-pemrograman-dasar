import tkinter as tk

root = tk.Tk()
root.title("Parkir Rara mart")

label_kendaraan = tk.Label(root, text="Tipe Kendaraan")
label_kendaraan.pack()
entry_kendaraan = tk.Entry(root)
entry_kendaraan.pack()

label_nomor = tk.Label(root, text="Plat Nomor")
label_nomor.pack()
entry_nomor = tk.Entry(root)
entry_nomor.pack()

label_parkir = tk.Label(root, text="Lama Parkir")
label_parkir.pack()
entry_parkir = tk.Entry(root)
entry_parkir.pack()

label_parkir = tk.Label(root, text="Biaya Parkir")
label_parkir.pack()
entry_parkir = tk.Entry(root)
entry_parkir.pack()

def hitung_biaya():
    tipe_kendaraan = entry_kendaraan.get()
    lama_parkir = int(entry_parkir.get())

# Tarif kendaraan
    tarif = {
        "Sepeda": 1000,
        "Motor": 2000,
        "Mobil": 5000,
        "Bis": 10000
    }

    total_biaya = tarif.get(tipe_kendaraan, 0) * lama_parkir
    label_parkir.config(text=f"Biaya Parkir di Rara Mart: {total_biaya} Rupiah")

button_hitung = tk.Button(root, text="Hitung Biaya", command=hitung_biaya)
button_hitung.pack()

root.mainloop()

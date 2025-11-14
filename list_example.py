# Membuat List
denim = ["Oldblue", "Wingman", "Sage"]

# Menampilkan Isi List
print("=== LIST DENIM AWAL ===")
print(denim, "\n")

# Menambahkan Item
denim.append("Pinion")
print("=== SETELAH DITAMBAH ===")
print(denim, "\n")

# Mengubah Isi List
denim[3] = "Adelaide"
print("=== SETELAH DIUBAH ===")
print(denim, "\n")

# Menghapus Item
denim.remove("Sage")
print("=== SETELAH DIHAPUS ===")
print(denim, "\n")

print("=== DENIM FAVORIT ===")
print("Denim Favorit :", denim[2])

# Dictionary Bob Marley
bob = {
    "nama": "Bob Marley",
    "genre": "Reggae",
    "musik":["No Woman, No Cry", "Three Little Birds", "One Love"]

}

# Menampilkan seluruh data
print("\n=== DATA BOB MARLEY 🍀 ===")
for key, value in bob .items():
    print(f"- {key:<8}: {value}")

# Menampilkan lagu favorit
print("\nLagu Favorit :", bob["musik"][2])


# Menambah data baru
bob["negara"] = "Jamaica"
print("\n=== SETELAH MENAMBAH DATA ===")
for key, value in bob.items():
    print(f"- {key:<8}: {value}")

# Mengubah nilai
bob["genre"] = "Roots Reggae"
print("\n=== SETELAH MENGUBAH GENRE ===")
for key, value in bob.items():
    print(f"- {key:<8}: {value}")
print("\n")
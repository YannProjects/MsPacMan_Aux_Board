# Demander à l'utilisateur une valeur hexadécimale de 8 bits
data_to_cpu = int(input("Entrez la valeur hexadécimale (8 bits, ex : FF, 1A, 00) : "), 16)

raw_data = (
    ((data_to_cpu & 0x01) << 1)
    | ((data_to_cpu >> 1 & 0x01) << 2)
    | ((data_to_cpu >> 2 & 0x01) << 3)
    | ((data_to_cpu >> 3 & 0x01) << 6)
    | ((data_to_cpu >> 4 & 0x01) << 7)
    | ((data_to_cpu >> 5 & 0x01) << 5)
    | ((data_to_cpu >> 6 & 0x01) << 4)
    | ((data_to_cpu >> 7 & 0x01))
)

print(f"raw_data = {raw_data:#04x}")
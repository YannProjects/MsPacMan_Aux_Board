import itertools

addr_1 = 0
hex_values_1 = []
hex_values_2 = [0] * 4096
with open('C:\\Users\\yannv\\Documents\\Projets_HW\\MsPacMan_Mezzanine\\roms\\mspacman_u567.mem', 'r') as fichier:
    for ligne in fichier:
        hex_str = ligne.strip()
        if hex_str:  # Ignore les lignes vides
            value = int(hex_str, 16)
            hex_values_1.append(value)

for ligne in range(2048):
    # Sauvegarde des bits nécessaires
    bit8  = (addr_1 >> 10) & 1
    bit5  = (addr_1 >> 8) & 1
    bit9  = (addr_1 >> 7) & 1
    bit10 = (addr_1 >> 6) & 1
    bit3  = (addr_1 >> 4) & 1

    addr_2 = addr_1
    # Efface les bits à modifier
    addr_2 &= ~(1 << 10)
    addr_2 &= ~(1 << 8)
    addr_2 &= ~(1 << 7)
    addr_2 &= ~(1 << 6)
    addr_2 &= ~(1 << 4)

    # Place les bits échangés        
    addr_2 |= (bit3 << 10)
    addr_2 |= (bit9 << 8)
    addr_2 |= (bit10 << 7)
    addr_2 |= (bit8 << 6)
    addr_2 |= (bit5 << 4)

    data = hex_values_1[addr_1]
    # On duplique les données sur les deux zones
    hex_values_2[addr_2] = data
    hex_values_2[addr_2+ 2048] = data

    print(f"addr_1: 0x{addr_1:04X}  addr_2: 0x{addr_2:04X}  data: 0x{data:02X}")
    addr_1 += 1    

# Sauvegarde de hex_values_2 puis du reste de hex_values_1 dans un nouveau fichier
with open('C:\\Users\\yannv\\Documents\\Projets_HW\\MsPacMan_Mezzanine\\roms\\mspacman_u567_u5_swapped.mem', 'w') as out_file:
    # D'abord hex_values_2 (2048 valeurs)
    for value in hex_values_2:
        out_file.write(f"{value:02X}\n")
    # Puis le reste de hex_values_1 (s'il y a plus de 2048 valeurs)
    for value in hex_values_1[2048:]:
        out_file.write(f"{value:02X}\n")
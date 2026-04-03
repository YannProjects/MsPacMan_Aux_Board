import itertools

addr_1 = 0
raw_hex_data = []
with open('C:\\Users\\yannv\\Documents\\Projets_HW\\MsPacMan_Mezzanine\\roms\\mspacman_u567_u5_swapped.mem', 'r') as fichier:
    for ligne in fichier:
        hex_str = ligne.strip()
        if hex_str:  # Ignore les lignes vides
            value = int(hex_str, 16)
            raw_hex_data.append(value)

for addr_1 in range(8192,8192+500):
    raw_data = raw_hex_data[addr_1]

    #data_to_cpu = (((raw_data >> 4) & 0x01) << 7) | (((raw_data >> 3) & 0x01) << 6) | (((raw_data >> 5) & 0x01) << 5) | (((raw_data >> 6) & 0x01) << 4)
    data_to_cpu = (((raw_data) & 0x01) << 7) | (((raw_data >> 4) & 0x01) << 6) | (((raw_data >> 5) & 0x01) << 5) | (((raw_data >> 7) & 0x01) << 4)
    data_to_cpu = data_to_cpu | (((raw_data >> 6) & 0x01) << 3) | (((raw_data >> 3) & 0x01) << 2) | (((raw_data >> 2) & 0x01) << 1) | (((raw_data >> 1) & 0x01))

    print(f"addr_1: 0x{addr_1:04X}  raw data: 0x{raw_data:02X} data to CPU: 0x{data_to_cpu:02X}")

def gen_Sim_data_for_overlay(resetn, addr, cpu_addr, expected_overlay):
    """Génère les lignes de test pour le mode overlay."""
    addr_short = addr >> 3
    # Ligne pour l'adresse avec overlay désactivé
    lines.append(f'$MSG "0x{addr:04X}";')
    lines.append(f"C {resetn} '{addr_short:04X}' 1 \"{cpu_addr:04X}\" {expected_overlay}")
    return lines

def gen_Sim_data_for_addr_checks(addr, rfrsh, expected_rom_patched, expected_final_addr, expected_jrfrshn, expected_Ap, expected_u5_bank_sel, expected_u6_bank_sel, expected_u7_bank_sel, expected_mspacman_flash_csn):
    """Génère les lignes de test pour une modification d'adresse (xlate ou patch)."""
    addr_short = addr >> 3
    lines.append(f"C 1 '{addr_short:04X}' \"{expected_rom_patched:04X}\" \"{expected_final_addr:04X}\" {rfrsh} {expected_jrfrshn} {expected_Ap} {expected_u5_bank_sel} {expected_u6_bank_sel} {expected_u7_bank_sel} {expected_mspacman_flash_csn} *")
    return lines

header = """
Revision 00 ;
Designer Engineer ;
Company  Owner ;
Assembly None ;
Location  ;
Device   F1504ISPPLCC44; /* This sets the target to be a JTAG Programmed Atmel ATF1504AS in TQFP-44 */\n
"""

# Création du fichier
with open("MsPacMan_aux_board_with_PINNODE.si", "w", encoding="utf-8") as f:
    lines=[]
    f.write(header)
    # Partie liée à la detection de l'overlay
    f.write("ORDER: i_clk, %5, i_resetn, %5, i_addr, %5, i_rfrshn, %5, cpu_addr, %2, overlay;\n\n")
    f.write("VECTORS:\n\n")
    gen_Sim_data_for_overlay("0", 0x0001, 0x0000, "L")
    gen_Sim_data_for_overlay("0", 0x0002, 0x0000, "L")
    gen_Sim_data_for_overlay("0", 0x0003, 0x0000, "L")
    gen_Sim_data_for_overlay("1", 0x30C9, 0x30C8, "L")
    gen_Sim_data_for_overlay("1", 0x3FF8, 0x3FF8, "H")
    gen_Sim_data_for_overlay("1", 0x008D, 0x0088, "H")
    gen_Sim_data_for_overlay("1", 0x008E, 0x0088, "H")
    gen_Sim_data_for_overlay("1", 0x008F, 0x0088, "H")
    gen_Sim_data_for_overlay("1", 0x0038, 0x0038, "L")
    gen_Sim_data_for_overlay("1", 0x30CA, 0x30C8, "L")
    gen_Sim_data_for_overlay("1", 0x30CB, 0x30C8, "L")
    gen_Sim_data_for_overlay("1", 0x3FF8, 0x3FF8, "H")
    gen_Sim_data_for_overlay("1", 0x32F3, 0x32F0, "H")
    gen_Sim_data_for_overlay("1", 0x32F4, 0x32F0, "H")
    gen_Sim_data_for_overlay("1", 0x32F5, 0x32F0, "H")
    gen_Sim_data_for_overlay("1", 0x1600, 0x1600, "L")
    gen_Sim_data_for_overlay("1", 0x32F3, 0x32F0, "L")
    gen_Sim_data_for_overlay("1", 0x32F4, 0x32F0, "L")
    gen_Sim_data_for_overlay("1", 0x32F5, 0x32F0, "L")
    gen_Sim_data_for_overlay("1", 0x3FF8, 0x3FF8, "H")
    f.write('\n'.join(lines))

    # Partie liée au decodage des adresses
    lines=[]
    f.write("\n\nORDER: i_clk, %5, i_resetn, %5, i_addr, %2, rom_patched, %2, final_addr, %2, i_rfrshn, %2, o_jrfrshn, %2, o_A3p, o_A4p, o_A5p, o_A8p, o_A9p, o_A10p, %2, u5_bank_sel, %2, u6_bank_sel, %2, u7_bank_sel, %2, o_mspacman_flash_csn, %2, overlay;\n\n")
    f.write("VECTORS:\n\n")
    # On a besoin de relancer avec l'adresse 3FF8 pour reactiver l'overlay à cause d'une nouvelle configuration de test ???
    f.write("C 1 '07FF' **************** **************** 1 * ****** * * * * *\n")
    # addr, rfrsh, expected_rom_patched, expected_final_addr, expected_jrfrshn, expected_Ap, expected_u5_bank_sel, expected_u6_bank_sel, expected_u7_bank_sel, expected_mspacman_flash_csn
    gen_Sim_data_for_addr_checks(0x2CC1, "1", 0x80D0, 0x80D0, "L", "LHLLLL", "H", "L", "L", "L")
    gen_Sim_data_for_addr_checks(0x3F4D, "0", 0x0000, 0x3F48, "L", "HLLHHH", "L", "L", "H", "L")
    gen_Sim_data_for_addr_checks(0x9797, "1", 0x0000, 0x9790, "L", "LHLHHH", "L", "H", "L", "L")
    gen_Sim_data_for_addr_checks(0x4E72, "1", 0x0000, 0x4E70, "H", "LHHLHH", "L", "L", "L", "H")
    gen_Sim_data_for_addr_checks(0x2CDF, "1", 0x80E0, 0x80E0, "L", "LLHLLL", "H", "L", "L", "L")
    
    f.write('\n'.join(lines))
    f.write('\n')

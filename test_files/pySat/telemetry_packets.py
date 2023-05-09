import struct
import random
import communication_protocols as protocol


def beacon():
    # Define telemetry packet content
    pkt_length = struct.calcsize('>II4fIL')
    pkt_id = 0
    bat_temp = random.random() + random.randrange(100)
    bat_volt = random.random() + random.randrange(100)
    bat_curr = random.random() + random.randrange(100)
    bat_charge = random.random()
    flt_comp_state = random.randrange(3)

    # Packet CRC
    CRC = protocol.create_crc(struct.pack('>II4fI', pkt_length, pkt_id, bat_temp,
                            bat_volt, bat_curr, bat_charge, flt_comp_state))

    # Packet Structure
    packet = struct.pack('>II4fIL', pkt_length, pkt_id, bat_temp, bat_volt, 
                        bat_curr, bat_charge, flt_comp_state, CRC)

    print('\nBEACON PACKET:\n')
    print(packet)
    return packet


def header():

    # Packet Parameters
    pkt_length = struct.calcsize('>9IL')
    pkt_id = 1
    payload_count = 0
    nack_array = (0, 0, 3, 0, 0, 6)

    # Packet CRC
    CRC = protocol.create_crc(struct.pack('>9I', pkt_length, pkt_id, payload_count, *nack_array))

    # Packet Structure
    packet = struct.pack('>9IL', pkt_length, pkt_id, payload_count, *nack_array, CRC)
    
    print('\nHEADER PACKET:\n')
    print(packet)
    payload_count += 1
    return packet


def eps():

    # Packet Parameters
    pkt_length = struct.calcsize('>IIffffL')
    pkt_id = 2
    bat_temp = random.random() + random.randrange(100)
    bat_volt = random.random() + random.randrange(100)
    bat_curr = random.random() + random.randrange(100)
    bat_charge = random.random()

    # Packet CRC
    CRC = protocol.create_crc(struct.pack('>IIffff', pkt_length, pkt_id, bat_temp, bat_volt, bat_curr, bat_charge))

    # Packet Structure
    packet = struct.pack('>IIffffL', pkt_length, pkt_id, bat_temp, bat_volt, bat_curr, bat_charge, CRC)
    
    print('\nEPS PACKET:\n')
    print(packet)
    return packet


def com():

     # Packet Parameters
    pkt_length = struct.calcsize('>6IL')
    pkt_id = 3
    radio_config = 1
    health_status = 1
    antenna_status = 1
    op_mode = 0 
    
    # Packet CRC
    CRC = protocol.create_crc(struct.pack('>6I', pkt_length, pkt_id, radio_config, 
                            health_status, antenna_status, op_mode))

    # Packet Structure
    packet = struct.pack('>6IL', pkt_length, pkt_id, radio_config, 
                         health_status, antenna_status, op_mode, CRC)
    
    print('\nCOM PACKET:\n')
    print(packet)
    return packet


def gnc():

    # Packet Parameters
    pkt_length = struct.calcsize('>3I23dI4d5I3dL')
    pkt_id = 4
    gnc_mode = random.randrange(4)
    sc_quat = list(random.random() + random.randrange(100) for i in range(4))
    sc_body_rates_radps = list(random.random() + random.randrange(100) for i in range(3))
    cmd_quat = list(random.random() + random.randrange(100) for i in range(4))
    cmd_body_rates_radps = list(random.random() + random.randrange(100) for i in range(3))
    mekf_3sigma_rad = list(random.random() + random.randrange(100) for i in range(6))
    mekf_biad_radps = list(random.random() + random.randrange(100) for i in range(3))
    mekf_telem = random.randrange(100)
    r_eci_m = list(random.random() + random.randrange(100) for i in range(3))
    ace_err = random.random() + random.randrange(100)
    eclipse = 0
    sgp4_flag = random.randrange(4)
    sc_above_gs = 1
    sc_above_targ = 0
    target_gen_flag = random.randrange(3)
    elev_gs_rad = random.random() + random.randrange(100)
    elev_targ_rad = random.random() + random.randrange(100)
    ss_valid = random.random() + random.randrange(100)
    
    # Packet CRC
    CRC = protocol.create_crc(struct.pack('>3I23dI4d5I3d', pkt_length, pkt_id, gnc_mode, *sc_quat,
                                        *sc_body_rates_radps, *cmd_quat, *cmd_body_rates_radps, 
                                        *mekf_3sigma_rad, *mekf_biad_radps, mekf_telem, *r_eci_m, 
                                        ace_err, eclipse, sgp4_flag, sc_above_gs, sc_above_targ, 
                                        target_gen_flag, elev_gs_rad, elev_targ_rad, ss_valid)) + 100

    # Packet Structure
    packet = struct.pack('>3I23dI4d5I3dL', pkt_length, pkt_id, gnc_mode, *sc_quat,
                         *sc_body_rates_radps, *cmd_quat, *cmd_body_rates_radps, 
                         *mekf_3sigma_rad, *mekf_biad_radps, mekf_telem, *r_eci_m, 
                         ace_err, eclipse, sgp4_flag, sc_above_gs, sc_above_targ, 
                         target_gen_flag, elev_gs_rad, elev_targ_rad, ss_valid, CRC)

    print('\nGNC PACKET:\n')
    print(packet)
    return packet


def soar():

    # Packet Parameters
    pkt_length = struct.calcsize('>2I65dIL')
    pkt_id = 5
    opt_state = list(random.random() + random.randrange(100) for i in range(30))
    opt_ctrl_Nm = list(random.random() + random.randrange(100) for i in range(17))
    final_time_s = random.random() + random.randrange(100)
    exit_code_values = list(random.random() + random.randrange(100) for i in range(17))
    soar_count = 0

    # Packet CRC
    CRC = protocol.create_crc(struct.pack('>2I65dI', pkt_length, pkt_id, *opt_state, *opt_ctrl_Nm, 
                                        final_time_s, *exit_code_values, soar_count))

    # Packet Structure
    packet = struct.pack('>2I65dIL', pkt_length, pkt_id, *opt_state, *opt_ctrl_Nm, 
                         final_time_s, *exit_code_values, soar_count, CRC)

    print('\nSOAR PACKET:\n')
    print(packet)
    soar_count += 1
    return packet


def img():

     # Packet Parameters
    pkt_length = struct.calcsize('>2I79092sL')
    pkt_id = 6
    image_data = None
    with open('data/imaging_payload.txt', 'rb') as f:
        image_data = f.read()

    # Packet CRC
    CRC = protocol.create_crc(struct.pack('>2I79092s', pkt_length, pkt_id, image_data))

    # Packet Structure
    packet = struct.pack('>2I79092sL', pkt_length, pkt_id, image_data, CRC)

    print('\nIMG PACKET:\n')
    print(packet)
    return packet


def main():
    beacon()
    # header()
    # eps()
    # com()
    # gnc()
    # soar()
    # img()



if __name__=='__main__':
    main()
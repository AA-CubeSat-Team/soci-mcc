import struct
import random
import communication_protocols as protocol


def header(packet, payload_size):

    # Grab and decode packet fields
    id = int.from_bytes(packet[0:4], byteorder='big')
    length = int.from_bytes(packet[4:8], byteorder='big')
    message = packet[8:34].decode()
    hmac = packet[34:98].decode()
    nack_array = list(bytearray(packet[98:122:4]))
    crc = int.from_bytes(packet[122:], byteorder='big')

    # Show packet contents
    print('\nHEADER COMMAND PACKET\n')
    print('Packet Length:', length)
    print('Packet ID:', id)
    print('Header Message:', message)
    print('Packet HMAC:', hmac)
    print('NACK Array:', nack_array)
    print('Packet CRC:', crc)

    # Check HMAC
    print('\n* MESSAGE AUTHENTICATION CHECK *')
    protocol.check_hmac(message, hmac)

    # Check CRC
    print('\n* CRC VERIFICATION CHECK *')
    protocol.check_crc(payload_size + packet[0:122], crc, id)
    print('--------------------')

def com(packet):

    # Grab and decode packet fields
    id = int.from_bytes(packet[0:4], byteorder='big')
    length = int.from_bytes(packet[4:8], byteorder='big')
    reconfig_radio = int.from_bytes(packet[8:12], byteorder='big')
    check_health = int.from_bytes(packet[12:16], byteorder='big')
    shut_down_trans = int.from_bytes(packet[16:20], byteorder='big')
    req_payload = int.from_bytes(packet[20:24], byteorder='big')
    req_image = int.from_bytes(packet[24:28], byteorder='big')
    check_ant_status = int.from_bytes(packet[28:32], byteorder='big')
    enter_data_mode = int.from_bytes(packet[32:36], byteorder='big')
    enter_cmd_mode = int.from_bytes(packet[36:40], byteorder='big')
    dep_ant_1 = int.from_bytes(packet[40:44], byteorder='big')
    dep_ant_2 = int.from_bytes(packet[44:48], byteorder='big')
    crc = int.from_bytes(packet[48:52], byteorder='big')

    cmd_dict = {0 : 'NO', 1 : 'YES'}

    # Show packet contents
    print('\nCOM COMMAND PACKET\n')
    print('Packet Length:', length)
    print('Packet ID:', id)
    print('Reconfigure Radio:', cmd_dict.get(reconfig_radio))
    print('Check Radio Health:', cmd_dict.get(check_health))
    print('Shut Down Transmissions:', cmd_dict.get(shut_down_trans))
    print('Request Payload:', cmd_dict.get(req_payload))
    print('Request Image:', cmd_dict.get(req_image))
    print('Check Antenna Status:', cmd_dict.get(check_ant_status))
    print('Enter Data Mode:', cmd_dict.get(enter_data_mode))
    print('Enter Command Mode:', cmd_dict.get(enter_cmd_mode))
    print('Deploy Antenna (Alg 1):', cmd_dict.get(dep_ant_1))
    print('Deploy Antenna (Alg 2):', cmd_dict.get(dep_ant_2))
    print('Packet CRC:', crc)


    # Check CRC
    print('\n* CRC VERIFICATION CHECK *')
    protocol.check_crc(packet[0:48], crc, id)
    print('--------------------')


def gnc():
    pass


def soar():
    pass


def img():
    pass


def main():
    # header()
    # com()
    # gnc()
    # img()
    pass



if __name__=='__main__':
    main()
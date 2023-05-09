import serial
import telemetry_packets as tlm
import command_packets as cmd
import communication_protocols as protocol

def get_cmds():

    # Initialize variables
    serial_port = serial.Serial(port='COM11', baudrate=9600)
    payload_size_data = serial_port.read(4)
    payload_size = int.from_bytes(payload_size_data, 'big') // 8
    payload = serial_port.read(payload_size - 4)
    print(f'Total Payload Size: {payload_size} bytes')

    # Return the data
    print('\n--- Start Payload ---\n')
    print(payload)
    print('\n--- End Payload ---\n')
    return payload, payload_size_data


# UPDATE: Trying TERMINATED Protocol, delineate packets on termination character
def uplink():

    # Init variables
    term_char = b'\x0A'

    # Get the data from the serial port
    print('\n* GRABBING DATA *\n')
    payload, payload_size = get_cmds()

    # Parse the data into packets
    print('* PROCESSING PACKETS *\n')
    packets = payload.split(term_char)
    for i in range(len(packets)):
        print(f'Packet {i}:', packets[i], '\n')


    # Unpack the command packets
    print('----- PAYLOAD CONTENTS -----\n')
    for packet in packets:
        pkt_id = int.from_bytes(packet[0:4], 'big')
        if pkt_id == 0:
            print('Beacon')
        elif pkt_id == 1:
            cmd.header(packet, payload_size)
        elif pkt_id == 2:
            cmd.com(packet)
        elif pkt_id == 3:
            print('GNC')
        elif pkt_id == 4:
            print('SOAR')
        elif pkt_id == 5:
            print('IMG')

    # cmd.header(packets[0], payload_size)
    # cmd.com(packets[1])


def downlink():

    # Serial Port
    ser = serial.Serial('COM11')

    # Downlink Payload

    beacon = tlm.beacon()
    header = tlm.header()
    eps = tlm.eps()
    com = tlm.com()
    gnc = tlm.gnc()
    soar = tlm.soar()
    # img = tlm.img()

    # Send the packets

    # ser.write(beacon)
    ser.write(header)
    ser.write(eps)
    ser.write(com)
    ser.write(gnc)
    ser.write(soar)
    # ser.write(img)


def main():
    # get_data()
    uplink()
    # downlink()


if __name__=='__main__':
    main()
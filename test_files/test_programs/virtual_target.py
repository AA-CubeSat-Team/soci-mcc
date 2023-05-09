# This program is used to simulate a target that COSMOS
# can read and write data to and from.

# Import Library
import serial # used to read/write data across serial ports
import struct # used to structure tlm packets that can be send across a serial line
import random # random num generator

# This is the COM Port that is paired with the other com port that COSMOS
# is reading and writing from.
COM_PORT = 'COM11'
serial_port = serial.Serial(port=COM_PORT, baudrate=9600)


def receive_cmds():
    """
    This function receives, parses, and decodes command packet data sent
    from COSMOS.
    """

    # Read command packet from the serial port.
    # we expect a packet containing 12 bytes worth of data, so we will only
    # read 12 bytes at a time.
    cmd_pkt = serial_port.read(12)

    print("PACKET RECEIVED!\n")
    print(f'RAW DATA: {cmd_pkt}\n')

    # Converts the byte string into the appropriate data types.
    # Since each parameter in our command packet is a 4 byte UINT, we can
    # parse the string 4 bytes at a time and convert those 4 bytes into an int.
    pkt_length = int.from_bytes(cmd_pkt[0:4], byteorder='big')
    pkt_id = int.from_bytes(cmd_pkt[4:8], byteorder='big')
    cmd_data = int.from_bytes(cmd_pkt[8:12], byteorder='big')

    print('RECEIVED COMMAND PACKET\n')
    print('--------------------')
    print('Packet Length:', pkt_length)
    print('Packet ID:', pkt_id)
    print('Command Data:', cmd_data)
    print('--------------------')


def send_tlm():
    """
    This function creates a simple telemetry packet and sends the data to
    COSMOS via the virtual serial port.
    """

    # Define telemetry packet contents
    pkt_length = struct.calcsize('>III')
    pkt_id = 1
    pkt_data = random.randrange(100)

    # Structure telemetry packet as single byte string
    tlm_pkt = struct.pack('>III', pkt_length, pkt_id, pkt_data)

    # Console Message
    print("Sending Telemetry Packet: ", tlm_pkt)

    # Write telemetry packet to serial port
    serial_port.write(tlm_pkt)


def main():
    """
    Uncomment one of these functions according to which communication
    phase you are testing. (Delete 'pass' as well when running)
    """
    # receive_cmds()
    send_tlm()


if __name__=='__main__':
    main()
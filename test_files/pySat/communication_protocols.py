import hmac
import hashlib
import crcmod

def check_hmac(header_message, rec_hmac):
    secret_key = bytes('Hello, SOCI!', 'UTF-8')

    # Calculated HMAC using secret key and header message 
    calc_hmac = hmac.new(secret_key, header_message, hashlib.sha256).hexdigest()

    # Compare HMACs
    if rec_hmac == calc_hmac:
        print('\nMessage authenticated!')
        print('Command mode enabled.')
    else:
        print('\nCommand authentication failed! Received HMAC does not match calculated HMAC.')
        print(f'Received HMAC   = {rec_hmac}')
        print(f'Calculated HMAC = {calc_hmac}')
        print('Please try again.')


def create_crc(message):

    # Initialize CRC32 function
    crc32 = crcmod.Crc(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)

    # Calculate CRC
    crc32.update(message)

    # Return CRC
    return crc32.crcValue


def check_crc(rec_message, rec_crc, pkt_id):

    # Calculate CRC using the received message
    calc_crc = create_crc(rec_message)

    # Compare CRCs
    if calc_crc == rec_crc:
        print('\nNo errors detected!')
        print('Command packet is acknowledged.')
        return True
    else:
        print()
        print(f'NACK flag raised for Packet {pkt_id}!')
        print(f'Received CRC   = {rec_crc}')
        print(f'Calculated CRC = {calc_crc}')
        print(f'Packet {pkt_id} has been logged for a resend request.')
        return False

# NEEDS WORK
def nack_protocol(pkt, pkt_id):

    nack_packets = list()

    if check_crc(pkt):
        # pass packet to respective subsystem task
        print(f'Passing packet to subsystem with ID {pkt_id}')
    else: 
        # add packet ID to list of nack packets
        # once we've processed all packets during uplink,
        # this list of NACK packets will be sent down in the downlink
        # payload header packet
        nack_packets.append(pkt_id)
    

def main():
    pass


if __name__=='__main__':
    main()




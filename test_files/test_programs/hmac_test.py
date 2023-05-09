import hashlib
import hmac


def transmit():
    packet = []
    message = "This is our first message!"
    key = "Starting Uplink!"
    hmac1 = hmac.new(str.encode(key), message.encode('UTF-8'), hashlib.sha256)
    transmit_digest = hmac1.digest()
    packet.append(message)
    packet.append(transmit_digest)

    print()
    print('Message:', message)
    print('Secret Key:', key)
    print('Digest Value:', transmit_digest)
    print('---------------------------')
    return packet


def receive(packet):
    key = "Starting Uplink!"
    message = packet[0]
    print('Received Message:', message)
    print('Secret Key:', key)
    received_hash = packet[1]
    print('Received hash:', received_hash)
    hmac1 = hmac.new(str.encode(key), message.encode('UTF-8'), hashlib.sha256)
    calc_hash = hmac1.digest()
    print('Calculated hash:', calc_hash)
    print('--------------------------')
    
    if calc_hash == received_hash:
        print('Message Athenticated!')
        print('Start Tasks')
        print()
    else:
        print('Message Denied!')
        print('Request Retransmit')
        print()
        

def main():
    transmit_packet = transmit()
    receive(transmit_packet)

if __name__ =='__main__':
    main()
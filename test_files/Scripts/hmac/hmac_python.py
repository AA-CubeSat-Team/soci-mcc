import hashlib
import hmac

def HMAC():
    message = "This is our first message!"
    print('Message:', message)
    key = "AACT"
    print('Secret Key:', key)
    encoded_key = str.encode(key)
    print('Encoded Key:', encoded_key)
    hmac1 = hmac.new(encoded_key, message, message.encode('UTF-8'), hashlib.sha256)
    digest = hmac1.digest()
    print('Digest Value:', digest)

def main():
    HMAC()

if __name__ =='__main__':
    main()
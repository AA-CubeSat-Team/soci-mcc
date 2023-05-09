require 'openssl'

# should call this in the command configuration file
def generateHMAC():
    # message = header packet message
    header_message = get_cmd_value('SOCI', 'HEADER', 'HEADER_MESSAGE')
    # secret_key = key for hashing our message with
    secret_key = "AACT"
    # generates the message HMAC
    hmac = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('sha256'), secret_key, message)
    return hmac
end

def setHMAC():
    hmac = generateHMAC()
    cmd("SOCI HEADER with LENGTH 88, <Param #2 Name> <Param #2 Value>, ...")
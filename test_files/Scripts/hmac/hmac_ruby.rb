require 'openssl'

def generateHMAC(message)
    secret_key = "AACT"
    hmac = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('sha256'), secret_key, message)
    return hmac
end


def transmit()
    message = "Starting Uplink!"
    hmac = generateHMAC(message)
    puts ("transmitted hmac: #{hmac}")
    packet = [message, hmac]
    return packet
end


def receive()
    received_packet = transmit()
    received_message = received_packet[0]
    puts ("received message: #{received_message}")
    received_hmac = received_packet[1]
    puts ("received hmac: #{received_hmac}")

    secret_key = "AACT"
    calculated_hmac = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.new('sha256'), secret_key, received_message)
    puts ("calculated hmac: #{calculated_hmac}")

    if received_hmac == calculated_hmac
        puts "MESSAGE AUTHENTICATED"
        puts "STARTING UPLINK"
    else
       puts "MESSAGE DENIED"
   end
end

receive()



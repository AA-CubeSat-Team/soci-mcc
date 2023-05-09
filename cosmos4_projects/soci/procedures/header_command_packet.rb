require 'openssl'

# This subroutine creates and sends the command payload header packet
def send_header_packet

  # Generate header packet message
  message = ('a'..'z').to_a.shuffle.join
  
  # Generate header packet HMAC
  secret_key = 'Hello, SOCI!'
  hmac = OpenSSL::HMAC.hexdigest('SHA256', secret_key, message)
  
  # Calculate payload size
  
  
  # Send header packet
  cmd("SOCI", 
  "HEADER",
  "PL_LENGTH" => 1040+416+1472+352, 
  "PKT_ID" => 1, 
  "PKT_LENGTH" => 1040,
  "HMAC_MESSAGE" => message, 
  "HMAC" => hmac,
  "NACK_ARRAY" => [0,0,0,0,0,0], 
  "CRC" => 0) 
  
end
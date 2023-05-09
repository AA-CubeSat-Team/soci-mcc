# This procedure tracks the cmd_tlm server for NACK messages and stores
# all packets with the NACK flag in the retransmit request command

resend_array = Array.new(7,0)
queue_size = 1000
message_queue_id = subscribe_server_messages(queue_size) # messages from cmd_tlm server
for i in 0..queue_size
  message, color = get_server_message(message_queue_id, false)
  puts message
  if !message.empty? & message.include?("NACK")
    pkt_id_index = message.index("=") # index of the pkt id in the NACK Log Message
    pkt_id = message[pkt_id_index + 2]
    resend_array.append(pkt_id) # add pkt id to resend array    
    puts resend_array
  end
end

# send cmd with resend_array
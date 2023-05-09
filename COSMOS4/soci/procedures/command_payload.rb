# This script will send the command payload to SOCI

load_utility("header_command_packet.rb")
load_utility("com_command_packet.rb")
load_utility("gnc_command_packet.rb")
load_utility("img_command_packet.rb")

# Command Payload
send_header_packet()
send_com_cmd_packet()
send_gnc_cmd_packet()
send_img_cmd_packet()
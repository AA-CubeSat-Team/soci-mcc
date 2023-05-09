# This subroutine sends the com command packet
def send_img_cmd_packet

  cmd("SOCI", 
      "IMG",
      "PKT_ID" => 4,
      "PKT_LENGTH" => 352,  
      "CHECK_STAT" => 1, 
      "TAKE_PIC" => 1, 
      "GET_PIC_SIZE" => 1, 
      "GET_PIC" => 0, 
      "SET_PIC_CONT" => rand(1000), 
      "SET_PIC_BRIGHT" => rand(1000), 
      "SET_PIC_EXPO" => rand(1000), 
      "SET_SLP_TIME" => rand(100),  
      "CRC" => 0)
      
end
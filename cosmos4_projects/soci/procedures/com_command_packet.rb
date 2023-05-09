# This subroutine sends the com command packet
def send_com_cmd_packet

  cmd("SOCI", 
      "COM",
      "PKT_ID" => 2,
      "PKT_LENGTH" => 416,  
      "RECONFIG_RADIO" => 0, 
      "CHECK_HEALTH" => 1, 
      "SHUT_DOWN_TRANS" => 0, 
      "REQ_PAYLOAD" => 0, 
      "REQ_IMAGE" => 0, 
      "CHECK_ANT_STATUS" => 1, 
      "ENTER_DATA_MODE" => 0, 
      "ENTER_CMD_MODE" => 0, 
      "DEP_ANT_1" => 0, 
      "DEP_ANT_2" => 0, 
      "CRC" => 0)
      
end
# This subroutine sends the com command packet

# This subroutine sends the com command packet
def send_gnc_cmd_packet

  cmd("SOCI", 
      "GNC",
      "PKT_ID" => 3,
      "PKT_LENGTH" => 1472,  
      "ORBIT_TLE_1" => rand(1000) + rand,
      "ORBIT_TLE_2" => rand(1000) + rand,
      "ORBIT_TLE_3" => rand(1000) + rand,
      "ORBIT_TLE_4" => rand(1000) + rand,
      "ORBIT_TLE_5" => rand(1000) + rand,
      "ORBIT_TLE_6" => rand(1000) + rand,
      "ORBIT_TLE_7" => rand(1000) + rand,
      "ORBIT_TLE_8" => rand(1000) + rand,
      "ORBIT_TLE_9" => rand(1000) + rand, 
      "MET_UTC_S" => rand(1000) + rand, 
      "MET_SOAR_UTC_S" => rand(1000) + rand, 
      "QUAT_SOAR_CMD_1" => rand(1000) + rand, 
      "QUAT_SOAR_CMD_2" => rand(1000) + rand, 
      "QUAT_SOAR_CMD_3" => rand(1000) + rand,
      "QUAT_SOAR_CMD_4" => rand(1000) + rand,
      "SET_TARG_LAT" => rand(1000) + rand, 
      "SET_TARG_LON" => rand(1000) + rand, 
      "SET_TARG_ALT" => rand(1000) + rand,
      "INIT_GNC_MODE" => 0,
      "EN_CRIT_POWER_MODE" => 0,
      "EN_LOW_POWER_MODE" => 0, 
      "EN_AUTO_POINT" => 1, 
      "EN_IMAGING" => 0, 
      "EN_SOAR" => 1, 
      "TRI_OVERRIDE" => 0,
      "CRC" => 0)

end
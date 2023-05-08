# Script Runner test script
cmd("SOCI EXAMPLE")
wait_check("SOCI STATUS BOOL == 'FALSE'", 5)

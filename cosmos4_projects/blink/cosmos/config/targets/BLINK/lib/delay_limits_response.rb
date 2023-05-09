# This file implements a class to handle responses to limits state changes.

require 'cosmos/packets/limits_response'

# DelayLimitsResponse class
#
# This class handles a limits response
#
class DelayLimitsResponse < Cosmos::LimitsResponse

  def call(packet, item, old_limits_state)
    case item.limits.state
    when :RED_HIGH
      cmd('BLINK', 'DELAY', 'DELAY' => 149)
    when :RED_LOW
      cmd('BLINK', 'DELAY', 'DELAY' => 51)
    end
  end

end # class DelayLimitsResponse

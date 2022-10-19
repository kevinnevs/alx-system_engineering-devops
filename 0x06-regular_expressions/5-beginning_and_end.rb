#!/usr/bin/env ruby
# Regex must start with "h" ends with "n" & can have any single character inbetween

puts ARGV[0].scan(/h.n$/).join

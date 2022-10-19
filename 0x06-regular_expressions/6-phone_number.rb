#!/usr/bin/env ruby
# Regex must match 10 digit phone num "4155049898"

puts ARGV[0].scan(/^\d{10}$/).join

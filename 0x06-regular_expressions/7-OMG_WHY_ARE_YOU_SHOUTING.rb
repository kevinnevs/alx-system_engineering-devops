#!/usr/bin/env ruby
# Test passes regex capital letters

puts ARGV[0].scan(/[A-Z]/).join

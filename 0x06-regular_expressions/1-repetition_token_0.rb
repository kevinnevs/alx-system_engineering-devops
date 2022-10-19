#!/usr/bin/env ruby
# Test cases "hbn hbtn hbttn hbtttn hbttttn hbtttttn hbttttttn" regex

puts ARGV[0].scan(/hbt{2,5}n/).join

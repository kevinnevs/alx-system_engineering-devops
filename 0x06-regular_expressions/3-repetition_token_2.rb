#!/usr/bin/env ruby
# Test case pass "hbtn hbttn hbtttn hbttttn" regex

puts ARGV[0].scan(/hbt{1,4}n/).join

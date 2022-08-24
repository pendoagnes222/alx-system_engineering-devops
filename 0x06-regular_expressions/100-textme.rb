#!/usr/bin/env ruby
# Prints sender, receiver and flags

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')

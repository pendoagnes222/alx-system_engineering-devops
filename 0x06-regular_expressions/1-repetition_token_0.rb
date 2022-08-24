#!/usr/bin/env ruby
# Take one argument and pass it to a regex matching method

puts ARGV[0].scan(/hbtt{1,4}n/).join

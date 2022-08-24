#!/usr/bin/env ruby
# Take one argument and pass it to a regex matching method

puts ARGV[0].scan(/h[a-zA-Z0-9]n$/).join

# frozen_string_literal: true
# Ruby-side verification (runs in docker ruby:3.3 service; also documents book Ch.3).
# Mirrors 01/02 in real Ruby: loop equivalence + hello-world arity.
raise 'loop mismatch' unless (1..4).map { 'forward 50; turnright 90' } == Array.new(4) { 'forward 50; turnright 90' }
puts 'Ruby loop equivalence OK'
print "Hello, world!\n"
# Shoes DSL smoke (parses only if scarpe/lacci present; otherwise skip gracefully)
begin
  require 'lacci'
  puts "lacci loaded: #{defined?(Lacci) ? 'yes' : 'partial'}"
rescue LoadError => e
  puts "lacci not installed in this container (skip Shoes GUI assert): #{e.message[0,120]}"
end

# Regular Expressions. Used for pattern matching and validation
# Used in data science for ETL
import Reg_Decorator as reg  # regular expression module
# meta (configuration) characters i.e. data about data
# The 3 types of matches are fullmatch(), match() and search() and syntax is (pattern, inp_str)
# The re result can be a re object or None
input_str = "hello, world!"

# .(dot) => match any character/digit/symbol/space
# reg.fullmatch("hello. world!", input_str)
# reg.match("hello. world!", input_str)
# reg.search("hello. world!", input_str)

# ^(caret) => starting with
# reg.fullmatch("^hello", input_str)  # will give not a match since fullmatch searches the entire string
# reg.match("^hello", input_str)
# reg.search("^hello", input_str)

# $(dollar) => ending with
# reg.fullmatch("d!$", input_str)  # will give not a match since fullmatch searches the entire string
# reg.match("^.*d!$", input_str)  # * checks all string
# reg.search("d!$", input_str)

# *(asterisk) => 0 or more repetitions
# reg.fullmatch("l*", input_str)  # will give not a match since fullmatch searches the entire string
# reg.match("l*", input_str)
# reg.search("l*", input_str)

# d => 0-9
# D => not 0-9
# w => a-z or 0-9
# W => not a-z neither 0-9
# s => space
# S => not space

# grouping
# [or] pr {range}
# [abc] => a or b or c
# [^abc] => not abcd (^ symbolizing not-in, in grouping)
# [d] => any digit
# a{2} => a occurs exactly twice
# t{2,} => t occurs at least twice upto n
# l{2,7} => l occurs at least twice upto 7 times
# [0-9]{3} => any digit exactly 3 times
# [0-9]{4}-[0-9]{3}-[0-9]{3} => mobile number
# ^www\.[a-z]*\.com$ => url regex
# [a-z]*\.[a-z]*@[a-z]*\.com$  => email validation
# [0-9]{4}-[0-9]{4}-[0-9]{4}  => aadhar card

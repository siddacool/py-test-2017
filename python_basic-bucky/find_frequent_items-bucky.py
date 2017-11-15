from collections import Counter

text = r'The command line syntax of dd differs from many other Unix programs, ' \
       'in that it uses the syntax option=value for its command line options, ' \
       'rather than the more-standard -option value or --option=value formats. ' \
       'By default, dd reads from stdin and writes to stdout,' \
       'but these can be changed by using the if (input file) and of (output file) options'\
       'Usage varies across different operating systems. Also, certain features of dd will depend' \
       'on the computer system capabilities, such as dd\'s ability to implement an option for direct memory access.' \
       'Sending a SIGINFO signal (or a USR1 signal on Linux) to a running dd process makes it print I/O statistics to ' \
       'standard error once and then continue copying. dd can read standard input from the keyboard.' \
       'When end-of-file (EOF) is reached, dd will exit. Signals and EOF are determined by the software.' \
       'For example, Unix tools ported to Windows vary as to the EOF: Cygwin uses Ctrl+D' \
       '(the usual Unix EOF) and MKS Toolkit uses ctrl+z (the usual Windows EOF).'

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)

print(top_three)
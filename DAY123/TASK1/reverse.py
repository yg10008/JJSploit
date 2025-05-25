from module_file_logger import ygLogs as ygsaw
from module_console_logger import consoleLogger as ygsawC
import module_log_parser as logParser

def reverse_string(string):
    ygsaw.debug("we are inside the reverse function")
    strl = list(string)
    first = 0
    last = len(strl) - 1

    while first < last:
        strl[first], strl[last] = strl[last], strl[first]
        first += 1
        last -= 1
    ygsaw.debug("logic successfully executed")
    ygsaw.debug("string was reversed and returned")
    return ''.join(strl)

ygsawC.debug("console logger was imported")

ygsaw.debug("user trying to enter the string")
string = str(input("Enter a string: "))
ygsaw.debug("string was entered: " + string)
ygsaw.debug("reverse function was called")
print(reverse_string(string))
ygsaw.debug("string was printed")


logParser.parsing_the_logFile('ygLogs.log')

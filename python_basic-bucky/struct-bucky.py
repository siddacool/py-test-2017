from struct import *

# Store as bytes
packed_data = pack('iif', 6, 20, 6.45)
print(packed_data)

print(calcsize('i'))

# byte to normal
human_readable = unpack('iif', packed_data)

print(human_readable)
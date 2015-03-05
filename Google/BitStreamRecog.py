
'''
Here we input a bitstream '1001 0101 0001 0010 ....'

From the start, if the beginning bit is 1, the next two byte will represent a character,
if the beginning bit is 0, the next byte will represent a character.

Give you an input stream how could you determine the last character is a single byte or double byte.
'''


def CheckSingleOrDouble(bitStream):
    step = 8

    inputL = len(bitStream)

    if inputL < 8 or inputL % 8 != 0:
        return "Invalid"


    currentLast = bitStream[-step]


    if currentLast == '0':
        i = 1
        stored = []
        while i * step < inputL:
            i += 1
            if bitStream[-i*step] == '0':
                break
            else:
                stored.append(bitStream[-i*step])
        # For the last unresolved bit
        if bitStream[-i * step] == '1':
            stored.append('1')

        if len(stored) % 2 == 0:
            return "Single"
        else:
            return "Double"

    else:
        stored = []
        i = 1
        while currentLast != '0' and i*step < inputL:
            stored.append(currentLast)
            i += 1
            currentLast = bitStream[-i*step]


        if bitStream[-i * step] == '1':
            stored.append('1')

        s = len(stored)

        if s %2 == 0:
            return "Double"
        else:
            return "Invalid"





def test():

    print "Pass" if CheckSingleOrDouble('00000000') == 'Single' else "Failed"
    print "Pass" if CheckSingleOrDouble('000') == 'Invalid' else "Failed"
    print "Pass" if CheckSingleOrDouble('1010110110001100') == 'Double' else "Failed"
    print "Pass" if CheckSingleOrDouble('00000000101011011010110110001100') == 'Invalid' else "Failed"
    print "Pass" if CheckSingleOrDouble('0000000010101101100011001010110110001100') == 'Double' else "Failed"
    print "Pass" if CheckSingleOrDouble('0000000010101101101011011010110100000000') == 'Double' else "Failed"
    print "Pass" if CheckSingleOrDouble('000000001010110110101101101011011010110100000000') == 'Single' else "Failed"

if __name__ == '__main__':
    test()

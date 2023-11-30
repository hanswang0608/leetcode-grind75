class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # returns (sum, carry)
        def bitAddition(aBit, bBit, carry):
            bitStr = aBit + bBit + carry
            # if aBit == 0 and bBit == 0:
            #     return (0, 0)
            # elif aBit == 1 and bBit == 0:
            #     return (1, 0)
            # elif aBit == 0 and bBit == 1:
            #     return (1, 0)
            # else:
            #     return (1, 1)
            if bitStr == '000':
                return ('0', '0')
            elif bitStr == '001':
                return ('1', '0')
            elif bitStr == '010':
                return ('1', '0')
            elif bitStr == '011':
                return ('0', '1')
            elif bitStr == '100':
                return ('1', '0')
            elif bitStr == '101':
                return ('0', '1')
            elif bitStr == '110':
                return ('0', '1')
            else:
                return ('1', '1')
        i = len(a)-1
        j = len(b)-1
        carry = '0'
        output = ''
        while i >= 0 or j >= 0:
            aBit = '0'
            bBit = '0'
            if i >= 0:
                aBit = a[i]
                i -= 1
            if j >= 0:
                bBit = b[j]
                j -= 1
            sum, carry = bitAddition(aBit, bBit, carry)
            output = sum + output
        if carry == '1':
            output = '1' + output
        return output
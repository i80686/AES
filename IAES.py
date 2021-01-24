# http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf
class IAES:
    def __init__(self):
        self.Nk = 4
        self.Nb = 4
        self.Nr = 10

    def arrays(self, raws):
        Nb = []
        for i in range(4):
            Nb = Nb + [raws[4*0+i], raws[4*1+i], raws[4*2+i], raws[4*3+i]]
        return Nb

    def Inv_arrays(self, raws):
        Inv_raws = []
        for i in range(4):
            Inv_raws = Inv_raws + [raws[4*0+i], raws[4*1+i], raws[4*2+i], raws[4*3+i]]
        return Inv_raws

    def view(self, raws):
        raws = self.Inv_arrays(raws)
        raws = ''.join([x.to_bytes(1, byteorder='big').hex() for x in raws])
        print(raws)

    def view2(self, list):
        for i in range(len(list)):
            print(format(list[i], '2x'), end=' ')
            if i & 3 == 3:     # i%4 == 3
                print('\n', end='')
        print('\n', end='')

    def AddRoundKey(self, raws, Keys):
        AddRoundKey = []
        for raw, Key in zip(raws, Keys):
            AddRoundKey.append(raw ^ Key)
        return AddRoundKey

    def SubBytes(self, raws):
        S_box = [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
        ]
        raws_S_box = []
        for raw in raws:
            raws_S_box.append(S_box[raw])
        return raws_S_box

    def InvSubBytes(self, raws):
        IS_box = [
            0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
            0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
            0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
            0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
            0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
            0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
            0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
            0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
            0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
            0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
            0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
            0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
            0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
            0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
        ]
        raws_IS_box = []
        for raw in raws:
            raws_IS_box.append(IS_box[raw])
        return raws_IS_box

    def InvShiftRows(self, raws):
        s13 = raws.pop(7)
        raws.insert(4, s13)
        s2223 = raws[10:12]
        del raws[10:12]
        raws[8:0] = s2223
        s313233 = raws[13:16]
        del raws[13:16]
        raws[12:0] = s313233
        return raws

    def GMUL(self, a, b):      #Russian Peasant Multiplication algorithm
        p = 0
        while a and b:
            if b & 1:    # b%2
                p = p ^ a
            if a & 0x80:   # a=a*x^7(a>0),a >= 2**7(128)
                a = (a << 1) ^ 0x11b # 0x11b = x^8 + x^4 + x^3 + x + 1 (0b100011011)
            else:
                a = a << 1
            b = b >> 1
        return p

    def InvMixColumns(self, raws):
        for i in range(4):
            raws[0*4+i], \
            raws[1*4+i], \
            raws[2*4+i], \
            raws[3*4+i]  \
            = \
            self.GMUL(0x0e, raws[0*4+i]) ^ self.GMUL(0x0b, raws[1*4+i]) ^ self.GMUL(0x0d, raws[2*4+i]) ^ self.GMUL(0x09, raws[3*4+i]),\
            self.GMUL(0x09, raws[0*4+i]) ^ self.GMUL(0x0e, raws[1*4+i]) ^ self.GMUL(0x0b, raws[2*4+i]) ^ self.GMUL(0x0d, raws[3*4+i]),\
            self.GMUL(0x0d, raws[0*4+i]) ^ self.GMUL(0x09, raws[1*4+i]) ^ self.GMUL(0x0e, raws[2*4+i]) ^ self.GMUL(0x0b, raws[3*4+i]),\
            self.GMUL(0x0b, raws[0*4+i]) ^ self.GMUL(0x0d, raws[1*4+i]) ^ self.GMUL(0x09, raws[2*4+i]) ^ self.GMUL(0x0e, raws[3*4+i])
        return raws

    def RotWord(self, temp):
        b0 = temp.pop(0)
        temp.insert(3, b0)
        return temp

    def SubWord(self, temp):
        temp = self.SubBytes(temp)
        return temp

    def KeyExpansion(self, key):
        i = 0
        w = [[0]]*(self.Nb * (self.Nr + 1))
        Rcon = [[0x01, 0x00, 0x00, 0x00],
                [0x02, 0x00, 0x00, 0x00],
                [0x04, 0x00, 0x00, 0x00],
                [0x08, 0x00, 0x00, 0x00],
                [0x10, 0x00, 0x00, 0x00],
                [0x20, 0x00, 0x00, 0x00],
                [0x40, 0x00, 0x00, 0x00],
                [0x80, 0x00, 0x00, 0x00],
                [0x1B, 0x00, 0x00, 0x00],
                [0x36, 0x00, 0x00, 0x00]
                ]
        while i < self.Nk:
            w[i] = ([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]])
            i = i + 1

        i = self.Nk

        while i < self.Nb * (self.Nr + 1):
            temp = w[i - 1].copy()
            if i % self.Nk == 0:
                temp = self.SubWord(self.RotWord(temp))
                temp2 = []
                for temp1, Rcon1 in zip(temp, Rcon[(i // self.Nk)-1]):
                    temp2.append(temp1 ^ Rcon1)
                temp = temp2
            elif self.Nk > 6 and i % self.Nk == 4:
                temp = self.SubWord(temp)
            w_temp = []
            for w1, temp1 in zip(w[i-self.Nk], temp):
                w_temp.append(w1 ^ temp1)
            w[i] = w_temp
            i = i + 1
        return w

    def IAES(self, IInput, Cipher_Key):
        IInput = [IInput1 for IInput1 in IInput]
        Cipher_Key = [Cipher_Key1 for Cipher_Key1 in Cipher_Key]
        KeyExpansion = self.KeyExpansion(Cipher_Key)
        keys = []
        for Key_index in range(len(KeyExpansion)//4):
            keys_temp = (KeyExpansion[4*Key_index] + KeyExpansion[4*Key_index+1] + KeyExpansion[4*Key_index+2] + KeyExpansion[4*Key_index+3])
            keys_temp = self.arrays(keys_temp)
            keys.append(keys_temp)
        IInput = self.arrays(IInput)
        self.view(IInput)
        self.view(keys[-1])
        IInput = self.AddRoundKey(IInput, keys[-1])
        self.view(IInput)
        for index in range(self.Nr-1):
            IInput = self.InvShiftRows(IInput)
            self.view(IInput)
            IInput = self.InvSubBytes(IInput)
            self.view(IInput)
            self.view(keys[-1-1-index])
            IInput = self.AddRoundKey(IInput, keys[-1-1-index])
            self.view(IInput)
            IInput = self.InvMixColumns(IInput)
            self.view(IInput)
        IInput = self.InvShiftRows(IInput)
        self.view(IInput)
        IInput = self.InvSubBytes(IInput)
        self.view(IInput)
        self.view(keys[0])
        IInput = self.AddRoundKey(IInput, keys[0])
        self.view(IInput)
        IInput =self.Inv_arrays(IInput)
        IInput = bytes(IInput)
        return IInput

IInput = bytes.fromhex('69c4e0d86a7b0430d8cdb78070b4c55a')
Cipher_Key = bytes.fromhex('000102030405060708090a0b0c0d0e0f')
Out = IAES().IAES(IInput, Cipher_Key)
print(Out)

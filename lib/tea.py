"""
The MIT License

Copyright (c) 2005 hoxide

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from struct import pack as _pack
from struct import unpack as _unpack
from binascii import b2a_hex, a2b_hex

from random import seed
from random import randint as _randint

__all__ = ['TEA']

seed()

op = 0xffffffffL

def xor(a, b):
	a1,a2 = _unpack('>LL', a[0:8])
	b1,b2 = _unpack('>LL', b[0:8])
	r = _pack('>LL', ( a1 ^ b1) & op, ( a2 ^ b2) & op)
	return r

class TEA(object):
	"""
	Tiny Encryption Algorithm
	"""
	def __init__(self, key):
		self.k = key

	def encipher(self, v):
		"""
		TEA coder encrypt 64 bits value, by 128 bits key,
		>>> c = encipher('abcdefgh', 'aaaabbbbccccdddd')
		>>> b2a_hex(c)
		'a557272c538d3e96'
		"""
		n = 16 
		delta = 0x9e3779b9L
		k = _unpack('>LLLL', self.k[0:16])
		y, z = _unpack('>LL', v[0:8])
		s = 0
		for i in xrange(n):
			s += delta
			y += (op &(z<<4))+ k[0] ^ z+ s ^ (op&(z>>5)) + k[1]
			y &= op
			z += (op &(y<<4))+ k[2] ^ y+ s ^ (op&(y>>5)) + k[3]
			z &= op
		r = _pack('>LL',y,z)
		return r

	def encrypt(self, v):
		"""
		Encrypt Message follow QQ's rule.
		v is the message to encrypt, k is the key
		fill char is some random numbers (in old QQ is 0xAD)
		fill n char's n = (8 - (len(v)+2)) %8 + 2
		( obviously, n is 2 at least, n is 2-9)

		then insert (n - 2)|0xF8 in the front of the fill chars
		to record the number of fill chars.
		append 7 '\0' in the end of the message.
		
		thus the lenght of the message become filln + 8 + len(v),
		and it == 0 (mod 8)

		Encrypt the message .
		Per 8 bytes,
		the result is:
		
		r = encipher( v ^ tr, key) ^ to   (*)

		code is the QQ's TEA function.
		v is 8 bytes data to encrypt.
		tr is the result in preceding round.
		to is the data coded in perceding round, is v_pre ^ r_pre_pre

		For the first 8 bytes 'tr' and 'to' is zero.
		
		loop and loop, 
		that's end.
		
		>>> en = encrypt('', b2a_hex('b537a06cf3bcb33206237d7149c27bc3'))
		>>> decrypt(en,  b2a_hex('b537a06cf3bcb33206237d7149c27bc3'))
		''
		"""
		END_CHAR = '\0'
		FILL_N_OR = 0xF8
		vl = len(v)
		filln = (8-(vl+2))%8 + 2;
		fills = ''
		for i in xrange(filln):
			fills = fills + chr(_randint(0, 0xff))
		v = ( chr((filln -2)|FILL_N_OR)
			  + fills
			  + v
			  + END_CHAR * 7)
		tr = '\0'*8
		to = '\0'*8
		r = ''
		o = '\0' * 8
		for i in xrange(0, len(v), 8):
			o = xor(v[i:i+8], tr)
			tr = xor( self.encipher(o), to)
			to = o
			r += tr
		return r

	def decrypt(self, v):
		"""
		DeCrypt Message
		
		by (*) we can find out follow easyly:
		
		x  = decipher(v[i:i+8] ^ prePlain, key) ^ preCyrpt
		
		prePlain is pre 8 byte to be code.
		
		Attention! It's v per 8 byte value xor pre 8 byte prePlain,
		not just per 8 byte. 
		preCrypt is pre 8 byte Cryped.

		In the end of deCrypte the raw message,
		we have to cut the filled bytes which was append in encrypt.

		the number of the filling bytes in the front of message is
		pos + 1.
		
		pos is the first byte of deCrypted --- r[0] & 0x07 + 2

		the end of filling aways is 7 zeros.
		we can test the of 7 bytes is zeros, to make sure it is right.
		
		so return r[pos+1:-7]

		>>> r = encrypt('', b2a_hex('b537a06cf3bcb33206237d7149c27bc3'))
		>>> decrypt(r, b2a_hex('b537a06cf3bcb33206237d7149c27bc3'))
		''
		>>> r = encrypt('abcdefghijklimabcdefghijklmn', b2a_hex('b537a06cf3bcb33206237d7149c27bc3'))
		>>> decrypt(r, b2a_hex('b537a06cf3bcb33206237d7149c27bc3'))
		'abcdefghijklimabcdefghijklmn'
		>>> import md5
		>>> key = md5.new(md5.new('python').digest()).digest()
		>>> data='8CE160B9F312AEC9AC8D8AEAB41A319EDF51FB4BB5E33820C77C48DFC53E2A48CD1C24B29490329D2285897A32E7B32E9830DC2D0695802EB1D9890A0223D0E36C35B24732CE12D06403975B0BC1280EA32B3EE98EAB858C40670C9E1A376AE6C7DCFADD4D45C1081571D2AF3D0F41B73BDC915C3AE542AF2C8B1364614861FC7272E33D90FA012620C18ABF76BE0B9EC0D24017C0C073C469B4376C7C08AA30'
		>>> data = a2b_hex(data)
		>>> b2a_hex(decrypt(data, key))
		'00553361637347436654695a354d7a51531c69f1f5dde81c4332097f0000011f4042c89732030aa4d290f9f941891ae3670bb9c21053397d05f35425c7bf80000000001f40da558a481f40000100004dc573dd2af3b28b6a13e8fa72ea138cd13aa145b0e62554fe8df4b11662a794000000000000000000000000dde81c4342c8966642c4df9142c3a4a9000a000a'
		
		"""
		l = len(v)
		#if l%8 !=0 or l<16:
		#	return ''
		prePlain = self.decipher(v)
		pos = (ord(prePlain[0]) & 0x07L) +2
		r = prePlain
		preCrypt = v[0:8]
		for i in xrange(8, l, 8):
			x = xor(self.decipher(xor(v[i:i+8], prePlain)), preCrypt)
			prePlain = xor(x, preCrypt)
			preCrypt = v[i:i+8]
			r += x
		if r[-7:] != '\0'*7: 
			return None   
		return r[pos+1:-7]

	def decipher(self, v):
		"""
		TEA decipher, decrypt  64bits value with 128 bits key.

		it's the inverse function of TEA encrypt.

		>>> c = encipher('abcdefgh', 'aaaabbbbccccdddd')
		>>> decipher( c, 'aaaabbbbccccdddd')
		'abcdefgh'
		"""
		n = 16
		y, z = _unpack('>LL', v[0:8])
		a, b, c, d = _unpack('>LLLL', self.k[0:16])
		delta = 0x9E3779B9L;
		s = (delta << 4)&op
		for i in xrange(n):
			z -= ((y<<4)+c) ^ (y+s) ^ ((y>>5) + d)
			z &= op
			y -= ((z<<4)+a) ^ (z+s) ^ ((z>>5) + b)
			y &= op
			s -= delta
			s &= op
		return _pack('>LL', y, z)

def _test():
	import doctest, tea
	return doctest.testmod(tea)

if __name__ == "__main__":
	_test()


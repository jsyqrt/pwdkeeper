# coding: utf-8
# DES.py, a realization of DES with python

''' some boxes'''
ip=  (58, 50, 42, 34, 26, 18, 10, 2,
	  60, 52, 44, 36, 28, 20, 12, 4,
	  62, 54, 46, 38, 30, 22, 14, 6,
	  64, 56, 48, 40, 32, 24, 16, 8,
	  57, 49, 41, 33, 25, 17, 9 , 1,
	  59, 51, 43, 35, 27, 19, 11, 3,
	  61, 53, 45, 37, 29, 21, 13, 5,
	  63, 55, 47, 39, 31, 23, 15, 7)

ip_1=(40, 8, 48, 16, 56, 24, 64, 32,
	  39, 7, 47, 15, 55, 23, 63, 31,
	  38, 6, 46, 14, 54, 22, 62, 30,
	  37, 5, 45, 13, 53, 21, 61, 29,
	  36, 4, 44, 12, 52, 20, 60, 28,
	  35, 3, 43, 11, 51, 19, 59, 27,
	  34, 2, 42, 10, 50, 18, 58, 26,
	  33, 1, 41,  9, 49, 17, 57, 25)

e  =(32, 1,  2,  3,  4,  5,  4,  5, 
	   6, 7,  8,  9,  8,  9, 10, 11, 
	  12,13, 12, 13, 14, 15, 16, 17,
	  16,17, 18, 19, 20, 21, 20, 21,
	  22, 23, 24, 25,24, 25, 26, 27,
	  28, 29,28, 29, 30, 31, 32,  1)
 
p=(16,  7, 20, 21, 29, 12, 28, 17,
	 1, 15, 23, 26,  5, 18, 31, 10, 
	 2,  8, 24, 14, 32, 27,  3,  9,
	 19, 13, 30, 6, 22, 11,  4,  25)

s= [[[14, 4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
	 [0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
	 [4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
	 [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]],

	 [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
	 [3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
	 [0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15], 
	 [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]],

	 [[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
	 [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],   
	 [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
	 [1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],

	[[7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11,  12,  4, 15],
	 [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,9],
	 [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
	 [3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]],


	[[2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
	 [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
	 [4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
	 [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]],

	[[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
	 [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
	 [9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
	 [4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],

	[[4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
	 [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
	 [1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
	 [6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]],

   [[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
	 [1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
	 [7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
	 [2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]]
	 
pc1=(57, 49, 41, 33, 25, 17,  9,
	   1, 58, 50, 42, 34, 26, 18,
	  10,  2, 59, 51, 43, 35, 27,
	  19, 11,  3, 60, 52, 44, 36,
	  63, 55, 47, 39, 31, 23, 15,
	   7, 62, 54, 46, 38, 30, 22,
	  14,  6, 61, 53, 45, 37, 29,
	  21, 13,  5, 28, 20, 12, 4);

pc2= (14, 17, 11, 24,  1,  5,  3, 28,
	  15,  6, 21, 10, 23, 19, 12,  4, 
	  26,  8, 16,  7, 27, 20, 13,  2, 
	  41, 52, 31, 37, 47, 55, 30, 40, 
	  51, 45, 33, 48, 44, 49, 39, 56, 
	  34, 53, 46, 42, 50, 36, 29, 32)

d = (1,  1,  2,  2,  2,  2,  2,  2, 1, 2, 2, 2, 2, 2, 2, 1)

def des_encode(plaintext, key):
	plaintext = string_to_binary(plaintext)
	if isinstance(key, str):
		key = string_to_binary(key)
	else:
		key = hex_to_binary(key)
	l = len(plaintext)
	m = l / 64
	n = l % 64
	plaintext += [0 for i in range(n)]
	x = []
	for i in range(m):
		x += encode_a_block(plaintext[i*64:i*64+64], key)
	ciphertext = ''
	for i in range(0, len(x), 4):
		ciphertext += '{:x}'.format(x[i]*8 + x[i+1]*4 + x[i+2]*2 + x[i+3])
	return ciphertext

def des_decode(ciphertext, key):
	ciphertext = ciphertext_to_binary(ciphertext)
	if isinstance(key, str):
		key = string_to_binary(key)
	else:
		key = hex_to_binary(key)
	l = len(ciphertext)
	m = l / 64
	n = l % 64
	x = []
	for i in range(m):
		x += decode_a_block(ciphertext[i*64:i*64+64], key)
	plaintext = binary_to_plaintext(x)
	return plaintext

def binary_to_plaintext(x):
	def l_2_i(x):
		y = 0
		return sum([x[i]*pow(2,7-i) for i in range(8)])
	x =  ''.join([chr(l_2_i(x[i*8:i*8+8])) for i in range(len(x)/8)])
	return x

def ciphertext_to_binary(ciphertext):
	return list(map(int, reduce(lambda x,y:x+y, ['{:0>4b}'.format(int(i,16)) for i in ciphertext])))

def encode_a_block(x, key):
	key = Permute(key, pc1)
	x = Permute(x , ip)
	for i in range(16):
		key = key_round(key, i)
		k = Permute(key, pc2)
		x = an_encode_round(x[:32], x[32:64], k)
	x = x[32:64] + x[:32]
	x = Permute(x, ip_1)
	return x

def decode_a_block(x, key):
	keys = get_key(key)
	x = Permute(x , ip)
	for i in range(16):
		k = keys[15-i]
		x = an_encode_round(x[:32], x[32:64], k)
	x = x[32:64] + x[:32]
	x = Permute(x, ip_1)
	return x

def get_key(key):
	key = Permute(key, pc1)
	x = []
	for i in range(16):
		key = key_round(key, i)
		k = Permute(key, pc2)
		x.append(k)
	return x

def key_round(key, i):
	return key[:28][d[i]:28]+key[:28][:d[i]]+key[28:56][d[i]:28]+key[28:56][:d[i]]

def an_encode_round(left, right, key):
	righti = xor_all(left, ffunc(right, key))
	lefti = right
	return lefti + righti

def ffunc(right, key):
	x = xor_all(Extend(right), key)
	x = [[x[j*6+i] for i in range(6)] for j in range(8)]
	x = s_box(x)
	x = reduce(lambda x, y: x+y, x)
	x = Permute(x, p)
	return x

def xor_all(x, y):
	return [x[i] ^ y[i] for i in range(len(x))]

def Extend(x):
	return [x[i-1] for i in e]

def s_box(x):
	y = []
	for i in range(8):
		y.append(list(map(int,'{:0>4b}'.format((s[i][x[i][0]*2+x[i][-1]][x[i][1]*8+x[i][2]*4+x[i][3]*2+x[i][4]])))))
	return y

def Permute(x, y):
	return [x[i-1] for i in y]

def hex_to_binary(x):
	return list(map(int, reduce(lambda x,y:x+y, list(map(lambda i:'{:0>4b}'.format(int(i, 16)), '{:0>16x}'.format(x))))))

def string_to_binary(string):
	binary_list = reduce(lambda x, y: x+y, list(map(lambda i: list(map(int, '{:0>8b}'.format(ord(i)))), string)))
	return binary_list

def DES(msg, key, ty='d'):
	return {'d': des_decode, 'e': des_encode}[ty](msg, key)
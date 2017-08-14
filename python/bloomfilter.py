#!/usr/bin/python
"""
Implementation of a bloom filter

"""

from bitarray import bitarray
import hashlib

class BloomFilter(object):

    def __init__(self, bfSize=4096):
        self.bfSize = bfSize
        self.bitarray = bitarray(self.bfSize, endian='little')
        self.bitarray.setall(False)

    def hash(self, string):
        return [int(hashlib.sha1(str(string).encode('utf-8')).hexdigest(),16) % self.bfSize,
                int(hashlib.sha256(str(string).encode('utf-8')).hexdigest(),16) % self.bfSize,
                int(hashlib.sha384(str(string).encode('utf-8')).hexdigest(),16) % self.bfSize,
                int(hashlib.sha512(str(string).encode('utf-8')).hexdigest(),16) % self.bfSize]


    def insert(self, string):
        keys = self.hash(string)
        for k in keys:
            self.bitarray[k] = True

    def search(self, string):
        keys = self.hash(string)
        z = [ 1 if self.bitarray[k] == 1 else 0 for k in keys]

        if 0 in z:
            return False
        else:
            return True

    def duplicate(self):
        bf = BloomFilter()
        bf.bitarray = self.bitarray.copy()
        return bf

    def union(self, bf):
        unionBf = self.duplicate()
        unionBf.bitarray = unionBf.bitarray | bf.bitarray
        return unionBf 

    def intersection(self,bf): 
        interBf = self.duplicate()
        interBf.bitarray = interBf.bitarray & bf.bitarray
        return interBf 

if __name__=='__main__':
    bf = BloomFilter()
    bf.insert('tryeyuuuuueueire')

    if bf.search('tryeyuuuuueueire'):
        print( "Is present")
    else:
        print( "Is NOT  present")
    if bf.search('DDDFFFdfdfdruueueire'):
        print( "Is present")
    else:
        print( "Is NOT  present")
    #print(bf.bitarray)
    nbf = bf.duplicate()
    ubf = bf.union(nbf)
    ibf = bf.intersection(nbf)


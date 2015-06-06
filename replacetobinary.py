#!/usr/bin/env python
# coding: utf-8

import sys, codecs, re, binascii, os

HEXREF = r'<hexdata\s+src="(.+)"\s*/>'

def hexdump(filename):
    with open(filename, 'rb') as f:
        bin = f.read()
        hexdump = binascii.hexlify(bin)
        return hexdump

def replace(text):
    p = re.compile(HEXREF)
    m = p.search(text)
    if m:
        binfile = m.group(1)
        ret = "            <hexdata>\n                "
        ret+= hexdump(binfile)
        ret+= "\n            </hexdata>\n"
        return ret
    else:
        return text

def main(source, dest):
    destdir = os.path.dirname(dest)
    if not os.path.isdir(destdir):
        os.makedirs(destdir)
    
    with codecs.open(source, 'r', 'utf-8') as r:
        with codecs.open(dest, 'w', 'utf-8') as w:
            line = r.readline()
            
            while line:
                replaced = replace(line)
                w.write(replaced)
                line = r.readline()

                
if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    if argc != 3:
        print('Usage: $ python %s sourcefile targetfile' % argv[0])
        quit()
    main(argv[1], argv[2])
    
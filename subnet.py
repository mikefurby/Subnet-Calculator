#!/usr/bin/python
import sys
import time


def subnet_calc(ipadd,subnet):
    src = str(ipadd.split("/")[0])
    mask = int(ipadd.split("/")[1])
    a_low_address = int(src.split(".")[0])
    b_low_address = int(src.split(".")[1])
    c_low_address = int(src.split(".")[2])
    d_low_address = int(src.split(".")[3])
    blocksize = (256,128,64,32,16,8,4,2,1)
    maskindex = (0,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8)
    a_index = (maskindex[mask])
    b_index = (maskindex[mask-8])
    c_index = (maskindex[mask-16])
    d_index = (maskindex[mask-24])
    if mask <= 32:
        net = (d_low_address / blocksize[d_index])        
        d_low_address = (net * blocksize[d_index])         
        d_bcast = (d_low_address + blocksize[d_index]-1)
        bcast = (str(a_low_address) + "." + str(b_low_address) + "." + str(c_low_address) + "." + str(d_bcast) + "/" + str(mask))
    if mask <= 24:
        net = (c_low_address / blocksize[c_index])        
        c_low_address = (net * blocksize[c_index])         
        c_bcast = (c_low_address + blocksize[c_index]-1)
        bcast = (str(a_low_address) + "." + str(b_low_address) + "." + str(c_bcast) + "." + str(d_bcast) + "/" + str(mask))
    if mask <= 16:
        net = (b_low_address / blocksize[b_index])        
        b_low_address = (net * blocksize[b_index])         
        b_bcast = (b_low_address + blocksize[b_index]-1)
        bcast = (str(a_low_address) + "." + str(b_bcast) + "." + str(c_bcast) + "." + str(d_bcast) + "/" + str(mask))
    if mask <= 8:
        net = (a_low_address / blocksize[a_index])        
        a_low_address = (net * blocksize[a_index])         
        a_bcast = (a_low_address + blocksize[a_index]-1)
        bcast = (str(a_bcast) + "." + str(b_bcast) + "." + str(c_bcast) + "." + str(d_bcast) + "/" + str(mask))
    subnet = (str(a_low_address) + "." + str(b_low_address) + "." + str(c_low_address) + "." + str(d_low_address) + "/" + str(mask))
    print (subnet)
    print (bcast)
    return [subnet,bcast]


def main():
    if len( sys.argv ) <= 1:   #check the arguements into the script
        sys.stderr.write("example syntax, one arguement is required \n")
        sys.stderr.write("./subnet.py <ip_src\netmask>\n")
        sys.exit(1)

    subnet = []
    ipadd = sys.argv[1]
    subnet = subnet_calc(ipadd,subnet)
    print (subnet)
    print (subnet[0])
    print (subnet[1])
    return

main()

# the end

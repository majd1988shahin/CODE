import optparse
import sys
   
if __name__=="__main__":
    """parser = optparse.OptionParser("usage: %prog [options] arg1 arg2")
    parser.add_option("-H", "--host", dest="hostname",
                       default="127.0.0.1", type="string",
                       help="specify hostname to run on")
    parser.add_option("-P", "--port", dest="portnum", default=80,
                       type="int", help="port number to run on")"""
    parser = optparse.OptionParser()
    parser.add_option('-a', action="store_true", default=False)
    parser.add_option('-b', action="store", dest="b", default="b")
    parser.add_option('-c', action="store", dest="c", type="int",default=1)
    #print (parser.parse_args(['-a', '-bval', '-c', '3']))

    (options, args) = parser.parse_args()
    a = options.a
    b = options.b
    c = options.c
    print(a,b,c)
    print(options,args)
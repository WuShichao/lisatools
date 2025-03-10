#!/usr/bin/env python

from synthlisa import *
from Numeric import *

import sys

if len(sys.argv) < 3:
    print "Usage: %s <challenge-name> <xml source file> [<xml sourcefile> ...]" % sys.argv[0]

noisefile = sys.argv[1] + '-noise.xml'

print "synthLISA TDI generation script for challenge %s" % sys.argv[1]

print "Using geometry/noise XML file %s" % noisefile

inputXML = readXML(noisefile)

lisa = inputXML.getLISAGeometry()
tdinoise = inputXML.getTDInoise()

inputXML.close()

stime = 15
samples = 2**21

print "...making noise"

[t,Xm,Ym,Zm] = transpose(getobsc(samples,stime,[tdinoise.t,tdinoise.Xm,
                                                           tdinoise.Ym,
                                                           tdinoise.Zm]))

publicXML = lisaXML(sys.argv[1] + '.xml',author='Michele Vallisneri',
                                         comments='Public lisaXML for challenge '+sys.argv[1])

publicXML.LISAData(lisa,'LISA')
publicXML.NoiseData(tdinoise,'TDI noises',hideseed=1)
publicXML.TDIData(transpose([t,Xm,Ym,Zm]),samples,stime,'t,Xf,Yf,Zf')

publicXML.close()

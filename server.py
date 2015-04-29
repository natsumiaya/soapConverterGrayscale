#!/usr/bin/env python

from ladon.ladonizer import ladonize
import Image
import base64
import StringIO

class Convert(object):

    @ladonize(str,rtype=str)
    def grayscale(self,gambar):
    
        ba = bytearray(base64.b64decode(gambar))

        # Convert to string
        buff = StringIO.StringIO()
        buff.write(ba)
        #seek back to the beginning so the whole thing will be read by PIL
        buff.seek(0)
        img = Image.open(buff).convert('LA')

        # Convert to string
        output = StringIO.StringIO()
        img.save(output, format="PNG")
        contents = output.getvalue()
        output.close()

        # Send grayscale results to sink
        bytes = bytearray(contents)
        s = base64.b64encode(bytes)
        return s
    

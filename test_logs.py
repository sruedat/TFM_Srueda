# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import time, sys
sys.tracebacklimit = 0
sta = 0
#cadena=""

def main ():
    num = 0
    #print (st)
    while True:
        st = MaqEstados(num)
        num=st

        if st < 4:
            if st == 1:
               cad = "Estado 1"

            elif st == 2:
                cad = "Estado 2"

            elif st ==3:
                cad = "Estado 3"

            print (cad)

        elif st==4:

            break

        return cad







def MaqEstados(n):
    if n==0:
        time.sleep(2)
        num = 1

    elif n==1:
         time.sleep(2)
         num = 2

    elif n == 2:
         time.sleep(2)
         num = 3

    elif n==3:
         num = 4

    else:
         num = 0

    return num



#def main(numero):
 #   Mensajes(numero)
    #cadena = Mensajes(numero)
    #print (cadena)
    #return cadena

if __name__ == '__main__':
    main()







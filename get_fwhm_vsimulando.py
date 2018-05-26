import math
import json
import urllib.request
import datetime
import time

FILTER_LAMBDA = {'J0430': 430, 'gSDSS': 475, 'rSDSS': 625, 'iSDSS': 773, 'J0861': 861, 'zSDSS': 915, 'uJAVA': 348,
                 'J0378': 378, 'J0395': 395, 'J0410': 410, 'J0515': 515, 'J0660': 660}
FILTER_ZP = {'uJAVA': 21.80, 'J0378': 21.00, 'J0395': 20.80, 'J0410': 21.64, 'J0430': 21.61, 'gSDSS': 23.70,
             'J0515': 21.65, 'rSDSS': 23.70, 'J0660': 21.10, 'iSDSS': 23.40, 'J0861': 21.60, 'zSDSS': 22.60}

SQL_IMAGES = """SELECT oa.name, TIMESTAMP(oa.date, oa.time) AS datetime, fwhmg, fwhm_mean, f.name, airmass, INSERTDATE_CR 
FROM t80oa oa JOIN rc ON oa.id = rc.ori_id join filter f ON oa.filter_id = f.id WHERE FWHMG IS NOT NULL 
AND oa.date >= DATE('{0}') AND oa.time > TIME('{1}') ORDER BY 2"""

SQL_SEEING = """SELECT datetime, seeing FROM seeing.seeingdata WHERE datetime >= TIMESTAMP(DATE('{0}'), TIME('{1}')) AND flag = 0 ORDER BY 1"""


def query_adql_by_http(query, url):
    data = json.dumps({'query': query})
    content = urllib.request.urlopen(url, bytearray(data, 'utf-8')).read()
    d = json.loads(content.decode('utf-8'))
    if d.get('error'):
        raise Exception(d['error'])

    return d['rows']


def get_seeing_data(timestamp, url):
    """
    Query for the available 'seeing' data form five minutes before the 'timestamp'.
    """
    t2 = (timestamp - datetime.timedelta(minutes=5)).isoformat()

    sql = SQL_SEEING.format(t2[:10], t2[11:16])
    res = query_adql_by_http(sql, url)

    return [(datetime.datetime.strptime(x[0], '%Y-%m-%dT%H:%M:%S'), float(x[1])) for x in res]


def get_seeing_at(timestamp, seeing):
    """Get the median seeing from measures 5 minutes before and after the 'timestamp'"""
    t_min = timestamp - datetime.timedelta(minutes=5)
    t_max = timestamp + datetime.timedelta(minutes=5)
    s_data = []
    for s in seeing:
        if s[0] >= t_min and s[0] <= t_max:
            s_data.append(s[1])

    if len(s_data) == 0:
        return None

    s_data.sort()

    return s_data[len(s_data) % 2]


def get_expected_psf(img, seeing):
    s = get_seeing_at(img['timestamp'], seeing)
    if s is None: return None

    return s * math.pow(img['airmass'], 0.6) * (math.pow(FILTER_LAMBDA[img['filter']], -0.2) / 0.2885399811814427)


def query_images_since(timestamp, url='http://upad.oaj.cefca.es/reduction/t80commcpd/exec_adql'):
    result = []
    seeing = get_seeing_data(timestamp, url)
    itmtp = timestamp.isoformat()
    sql = SQL_IMAGES.format(itmtp[:10], itmtp[11:16])
    res = query_adql_by_http(sql, url)
    for i in range(len(res)):
        cur = res[i]
        img = {'name': cur[0],
               'timestamp': datetime.datetime.strptime(cur[1], '%Y-%m-%dT%H:%M:%S'),
               'fwhmg': float(cur[2]), 'fwhm_mean': cur[3],
               'filter': cur[4], 'airmass': float(cur[5]),
               'insertdate': datetime.datetime.strptime(cur[6], '%Y-%m-%dT%H:%M:%S')}

        img['expected_psf'] = get_expected_psf(img, seeing)

        result.append(img)

    return result


if __name__ == '__main__':
    #Se introducen imágenes repetidas
    last_img=[]
    #para simulador de horas
    fecha_inicio=datetime
    fecha_inicio.datetime.year=2018
    fecha_inicio.datetime.mes=5
    fecha_inicio.datetime.dia=12
    fecha_inicio.datetime.hora=22
    fecha_inicio.datetime.minuto=0
    while (True):
        # get actual date
        #now=datetime.datetime.now()
        #SIMULADOR TIEMPO
        now = datetime.datetime.now() + datetime.timedelta(minutes=5)
        print(now)

        # get data
        result = query_images_since(datetime.datetime(now.year, now.month, now.day, now.hour, now.minute))
        #result = query_images_since(datetime.datetime(2018, 5, 18, 22, 0))

        # Esto sólo es para comprobar si funciona bien
        # Borrarrrrrrr
        if len(result) > 0:
            print("Total", len(result))
            print(result)
            #for i in range(len(result)):
            #    img = result[i]
            #    print("Image %s" % i)
            #    print("   name:", img['name'])
            #    print("   filter:", img['filter'])
            #    print("   timestamp:", img['timestamp'])
            #    print("   fwhmg (PSF):", img['fwhmg'])
            #    print("   expected_psf:", img['expected_psf'])

        #####################################################################

        # if there are data
        if len(result)>0:
            if len(last_img)>0:
            #delete images already introduced
                for i in range (len(last_img)):
                    for e in range (len(result)):
                        if last_img[i]==result[e]:
                            #print ("repetidas: %s" % result[e])
                            result.remove(result[e])
                            break


            print("Total nuevas", len(result))
            for i in range (len(result)):
                img = result[i]
                print("Image %s" % i)
                print("   name:", img['name'])
                print("   filter:", img['filter'])
                print("   timestamp:", img['timestamp'])
                print("   fwhmg (PSF):", img['fwhmg'])
                print("   expected_psf:", img['expected_psf'])
            last_img = result
        else:
            print('No new imagenes available')
        time.sleep (300)







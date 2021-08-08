import guiAPI
import math


def calculo(hidrometro, temperatura):
    apiobservado = float(hidrometro)
    temperatura = float(temperatura)

    presion = 0

    densidad = (141.5 / (apiobservado + 131.5)) * 999.016

    hyc = 1 - (0.00001278*(temperatura-60))-(0.0000000062*(temperatura-60)**2)

    densidad = hyc*densidad

    densidad60 = densidad

    tc90 = (temperatura - 32) / 1.8
    t = tc90 / 630
    a1 = -0.148759
    a2 = -0.267408
    a3 = 1.08076
    a4 = 1.269056
    a5 = -4.089591
    a6 = -1.871251
    a7 = 7.438081
    a8 = -3.536296

    dtt = (a1 + (a2 + (a3 + (a4 + (a5 + (a6 + (a7 + a8 * t) * t) * t) * t) * t) * t) * t) * t
    tc68 = tc90 - dtt
    tf68 = 1.8 * tc68 + 32

    k0 = 341.0957
    k1 = 0
    k2 = 0
    Da = 2
    s60 = 0.01374979547

    i = 0
    spo = 1
    v = math.fabs(spo)
    
    while i < 15 or v < 0.0001:

        a = (s60 / 2) * ((((k0 / densidad60) + k1) / densidad60) + k2)
        b = (2 * k0 + k1 * densidad60) / \
            (k0 + (k1 + k2 * densidad60) * densidad60)
        de = densidad60 * \
            (1 + ((math.exp(a * (1 + 0.8 * a)) - 1) / (1 + a * (1 + 1.6 * a) * b)))
        alfa60 = k2 + ((k0 / de) + k1) / de

        dt = tf68 - 60.0068749
        ctlc = math.exp(-alfa60 * dt * (1 + 0.8 * alfa60 * (dt + s60)))
        fp = math.exp(-1.9947 + 0.00013427 * tf68 +
                      ((793920 + 2326 * tf68) / de ** 2))
        cpl2 = 1 / (1 - fp * presion * 0.00001)
        ctpl2 = ctlc * cpl2
        dt2 = temperatura - 60
        x = densidad60 * ctpl2
        spo = densidad60 - x
        v=math.fabs(spo) 
        e = (densidad / (ctlc * cpl2)) - densidad60
        dtm = 2 * alfa60 * dt2 * (1 + 1.6 * alfa60 * dt2)
        dp = (Da * cpl2 * presion * fp * (7.9392 +
              0.02326 * temperatura)) / (densidad60 ** 2)
        ddensidad60 = e / (1 + dtm + dp)
        i += 1

    densidad60 = densidad60 + ddensidad60
    densidad60 = round(densidad60,1)

    return densidad60

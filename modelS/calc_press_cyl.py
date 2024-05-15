import numpy as np

def model_s(r:float, d:float, alpha:float, M=0):
    """calcul du coefficient de transmission applicable sur la face "à l'ombre" d'un hemicylindre

    :param r: Rayon de l'hemicylindre
    :type r: float
    :param d: Distance entre le centre de la charge et la face externe de l'hemicylindre
    :type d: float
    :param alpha: angle de mesure
    :type alpha: float
    :param M: masse, defaults to 0.
    :type M: float, optional
    :return: l'angle limite de vue de la charge, le coefficient de transmission à l'angle alpha, la distnace reduite shiftée 
    :rtype: list
    """
    
    x0 = d+r
    b0 = -2*x0
    # Delta = 0 donne :
    k = np.sqrt((r**2)/(x0**2-r**2))
    a0 = (1+k**2)
    # Donc 
    x_lim = - b0/(2*a0)
    y_lim = k*x_lim
    lda_lim = np.sqrt(x_lim**2+y_lim**2)

    alpha_lim = np.rad2deg(np.arctan(y_lim/(x0-x_lim)))

    if alpha < alpha_lim:
        return alpha_lim, 0, 0    
    # coefficient
    a = 0.396
    b = -1.4385
    c = 1.347
    
    alpha = 180-alpha
    
    lda = np.sqrt((d+r+r*np.cos(np.deg2rad(alpha)))**2+((r*np.sin(np.deg2rad(alpha)))**2))
    # surpression UFC
    # dico_Z, dico_val = ufc.param_blast('hemispherique')
    # p_ufc =  np.asarray(dico_val["Pso"])*0.0689476
    # z_UFC = np.asarray(dico_Z["Pso"])*0.3048/0.76834
    
    # z_lda = lda/(M**(1/3.))
    # press = ufc.ponderation(z_lda, z_UFC, p_ufc)
    
    rsdd = (lda-lda_lim)/r
    ct = a*rsdd**2 + b*rsdd + c
    #press_hemi = Ct*press
    
    return alpha_lim, ct


# geoms = [
#     # {'D': 2.5, 'R':1.25, 'M':200},
#     # {'D':1.0, 'R': 2.5, 'M':200},
#     {'D': 0.6, 'R':0.2, 'M':0.05}
#     ]

# for geom in geoms:

#     angles, coef, l_rsdd  = [], [], []
#     for angle in np.linspace(0,180,181):
        
#         angles.append(angle)
#         a_lim, Ct, rsdd = model_s(geom["R"], geom["D"], angle, geom['M'])
#         l_rsdd.append(rsdd)

#         if angle < a_lim :
#             coef.append(0)
#         else:
#             coef.append(Ct)

#     print(coef)
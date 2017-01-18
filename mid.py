import math
# step 1
def gravity(n):

    dangle_0 = angle_0 / 100
    z_0 = math.tan(1.0 / 2.0 * angle_0)
    c = v_0 /\
    (z_0**(n-1.0) * (1.0+z_0)**2.0)
    angle = angle_0 + dangle_0
    z = math.tan(1.0 / 2.0 * angle)
    v = c * z ** (n-1.0) * (1.0+z**2.0)
    delta_t = c / g * (z**(n-1.0) * (1.0/(n-1.0)+z**2.0/(n+1.0)) \
    - z_0**(n-1.0) * (1.0/(n-1.0) + z_0**2.0/(n+1.0)))
    delta_x = 1.0 / 2.0 * (v_0 * math.sin(angle_0)\
    + v * math.sin(angle)) * delta_t
    delta_y = 1.0 / 2.0 * (v_0 * math.cos(angle_0) + v * math.cos(angle))*dangle_0
    x = x

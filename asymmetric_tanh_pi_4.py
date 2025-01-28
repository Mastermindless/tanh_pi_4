import math

# asymmetric_tanh_pi_4()
def asymetric_tanh_pi_4(x):
    return ((np.exp(math.pi/4 * x)) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
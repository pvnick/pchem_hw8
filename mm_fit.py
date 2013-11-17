from scipy.optimize import curve_fit

def michaelisMenten(sConc, vMax, kM):
    return vMax / (1 + kM / sConc)

sConcArr = [0.050, 0.017, 0.010, 0.005, 0.002]
rateArr = [0.0002767, 0.0002067, 0.0001683, 0.0001100, 0.0000550]
optimizedParams, covariance = curve_fit(michaelisMenten, sConcArr, rateArr)

print("Vmax = " + str(optimizedParams[0]))
print("Km = " + str(optimizedParams[1]))
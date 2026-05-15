# add necessary imports
import matplotlib.pyplot as plt
import numpy as np

# constants

G = 4*np.pi**2

mass = {
    'sun': 1.0,
    'earth': 3.0034e-6,
    'moon': 3.6923e-8}

r0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([9.978977040419635E-01, 6.586825681892025E-02, -6.320430920521123E-06]),
    'moon': np.array([9.956768547953816E-01, 6.676030485840675E-02, 1.641093070596718E-04])
     }
v0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([-4.70015711e-01, 6.25165839e+00, -3.40817831e-04]),
    'moon': np.array([-0.55065949, 6.03534661, 0.01111456])
}

#r_values = []
#r_E = []
#r_M = []

# functions
def integrate_earth(tmax, dt=1e-3):
    #trajectory = 
    time = np.arange(0, tmax, dt)
    rE = r0['earth'].copy()
    vE = v0['earth'].copy()
    r_values = [rE.copy()]    
    for t in time:
        rE = rE + vE * dt
        vE = vE + F_ES(rE) * dt / mass['earth']
        r_values.append(rE.copy())
    return np.array(r_values)

#return a tuple (r_E, r_M) with the Earth and Moon trajectories, each a (N, 3) array
def integrate_EM(tmax, dt=1e-3):
    time = np.arange(0, tmax, dt)
    rE = r0['earth'].copy()
    vE = v0['earth'].copy()
    rM = r0['moon'].copy()
    vM = v0['moon'].copy()   
    r_E = [rE.copy()] 
    r_M = [rM.copy()] 
    for t in time:
        rE = rE + vE * dt
        rM = rM + vM * dt
        #might need F_E instead of F_ES
        #vE = vE + F_ES(rE) * dt / mass['earth']
        #vM = vM + F_MS(rM) * dt / mass['moon']
        vE = vE + F_E(rE, rM) * dt / mass['earth']
        vM = vM + F_M(rE, rM) * dt / mass['moon']
        r_E.append(rE.copy())
        r_M.append(rM.copy())
    #return np.array(r_E, r_M)
    return (r_E, r_M)

def F_gravity(ri, rj, mi, mj):
    bold_r_ij = ri - rj
    light_r_ij = np.sqrt((bold_r_ij[0] * bold_r_ij[0]) + (bold_r_ij[1] * bold_r_ij[1]) + (bold_r_ij[2] * bold_r_ij[2]))
    r_hat_ij = bold_r_ij / light_r_ij 
    Force_gravity = (((G * mi * mj)/light_r_ij**2) * r_hat_ij) * -1
    return Force_gravity


#calculates the force on the Earth due to the Sun
def F_ES(rE):
    bold_rE = rE - rs
    light_rE = np.sqrt((bold_rE[0] * bold_rE[0]) + (bold_rE[1] * bold_rE[1]) + (bold_rE[2] * bold_rE[2]))
    r_hat_E = bold_rE / light_rE 
    Force_Earth_Sun = (((G * mi * ms)/light_rE**2) * r_hat_E) * (-1)
    return Force_Earth_Sun

#calculate the force from the Moon on the Earht
def F_EM(rE, rM):
    bold_rM = rM - rE  #changed rj to rM, and ri to rE
    light_rM = np.sqrt((bold_rM[0] * bold_rM[0]) + (bold_rM[1] * bold_rM[1]) + (bold_rM[2] * bold_rM[2]))
    r_hat_M = bold_rM / light_rM 
    Force_Moon_Earth = (((G * mj * mi)/light_rM**2) * r_hat_M)
    return Force_Moon_Earth 

#force of the Earth on the Moon
def F_ME(rE, rM):
    bold_rE = rE - rM  #changed rj to rM, and ri to rE
    light_rE = np.sqrt((bold_rE[0] * bold_rE[0]) + (bold_rE[1] * bold_rE[1]) + (bold_rE[2] * bold_rE[2]))
    r_hat_E = bold_rE / light_rE 
    Force_Earth_Moon = (((G * mj * mi)/light_rE**2) * r_hat_E)
    return Force_Earth_Moon

#force from the Sun on the Moon
def F_MS(rM):
    bold_rS_s = rs - rM   #changed rj to rM
    light_rS_s = np.sqrt((bold_rS_s[0] * bold_rS_s[0]) + (bold_rS_s[1] * bold_rS_s[1]) + (bold_rS_s[2] * bold_rS_s[2]))
    r_hat_S_s = bold_rS_s / light_rS_s 
    Force_Sun_Moon = (((G * mj * ms)/light_rS_s**2) * r_hat_S_s)
    return Force_Sun_Moon

#returns the total force on the Earht (from Sun and Moon)
def F_E(rE, rM):
    Force_Earth_Total = F_ES(rE) + F_EM(rE, rM)  #need force on earth due to moon
    return Force_Earth_Total

#total force on the Moon (from Sun and Earth)
def F_M(rE, rM):  
    Force_Moon_Total = F_ME(rE, rM) + F_MS(rM)
    return Force_Moon_Total
# calling numpy arrays for earth and moon

#assume i = earth, and j = moon
ri = r0['earth']
rj = r0['moon']
rs = r0['sun']
mi = mass['earth']
mj = mass['moon']
ms = mass['sun']
#rE = ri

print(F_E(r0['earth'], r0['moon']))


if __name__ == "__main__":
    # create the trajectory for 1 year
    
    #print(r_values)
    r_values = integrate_earth(1, dt=1e-3)
    print(r_values[:10])
    print(r_values.shape)
    
    # plot
    plt.plot(r_values[:, 0], r_values[:, 1])
    plt.xlabel("x (AU)")
    plt.ylabel("y (AU)")
    plt.gca().set_aspect("equal")     
    plt.savefig("orbit_earth_only.png")
    #Write the figure to the file "orbit_earth_only.png"

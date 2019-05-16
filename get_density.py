rho_al = 2700
mass_alskin = [0.295, 0.343, 0.387]

rho_steel = 8050
mass_steelskin = [0.652, 0.832, 1.044]

t_skin = [0.8e-3, 1e-3, 1.2e-3]
t_core = 30e-3




def get_density(m, t_skin, rho_skin, t_core, l=1, w=0.05):
    
    V_skin = l*w*t_skin
    m_skin = V_skin * rho_skin

    deltaM = m - (2 * m_skin)
    V_core = l*w*t_core

    return (deltaM/V_core)

density_1 = []
density_2 = []


for i in range(3):
    density_1.append(get_density(mass_alskin[i], t_skin[i], rho_al, t_core))
    

for i in range(3):
    density_2.append(get_density(mass_steelskin[i], t_skin[i], rho_steel, t_core))

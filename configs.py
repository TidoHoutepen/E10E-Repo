"""
E_fx - Young's modulus of skin
E_cx - Young's modulus of core
b - width of panel
t - thickness of skin
c - thickness of honeycomb
d = c + t
"""

import xlwt

wb = xlwt.Workbook()

sheet = wb.add_sheet('data')

sheet.write(0,0, 'Skin material')
sheet.write(0,1, 'Core material')
sheet.write(0,2, 'Skin thickness [mm]')
sheet.write(0,3, 'Core thickness [mm]')
sheet.write(0,4, 'Flexural rigidity')
sheet.write(0,5, 'Mass [kg]')
sheet.write(0,6, 'Flexural rigidity / mass')
sheet.write(0,7, 'Natural frequency [Hz]')


pi = 3.1415

class config():

    length = 0.9
    width = 0.05

    row = 0

    def __init__(self, E_skin, E_core, t_skin, t_core, rho_skin, rho_core):
        self.E_skin = E_skin
        self.E_core = E_core
        self.t_skin = t_skin
        self.t_core = t_core
        self.d = t_skin + t_core
        self.mass = 2 * config.get_mass(rho_skin, self.length, self.width, t_skin) + config.get_mass(rho_core, self.length, self.width, t_core)
        config.row += 1
        self.EI = self.flexural_rigidity()
        self.nat_freq = self.natural_freq()

    @staticmethod
    def get_mass(rho, l, w, t):
        return rho * l * w * t

    def flexural_rigidity(self):
        calc_1 = (self.E_skin * config.width * (self.t_skin**3))/6
        calc_2 = (self.E_skin * config.width * self.t_skin * (self.d**2))/2
        calc_3 = (self.E_core * config.width * (self.t_core**3))/12

        result = calc_1 + calc_2 + calc_3

        return result

    def natural_freq(self):
        return (1 / (2 * pi)) * ((self.EI/(self.mass * (config.length ** 3)))**0.5)

    def get_data(self):
        if self.E_skin == 72.4e9:
            material_skin = "Aluminium"
        elif self.E_skin == 210e9:
            material_skin = "Steel"
        else:
            material_skin = "Carbon Fibre"

        if self.E_core == 1.118e9:
            material_core = "Aramid honeycomb"
        elif self.E_core == 4.16e9:
            material_core = "Foam"
        else:
            material_core = "Aluminium"


       
        sheet.write(self.row,0, material_skin)
        sheet.write(self.row,1, material_core)
        sheet.write(self.row,2, self.t_skin * 1000)
        sheet.write(self.row,3, self.t_core * 1000)
        sheet.write(self.row,4, self.EI)
        sheet.write(self.row,5, self.mass)
        sheet.write(self.row,6, self.EI/self.mass)
        sheet.write(self.row,7, self.nat_freq)
       



E_al = 72.4e9 
E_steel = 210e9 
E_carb = 48.5e9
E_al_core = 0.8e9
E_foam = 4.16e9 
E_aramid = 1.118e9

rho_aluminium = 2700
rho_aluminium_core = 48
rho_steel = 8050
rho_carbon = 1470
rho_aramid = 82
rho_foam = 100

al_t = [0.8e-3, 1e-3, 1.2e-3]
steel_t = [0.8e-3, 1e-3, 1.2e-3]
carbon_t = [0.75e-3, 1e-3]

aramid_t = [10e-3, 16e-3]
foam_t = 22.5e-3
alum_core_t = [12e-3, 30e-3]

тес


for skin_t in al_t:
    test = config(E_al, E_aramid, skin_t, aramid_t[0], rho_aluminium, rho_aramid)
    test.get_data()

for skin_t in al_t:
    for core_t in alum_core_t:
        test = config(E_al, E_al_core, skin_t, core_t, rho_aluminium, rho_aluminium_core)
        test.get_data()

for skin_t in steel_t:
    test = config(E_steel, E_aramid, skin_t, aramid_t[0], rho_steel, rho_aramid)
    test.get_data()

for skin_t in steel_t:
    for core_t in alum_core_t:
        test = config(E_steel, E_al_core, skin_t, core_t, rho_steel, rho_aluminium_core)
        test.get_data()

for skin_t in carbon_t:
    for core_t in aramid_t:
        test = config(E_carb, E_aramid, skin_t, core_t, rho_carbon, rho_aramid)
        test.get_data()

for skin_t in carbon_t:
    test = config(E_carb, E_foam, skin_t, foam_t, rho_carbon, rho_foam)
    test.get_data()

wb.save('flexural_rigidity.xls')



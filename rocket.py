class stage:
    def __init__(self, fuel_mass, mass, fuel_ejection, thrust):
        self.fuel_mass = fuel_mass
        self.mass = mass
        self.fuel_ejection = fuel_ejection
        self.thrust = thrust


stage_number = int(raw_input('number of stages: '))
stages = []


for i in range(stage_number):
    stages.append(stage(int(raw_input("Fuel mass: ")), int(raw_input("Mass: ")), int(raw_input("Fuel ejection: ")), int(raw_input('Thrust: '))))


for i in range(stage_number):
    print 'stage', i+1, ':', stages[i].fuel_mass
    print 'stage', i+1, ':', stages[i].mass
    print 'stage', i+1, ':', stages[i].fuel_ejection
    print 'stage', i+1, ':', stages[i].thrust


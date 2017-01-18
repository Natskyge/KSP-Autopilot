# define the a stage of the rocket
class stage:

    def __init__(self, fuel_mass, isp, thrust):
        self.fuel_mass = fuel_mass
        self.isp = isp
        self.thrust = thrust
        self.flow_rate = thrust / ( isp * 9.82 )


# get the number of stages, initialize the list for storing the specs and
# get the total mass
stage_number = int(raw_input('number of stages: '))
stages = []
total_mass = int(raw_input('Total mass: '))


# the inputs for the specs of the rocket
for i in range(stage_number):
    stages.append(stage(
        int(raw_input("Fuel mass: ")), \
        int(raw_input("Isp: ")), \
        int(raw_input('Thrust: '))
))


# open file to write the data too and declare current mass of rocket
data = open('data.txt', 'w')
current_mass = total_mass


for i in range(len(stages)):

    # initialize the mass and run loop til there is no more fuel in stage
    remaing_fuel = stages[i].fuel_mass
    while remaing_fuel > 0:

        # calculate acceleration when there is less fuel left
        # than expelled per second
        if remaing_fuel <= stages[i].flow_rate:
            force = stages[i].thrust * 1000 * \
                    (remaing_fuel / stages[i].flow_rate)
            mass = current_mass
            remaing_fuel -= remaing_fuel
            current_mass -= remaing_fuel
            output = '%f \n' % float(force/mass)
            data.write(output)

        # calculate acceleration when there is more fuel
        # than expelled per second
        else:
            force = stages[i].thrust * 1000
            mass = current_mass
            remaing_fuel -= stages[i].flow_rate
            current_mass -= stages[i].flow_rate
            output = '%f \n' % float(force/mass)
            data.write(output)


# closing file
data.close()


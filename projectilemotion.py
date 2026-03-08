import math

print("Projectile Motion Program Start")

# input
u = float(input("Initial velocity (m/s): "))
theta = float(input("Angle (degree): "))

g = 9.8
theta_rad = math.radians(theta)

# calculation
T = (2*u*math.sin(theta_rad))/g
H = (u*u*(math.sin(theta_rad))**2)/(2*g)
R = (u*u*math.sin(2*theta_rad))/g

# screen output
print("\n----- RESULT -----")
print("Time of Flight =", T)
print("Maximum Height =", H)
print("Range =", R)

# file output
f = open("projectile output.txt","w")
f.write("Time of Flight = " + str(T) + "\n")
f.write("Maximum Height = " + str(H) + "\n")
f.write("Range = " + str(R) + "\n")
f.close()

print("\nOutput print → projectileoutput.txt")
input("prit the output")

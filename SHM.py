import math

# Input parameters later
A = float(input("Enter Amplitude (A): "))
omega = float(input("Enter Angular Frequency (omega): "))
phi = float(input("Enter Phase Constant (phi): "))
t = float(input("Enter Time (t): "))

# SHM equation
x = A * math.sin(omega * t + phi)

print("\nDisplacement =", x)















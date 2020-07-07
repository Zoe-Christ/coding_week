
print("Hello, Visual Studio")


from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()


# Das ist der erste Kommentar
spam = 1                    # und dies ist der zweite Kommentar
                            # ... und jetzt ein dritter!
string = "# Dies ist kein Kommentar."


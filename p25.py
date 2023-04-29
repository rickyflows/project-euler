#!/usr/bin/env python3
from numpy import sqrt, log10

# For large n, log(F_n) ~ log(1/sqrt(5)) + n * log(\phi)
# We want n satisfying n >= (999 - log(1/sqrt(5))) / log(\phi)
phi = (1 + sqrt(5))/2
print((999 - log10(1/sqrt(5))) / log10(phi))

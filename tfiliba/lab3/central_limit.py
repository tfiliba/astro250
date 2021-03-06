import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.stats import poisson

# sum n random variables
n=1000
# take the sum
trials = 1000

mu=3

# generate random variables
randomsamples = poisson.rvs(mu,size=[n,trials])
# sum 
sums = np.sum(randomsamples,axis=0)
average_sums = sums*1./n # ARP: why multiply by inverse, rather than just divide?
print 'mean:' + `np.mean(average_sums)` + ' std dev: ' + `np.std(average_sums)`
print 'expected mean:' + `mu` + ' expected std dev:' + `np.sqrt(mu*1./n)`
# ARP: spot on.

z_scores = (average_sums-mu)/np.sqrt(mu*1./n)
plt.hist(z_scores,100, normed=True) # ARP: does this improve with n?

# plot from z=-5 to z=5
z = np.linspace(-5,5,500)
#plot the normal pdf
plt.plot(z,norm.pdf(z))
plt.show() # ARP: looks like you were missing this...

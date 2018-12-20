#import timeit
import numpy as np
#from scipy.ndimage import convolve
#
#repeat = 10
#total = 10
#
#setup = """
#import numpy as np
#from scipy.ndimage import convolve
#SigmaSpins = np.random.choice((-1, 1), (50, 50))
#
#def Energy2(sigmaconfig):
#    return -1*np.sum(np.roll(sigmaconfig,1,axis=0)+np.roll(sigmaconfig,-1,axis=0)+np.roll(sigmaconfig,1,axis=1)+np.roll(sigmaconfig,-1,axis=1))
#    
#def Energy3(sigmaconfig):
#    return -1*np.sum(convolve(sigmaconfig, np.ones(sigmaconfig.shape), mode='wrap'))
#"""
#
#test5 = """
#print(Energy2(SigmaSpins))
#"""
#
#test6 = """
#print(Energy3(SigmaSpins))
#"""
#
#print('test5')
#timeconvergence5 = sum(timeit.Timer(test5, setup=setup).repeat(repeat, total))/10
#print('test6')
#timeconvergence6 = sum(timeit.Timer(test6, setup=setup).repeat(repeat, total))/10
#
#print('test5')
#print(timeconvergence5)
#print('test6')
#print(timeconvergence6)
#
#def Energy3(sigmaconfig):
#    return -1*np.sum(convolve(sigmaconfig, np.ones(sigmaconfig.shape), mode='wrap'))
#
#print(Energy3(np.ones((3,3))))

SigmaSpins = np.random.choice((-1, 1), (50, 50))
x=np.repeat(SigmaSpins[:,:,np.newaxis], 5, axis=2)
print(x)
print(x[:,:,1])
print(SigmaSpins)
print(x[:,:,1]==SigmaSpins)
print(np.sum(np.logical_and(x[:,:,1], SigmaSpins)))
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 10:27:22 2014

@author: longqi
"""

from pylab import *
import matplotlib.patheffects as path_effects

x = arange(0,20,.3)
y = sin(x)

close('all')
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'])

figure()

plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],3)

figure()
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],bbox_to_anchor=(0.5,0.5),loc=10)


figure()
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],bbox_to_anchor=(1.02,0.8),loc='center left')


figure()
ax = gca()
ax.set_position([0.1,0.1,0.7,0.85])
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],bbox_to_anchor=(1.02,0.8),loc='center left')


figure()
plot(x,y,'darkblue',lw=2,marker='*',mfc='lightgreen',ms=12,mec='darkgreen',mew=1)
legend(['$sin(x)$'],loc='best',fancybox=True,shadow=True,numpoints=1,)


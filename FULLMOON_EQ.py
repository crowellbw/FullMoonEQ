import numpy
import math
import datetime
import matplotlib.pylab as plt

#LOAD Full moon data, convert to Days since Jan 1 1970 
a = numpy.loadtxt('fullmoon_dates.txt')

fm_day = a[:,0].astype(float)
fm_month = a[:,1].astype(float)
fm_year = a[:,2].astype(float)

fm_days = numpy.zeros((len(fm_day),1))
for i in range(0,len(fm_day)):
	date = datetime.datetime(int(fm_year[i]),int(fm_month[i]),int(fm_day[i]))
	fm_days[i] = (numpy.datetime64(date) - numpy.datetime64('1970-01-01T00:00:00'))/ numpy.timedelta64(1, 'D')

#LOAD Earthquake Catalog, convert to Days since Jan 1 1970
b = numpy.loadtxt('eq_catalog.txt',dtype=str)
eq_tstamp = b[:,0]
eq_mag = b[:,4].astype(float)

eq_days = numpy.zeros((len(eq_tstamp),1))
for i in range(0,len(eq_tstamp)):
	stime = numpy.datetime64(eq_tstamp[i]).item()
	eq_days[i] = (numpy.datetime64(stime) - numpy.datetime64('1970-01-01T00:00:00'))/ numpy.timedelta64(1, 'D')

#Find the closest full moon date to earthquake

closestFM = numpy.zeros((len(eq_days),1))
for i in range(0,len(eq_days)):
	dt = eq_days[i] - fm_days
	dtabs = numpy.absolute(dt)
	a1 = numpy.where(numpy.min(dtabs) == dtabs)[0]
	closestFM[i] = dt[a1]

plt.plot(eq_mag,closestFM,'.')
plt.xlabel('Earthquake Magnitude')
plt.ylabel('Days to Closest Full Moon')
plt.savefig('FM_EQ.png')		

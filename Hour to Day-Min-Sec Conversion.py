print('Enter the number of hours that you want to convert to days, minutes and seconds : ')

hours = float(input())

seconds = round((float(hours) * 60 * 60), 6)

minutes = round((float(hours) * 60), 6)

days = round((float(hours) / 24), 6)

print('Okay, so that is '+str(days)+' day(s), '+str(minutes)+' minutes and '+str(seconds)+' seconds!')

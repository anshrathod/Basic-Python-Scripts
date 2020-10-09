# Python program to find angle between hour and minute hands

# Function to Calculate angle b/w hour hand and minute hand
def calcAngle(h, m):
    # validate the input
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print('Wrong input')

    if (h == 12):
        h = 0
    if (m == 60):
        m = 0
        h += 1
        if(h > 12):
            h = h-12

    # Calculate the angles moved by
    # hour and minute hands with
    # reference to 12:00
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    # possible angles
    angle = min(360 - angle, angle)

    return angle


# Input
h = int(input('Enter hour:'))
m = int(input('Enter minute:'))
print('Angle ', calcAngle(h, m))

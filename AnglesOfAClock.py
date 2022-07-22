def calcAngle(h, m):
    # Calculate the hours degree
    hour_angle = (360 / (12 * 60.0)) * (h * 60 + m)
    # Calculate the minutes degree
    min_angle = 360 / 60.0 * m
    # Calculate the angle the hours degree and the minutes degree
    angle = abs(hour_angle - min_angle)
    # Return the min between angle and 360- angle
    return min(angle, 360 - angle)


print(calcAngle(3, 15))
# 7.50
print(calcAngle(3, 00))
# 90

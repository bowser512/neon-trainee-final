
def control(left_sensor, right_sensor, speed):

    P = 0.38
    erro = right_sensor - left_sensor
    return {
        'engineTorque': 800,
        'breakingTorque': 0,
        'steeringAngle': P * erro,
        'log': [
            {'name': 'Speed', 'value': speed, 'min': 0, 'max': 200},
            {'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1}
            {'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1}
        ]
    }

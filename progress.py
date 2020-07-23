def reward_function(params):
    SPEED_THRESHOLD = 1.0
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    completion=params["progress"]

    if not all_wheels_on_track:
        reward = -1
    else:
        reward = completion

    if speed < SPEED_THRESHOLD and all_wheels_on_track:
        reward *= 0.5  # Penalize if the car goes too slow

    return float(reward)

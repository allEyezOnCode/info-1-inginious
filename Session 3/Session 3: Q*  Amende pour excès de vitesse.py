def fine(authorized_speed, actual_speed):
    limit = actual_speed - authorized_speed
    fine = 0
    if limit > 0:
        fine = limit * 5
        if limit >= 10:
            fine *= 2
    return fine if fine == 0 or fine >= 12.5 else 12.5

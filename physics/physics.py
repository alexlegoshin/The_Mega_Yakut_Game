G = 0.5  # gravity acceleration per frame
K = 0.05  # x_resistance acceleration per frame


def gravity(vy, on_platform):
    """Add a gravity effect if the object is not on the platform"""
    if not on_platform:
        vy += G
    else:
        vy = 0
    return vy


def x_resistance(vx):
    """Stopping player while flying on x. Needed for death animation."""
    if vx > 0:
        vx -= K
    elif vx != 0:
        vx += K
    return vx

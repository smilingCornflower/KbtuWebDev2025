def make_bricks(small, big, goal):
    max_big = min(goal // 5, big)
    return (goal - max_big * 5) <= small


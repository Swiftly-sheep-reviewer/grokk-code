"""
Fundamental concepts

1. Determine if there’s an overlap between two intervals:
First let’s think in the opposite direction, how would the intervals look like
if they do NOT overlap?

x1  x2
|---|
        |----|
        y1  y2

y1  y2
|---|
        |----|
        x1  x2

i.e. x2 < y1 or y2 < x1
So the overlapping condition is the opposite
Not (x2 < y1 or y2 < x1)

2. Finding the overlap
The key formula here is the overlap of two interval is given by
[max(x1, y1), min(x2, y2)].

"""
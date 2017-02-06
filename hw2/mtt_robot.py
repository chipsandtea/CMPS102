# Christopher Hsiao
# 2/6/2017
# 
# Problem: Box Picking
# You are a box picker at SoftPillwos and your job is to pick the boxes for the pillows your company is shipping out.
# The fit is rarely perfect, but if the box is too big you can stuff it with bubblewrap, and if the box is too small, youc ompress the pillow. 
# Specifically, if box b_j has length m_j and pillow a_j has length l_i, then if you ship a pillow a_i, in n pillows each day your job is to pick a box for each pillow, such that total cost is minimized.
# 
# MTT ALGORITHM: Find some pair (b_j , a_i) for which their corresponding |m_j - l_i| is a minimum, assigning a_i to b_j, and repeating, until all pillows have been assigned.
# 
# Q: Is the algorithm described for the MTT BP3k optimal, or can you find a counter example?
# 
# Bonus: What if the cost instead of |m_j - l_i| was (m_j - l_i)^2? Wouuld your algorithm still work? If not, could yo modify it so that it did.

# boxes/pillows = (int val, bool paired)
# calculate all minimum pairings 
def mtt_picker(boxes, pillows):
	pairings = {}

	for i in range(len(pillows)):
		min = float("inf")
		curr_pair = (0,0)
		for j in range(len(boxes)):
			cost = abs(pillows[i][0] - boxes[j][0])
			if cost < min:
				curr_pair = (i, j, cost)
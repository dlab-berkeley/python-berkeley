# the following line is highlighted because it's an unused import
import numpy as np

# this next line is highlighted because `n` doesn't exist (fixing this
# line would actually also fix the previous line)
arr = n.ones(10)

# this line is highlighted because it's really long, and long lines in python are bad if you're working in a fixed-width terminal


def foo():
        # the next line is highlighted because it uses tabs, eww
	pass

# Classic poker game. Human vs Human or Human vs AI. No bids just shuffling cards, 
# exchange turn and finally - result. Showing not only the winner but also his "hand" with description
# this is the main game file.

a = "A \u2664"
b = "K \u2661"
c = "D \u2662"
d = "J \u2667"
e = "10\u2664"

print(f"""\n|  \033[1m1\033[0m  |  \033[1m2\033[0m  |  \033[1m3\033[0m  |  \033[1m4\033[0m  |  \033[1m5\033[0m  |
-------------------------------
| {a} | {b} | {c} | {d} | {e} |\n""")
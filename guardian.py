import random

# Stalker
# Normal - x10-12
#   35.0% - Ancient Screw
#   26.0% - Ancient Spring
#   21.0% - Ancient Gear
#   15.0% - Ancient Shaft
#    2.5% - Ancient Core
#    0.5% - Giant Ancient Core

# Skywatcher
# Normal - x8-12
#   35.0% - Ancient Gear
#   24.0% - Ancient Screw
#   23.0% - Ancient Shaft
#   15.0% - Ancient Spring
#    2.5% - Ancient Core
#    0.5% - Giant Ancient Core

NUM_TRIALS = 1000000
MAX_NUM_STALKERS = 5

items = ["Screw", "Spring", "Gear", "Shaft", "Core", "Giant Core"]
#stalker weights = [0.35, 0.26, 0.21, 0.15, 0.025, 0.05]
weights = [0.24, 0.15, 0.35, 0.23, 0.025, 0.05]

def dropsFromOneStalker():
	num_drops = random.randint(10,12)
	drops = random.choices(items, weights = weights, k = num_drops)
	return drops

counts = {}
for i in items:
	counts[i] = 0

print("n\tp")
for n in range(1,MAX_NUM_STALKERS+1):
	fail_count = 0
	for i in range(NUM_TRIALS):
		drops = []
		for j in range(n):
			drops = drops + dropsFromOneStalker()
		# print(drops),
		if ("Spring" not in drops or "Shaft" not in drops):
			# print("Fail")
			fail_count += 1
		else:
			# print("Ok")
			pass

	print(str(n) + "\t" + str(1.0*fail_count/NUM_TRIALS))
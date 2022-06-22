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
MAX_NUM_STALKERS = 2

items = ["Screw", "Spring", "Gear", "Shaft", "Core", "Giant Core"]
weights_stalker = [0.35, 0.26, 0.21, 0.15, 0.025, 0.05]
weights_skywatcher = [0.24, 0.15, 0.35, 0.23, 0.025, 0.05]

def dropsFromOneStalker(w):
	num_drops = random.randint(10,12)
	drops = random.choices(items, weights = w, k = num_drops)
	return drops

counts = {}
for i in items:
	counts[i] = 0

print("n\tp")
for n in range(2,MAX_NUM_STALKERS+1):
	fail_count = 0
	for i in range(NUM_TRIALS):
		# drops = []
		# for j in range(n):
		# 	drops = drops + dropsFromOneStalker()
		drops = dropsFromOneStalker(weights_stalker) + dropsFromOneStalker(weights_stalker) + dropsFromOneStalker(weights_skywatcher)
		spring_count = 0
		shaft_count = 0
		for item in drops:
			if item == "Spring":
				spring_count += 1
			elif item == "Shaft":
				shaft_count += 1

		if spring_count <= 1 or shaft_count <= 1:
			fail_count += 1

	print(str(n) + "\t" + str(1.0*fail_count/NUM_TRIALS))
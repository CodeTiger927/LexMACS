import math

points = [];
N = 1000;

def dist(a,b):
	return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2) + (a[2] - b[2])**2;

f = open("points.txt", "r")
for i in range(N):
	line = f.readline().rstrip().split(" ");
	points.append([float(line[0]),float(line[1]),float(line[2])]);

print("Please enter your order and separate them by a space (like 5 2 4 1 3, you don't have to include the last one as it should be the first)")
inputs = input().split(" ");
order = [];
for x in inputs:
	if(int(x) not in order):
		order.append(int(x));

if(len(order) != len(inputs)):
	print("You have duplicate numbers!");
	exit();

if(len(order) != N):
	print("You are either missing numbers or have too many numbers");
	exit();

totalDistance = 0;
for i in range(N):
	if(order[i] < 1 or order[i] > N or order[(i + 1) % N] < 1 or order[(i + 1) % N] > N):
		print("One of your numbers is out of range from 1 to " + str(N))
		exit();
	totalDistance += dist(points[order[i] - 1],points[order[(i + 1) % N] - 1]);

print(totalDistance);
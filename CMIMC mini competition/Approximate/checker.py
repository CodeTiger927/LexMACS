import math

def target(x):
	return (3/4) * math.exp(0.22 * x) - 8 * math.sqrt(3 * abs(x)) + 14 * math.sin(3 * x / 4 - 2) - abs(x - 43.2) / 3 + 40;

def Y(a,b,c,d,e,f,x):
	return a * (x**2.2) + b * math.cos(2 * x + c) + d / (1 + math.exp(-x)) + math.log(abs(x) + 0.1,abs(e) + 1.1) + f;

while(1) :
	print("Input the six parameters with spaces between them (for example 1 2 3 4 5 6):")
	str = input().split(" ");
	tot = 0;
	for i in range(-20,21):
		tot += abs(target(i) - Y(float(str[0]),float(str[1]),float(str[2]),float(str[3]),float(str[4]),float(str[5]),i));

	print("Your total difference is");
	print(tot);
	print("");
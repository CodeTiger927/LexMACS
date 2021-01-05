import random;

sizeX = 50;
sizeY = 50;
numO = 100;
grid = [[0 for i in range(sizeX)] for j in range(sizeY)]

bot1X = 0
bot1Y = 0
bot2X = sizeX - 1
bot2Y = sizeY - 1

dx = [0,1,0,-1,0]
dy = [1,0,-1,0,0]

frameSpeed = 10;
totalTime = 60 * frameSpeed * 3; 

def finalCounter():
    counterA = 0;
    counterB = 0;
    for i in range(sizeX):
        for j in range(sizeY):
            if(grid[i][j] == 1): counterA += 1;
            if(grid[i][j] == 2): counterB += 1;
            
    print("Player A in total has " + str(counterA) + " points and Player B in total has " + str(counterB) + "points.");
    if(counterA > counterB):
        print("Congratulation to Player A!");
    if(counterA < counterB):
        print("Congratulation to Player B!");
    if(counterA == counterB):
        print("Oh wow, a TIE!");

def generateObstacles():
    for i in range(numO):
        ranX = random.randrange(0,sizeX)
        ranY = random.randrange(0,sizeY)
        # print(ranX,ranY);
        if((ranX == 0 and ranY == 0) or (ranX == sizeX - 1 and ranY == sizeY - 1)): continue
        grid[ranX][ranY] = -1;

def setup():
    frameRate(frameSpeed);
    size(1600,1600)
    generateObstacles();
    grid[0][0] = 1;
    grid[sizeX - 1][sizeY - 1] = 2;

def draw():
    global bot1X,bot1Y,bot2X,bot2Y;
    background(255);
    for i in range(sizeX):
        for j in range (sizeY):
            fill(255);
            if(grid[i][j] == -1):
                fill(0);
            if(grid[i][j] == 1):
                fill(255,0,0);
            if(grid[i][j] == 2):
                fill(0,0,255);
            if(i == bot1X and j == bot1Y):
                fill(255,150,150);
            if(i == bot2X and j == bot2Y):
                fill(150,150,250);
            rect(30 * i + 50 ,30 * j + 50,30,30);
            
    moveA = playerA(bot1X,bot1Y,bot2X,bot2Y,grid);
    nb1x = bot1X + dx[moveA];
    nb1y = bot1Y + dy[moveA];
    if(nb1x < sizeX and nb1x >= 0 and nb1y < sizeY and nb1y >= 0 and (grid[nb1x][nb1y] == 0 or grid[nb1x][nb1y] == 1)):
        bot1X = nb1x;
        bot1Y = nb1y;
        grid[bot1X][bot1Y] = 1;
        
        
    moveB = playerB(bot2X,bot2Y,bot1X,bot1Y,grid);
    nb2x = bot2X + dx[moveB];
    nb2y = bot2Y + dy[moveB];
    if(nb2x < sizeX and nb2x >= 0 and nb2y < sizeY and nb2y >= 0 and (grid[nb2x][nb2y] == 0 or grid[nb2x][nb2y] == 2)):
        bot2X = nb2x;
        bot2Y = nb2y;
        grid[bot2X][bot2Y] = 2;
        
    if(frameCount % (10 * frameSpeed) == 0):
        print(str((totalTime - frameCount) / (frameSpeed)) + " seconds left");
    if(frameCount == 480):
        finalCounter();
        noLoop();
    
# 0 - down, 1 - right, 2 - up, 3 - left, 4 - nothing
def playerA(b1x,b1y,b2x,b2y,g):
    if(b1y + 1 == 50): return 1;
    if(g[b1x][b1y + 1] != 0): return 1;
    return 0;
            
            
# 0 - down, 1 - right, 2 - up, 3 - left, 4 - nothing
def playerB(b1x,b1y,b2x,b2y,g):
    if(b1y == 0): return 3;
    if(g[b1x][b1y - 1] != 0): return 3;
    return 2;
            
            
            
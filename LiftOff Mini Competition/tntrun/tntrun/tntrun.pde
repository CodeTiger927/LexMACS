int sizeX = 12;
int sizeY = 12;
int cellX = 1;
int cellY = 1;

int bot1X = 0;
int bot1Y = 0;
int bot2X = sizeX - 1;
int bot2Y = sizeY - 1;

int[] dx = new int[]{1,0,-1,0};
int[] dy = new int[]{0,1,0,-1};

int[][] grid = new int[sizeX][sizeY];

void setup() {
  size(1200,1200);
  cellX = height / sizeX;
  cellY = width / sizeY;
  
  for(int i = 0;i < sizeX;++i) {
    for(int j = 0;j < sizeY;++j) {
      if(Math.random() < 0.05) {
        grid[i][j] = -1;
      }
    }
  }
  
  frameRate(5);
}

void draw() {
  background(255);
  for(int i = 0;i < sizeX;++i) {
    for(int j = 0;j < sizeY;++j) {
      if(grid[i][j] == 0) {
        fill(255);
      }else if(grid[i][j] == 1) {
        fill(255,150,150);
      }else if(grid[i][j] == 2){
        fill(150,150,250);
      }else{
        fill(80);
      }
      rect(i * cellX,j * cellY,cellX,cellY);
    }
  }
  fill(255,0,0);
  rect(bot1X * cellX,bot1Y * cellY,cellX,cellY);
  fill(0,0,255);
  rect(bot2X * cellX,bot2Y * cellY,cellX,cellY);
  if(Math.random() > 0.5) {
    int playerADecision = playerA(bot1X,bot1Y,bot2X,bot2Y,grid);
    if(!moveA(playerADecision)) {
      System.out.println("B wins!");
      noLoop();
    }
    int playerBDecision = playerB(bot2X,bot2Y,bot1X,bot1Y,grid);
    if(!moveB(playerBDecision)) {
      System.out.println("A wins!");
      noLoop();
    }
  }else{
    int playerBDecision = playerB(bot2X,bot2Y,bot1X,bot1Y,grid);
    if(!moveB(playerBDecision)) {
      System.out.println("A wins!");
      noLoop();
    }
    int playerADecision = playerA(bot1X,bot1Y,bot2X,bot2Y,grid);
    if(!moveA(playerADecision)) {
      System.out.println("B wins!");
      noLoop();
    }
  }
}

int playerA(int selfX,int selfY,int otherX,int otherY,int[][] grid) {
  int d = (int)(Math.random() * 4) % 4;
  int nx = selfX + dx[d];
  int ny = selfY + dy[d];
  int counter = 20;
  while(nx < 0 || nx >= sizeX || ny < 0 || ny >= sizeY || grid[nx][ny] == -1 && counter-- > 0) {
    d = (int)(Math.random() * 4) % 4;
    nx = selfX + dx[d];
    ny = selfY + dy[d];
  }
  return d;
}

int playerB(int selfX,int selfY,int otherX,int otherY,int[][] grid) {
  int d = (int)(Math.random() * 4) % 4;
  int nx = selfX + dx[d];
  int ny = selfY + dy[d];
  int counter = 20;
  while(nx < 0 || nx >= sizeX || ny < 0 || ny >= sizeY || grid[nx][ny] == -1 && counter-- > 0) {
    d = (int)(Math.random() * 4) % 4;
    nx = selfX + dx[d];
    ny = selfY + dy[d];
  }
  return d;
}

boolean moveA(int d) {
  int nx = bot1X + dx[d];
  int ny = bot1Y + dy[d];
  if(nx < 0 || nx >= sizeX || ny < 0 || ny >= sizeY || grid[nx][ny] == -1) return false;
  grid[bot1X = nx][bot1Y = ny] = -1;
  return true;
}

boolean moveB(int d) {
  int nx = bot2X + dx[d];
  int ny = bot2Y + dy[d];
  if(nx < 0 || nx >= sizeX || ny < 0 || ny >= sizeY || grid[nx][ny] == -1) return false;
  grid[bot2X = nx][bot2Y = ny] = -1;
  return true;
}

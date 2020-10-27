//var bird;
var bot;
var bots = [];
var bullets = [];

function setup() {
	createCanvas(900,500);
	bot = new Bot(100,100)
	bots.push(bot);
}

function draw() {
	background(51);
	for(var i = 0;i < bots.length;++i) {
		if(!bots[i].boolS) {
			bots[i].show();
			bots[i].check();
			bots[i].think();
		}else{
			noLoop();
			console.log("You win!");
		}
	}
	for(var i = 0;i < bullets.length;++i) {
		bullets[i].show();
		bullets[i].move();
	}

	if(keyIsDown(39)) {
		bot.rotateRight();
	}else if(keyIsDown(37)) {
		bot.rotateLeft();
	}else if(keyIsDown(38)) {
		bot.move();
	}else if(keyIsDown(32)) {
		bot.shoot();
	}
}

function Bullet(x,y,ang) {
	this.x = x;
	this.y = y;
	this.ang = ang;
}

Bullet.prototype.show = function() {
	fill(255,50,100);
	ellipse(this.x,this.y,10,10);
}

Bullet.prototype.move = function() {
	this.x += 8 * Math.sin(this.ang);
	this.y += 8 * Math.cos(this.ang);
}

Bullet.prototype.check = function(x,y) {
	if(Math.sqrt((this.x - x) * (this.x - x) + (this.y - y) * (this.y - y)) <= 25) {
		return true;
	}
}

function Bot(x,y) {
	this.x = x;
	this.y = y;
	this.ang = 0;
	this.lastAttack = frameCount;
}


Bot.prototype.think = function() {

}

Bot.prototype.rotateLeft = function() {
	this.ang += 0.1;
	if(this.ang > 2 * PI) this.ang -= 2 * PI;
}

Bot.prototype.rotateRight = function() {
	this.ang -= 0.1;
	if(this.ang < 0) this.ang += 2 * PI;
}

Bot.prototype.move = function() {
	this.x += 4 * Math.sin(this.ang);
	this.y += 4 * Math.cos(this.ang);
}

Bot.prototype.check = function() {
	for(var i = 0;i < bullets.length;++i) {
		if(bullets[i].check(this.x,this.y)) {
			console.log("you're dead");
			noLoop();
		}
	}
}

Bot.prototype.shoot = function() {
	if(frameCount - this.lastAttack <= 100) return;
	this.lastAttack = frameCount;
	bullets.push(new Bullet(this.x + 30 * Math.sin(this.ang),this.y + 30 * Math.cos(this.ang),this.ang));
}

Bot.prototype.show = function() {
	ellipseMode(CENTER);
	noStroke();
	fill(255,128,0);
	ellipse(this.x,this.y,40,40);
	fill(0);
	ellipse(this.x + 10 * Math.sin(this.ang),this.y + 10 * Math.cos(this.ang),10,10);
}



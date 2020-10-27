//var bird;
var obstacles = [];
var birds = [];
var pos = 500;
var bird;


function setup() {
	createCanvas(900,500);
	bird =  new Bird(0.15,2)
	birds.push(bird);
	for(var i = 0;i < 20;i++) {
		var tmp1 = Math.random() * 250;
		var tmp2 = Math.random() * 50 + 200;
		obstacles.push(new obstacle(tmp1,height - tmp1 - tmp2, 0 - i * 200));
	}

}

function draw() {
		pos -= 3.5;
		background(64,224,208);
		for(var i = 0;i < birds.length;i++) {
			if(!birds[i].boolS) {
				birds[i].show();
				birds[i].fall();
				birds[i].check();	
				birds[i].think();
			}else{
				noLoop();
				console.log("You're dead");
			}
		}
		for(var i = 0;i < obstacles.length;i++) {
			obstacles[i].show();
		}

}

function obstacle(s,e,p) {
	this.s = s;
	this.e = e;
	this.p = p;
}

obstacle.prototype.show = function() {
	noStroke();
	fill(255);
	rect(pos - this.p,0,50,this.s);
	rect(pos - this.p,height - this.e,50,this.e);
}

obstacle.prototype.highLight = function() {
	noStroke();
	fill(255,0,0);
	rect(pos - this.p,0,50,this.s);
	rect(pos - this.p,height - this.e,50,this.e);
}

function Bird(d,u) {
	this.dv = d;
	this.uv = u;
	this.v = 0;
	this.h = height / 2;
}


Bird.prototype.think = function() {

}

Bird.prototype.check = function() {
	if(this.h < 0) {
		this.v = 0;
		this.h = 0;
	}else if(this.h > height) {
		this.v = 0;
		this.h = height;
	}
	if(this.where() == 0) {
		var a = obstacles[this.getN()].s;
		var b = height - obstacles[this.getN()].e;
		if(this.h < a || this.h > b) {
			this.boolS = 1;
		}
	}
}

Bird.prototype.fall = function() {
	this.v -= this.dv;
	this.h -= this.v;
}

Bird.prototype.up = function() {
	this.v += this.uv;
	this.h -= this.v;
}

Bird.prototype.show = function() {
	noStroke();
	fill(255,128,0);
	ellipse(150,this.h,20,20);
}

Bird.prototype.getN = function() {
	var n = Math.max(Math.floor((pos - 300) / -200),0);
	return n;
}

Bird.prototype.where = function() {
	var p = obstacles[this.getN()].p;
	var t = pos - 112;	
	if (p - 40 <= t && p + 50>= t) {
		return 0;
	}else{
		return -1;
	}
}

function keyPressed() {
	if(keyCode === 32) {
		bird.up();
	}
}
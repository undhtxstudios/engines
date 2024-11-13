"use strict";

let levelSize, ball, score, paddle;

const sound_brick_collide = new Sound([
  1.2,
  ,
  126,
  ,
  0.03,
  0.02,
  1,
  ,
  ,
  ,
  ,
  ,
  ,
  ,
  4.5,
  ,
  ,
  0.91,
  0.03,
  0.02,
  121,
]);
const sound_bounce = new Sound(
  [, , 1e3, , 0.03, 0.02, 1, 2, , , 940, 0.03, , , , , 0.2, 0.6, , 0.06],
  0
);
const sound_start = new Sound([
  ,
  0,
  500,
  ,
  0.04,
  0.3,
  1,
  2,
  ,
  ,
  570,
  0.02,
  0.02,
  ,
  ,
  ,
  0.04,
]);

function gameInit() {
  canvasFixedSize = vec2(1280, 720);
  levelSize = vec2(38, 20);
  cameraPos = levelSize.scale(0.5);
  score = 0;

  setCameraPos(cameraPos);
  setCanvasFixedSize(canvasFixedSize);

  for (let x = 2; x <= levelSize.x - 2; x += 2)
    for (let y = 12; y <= levelSize.y - 2; y += 1) {
      const brick = new Brick(vec2(x, y), vec2(2, 1));
      brick.color = randColor();
    }

  paddle = new Paddle();

  // create walls
  new Wall(vec2(-0.5, levelSize.y / 2), vec2(1, 100)); // left
  new Wall(vec2(levelSize.x + 0.5, levelSize.y / 2), vec2(1, 100)); // right
  new Wall(vec2(levelSize.x / 2, levelSize.y + 0.5), vec2(100, 1)); // top
}

function gameUpdate() {
  // if there is no ball or ball is below level
  if (ball && ball.pos.y < -1) {
    ball.destroy();
    ball = new Ball(cameraPos);
  }

  if (!ball && mouseWasPressed(0)) {
    // if there is no ball and left mouse is pressed
    ball = new Ball(cameraPos); // create the ball
    sound_start.play(); // play start sound
  }
}

function gameUpdatePost() {}

function gameRender() {
  drawRect(cameraPos, levelSize, new Color(0.1, 0.1, 0.1)); // draw level boundary
}

function gameRenderPost() {
  drawTextScreen("Score " + score, vec2(mainCanvasSize.x / 2, 70), 50); // show score
}

// Startup LittleJS Engine
engineInit(gameInit, gameUpdate, gameUpdatePost, gameRender, gameRenderPost);

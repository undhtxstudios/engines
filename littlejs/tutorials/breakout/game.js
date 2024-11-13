"use strict";

let levelSize, ball, paddle, score, brickCount;

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
const sound_break = new Sound([
  ,
  ,
  90,
  ,
  0.01,
  0.03,
  4,
  ,
  ,
  ,
  ,
  ,
  ,
  9,
  50,
  0.2,
  ,
  0.2,
  0.01,
]);
const sound_bounce = new Sound([
  ,
  ,
  1e3,
  ,
  0.03,
  0.02,
  1,
  2,
  ,
  ,
  940,
  0.03,
  ,
  ,
  ,
  ,
  0.2,
  0.6,
  ,
  0.06,
]);

function gameInit() {
  canvasFixedSize = vec2(1280, 720);
  levelSize = vec2(38, 20);
  cameraPos = levelSize.scale(0.5);
  paddle = new Paddle(vec2(levelSize.x / 2 - 12, 1));
  score = brickCount = 0;

  const pos = vec2();
  for (pos.x = 4; pos.x <= levelSize.x - 4; pos.x += 2)
    for (pos.y = 12; pos.y <= levelSize.y - 2; pos.y += 1) new Brick(pos);

  new Wall(vec2(-0.5, levelSize.y / 2), vec2(1, 100));
  new Wall(vec2(levelSize.x + 0.5, levelSize.y / 2), vec2(1, 100));
  new Wall(vec2(levelSize.x / 2, levelSize.y + 0.5), vec2(100, 1));
}

function gameUpdate() {
  // spawn ball
  if (!ball && (mouseWasPressed(0) || gamepadWasPressed(0))) {
    ball = new Ball(vec2(levelSize.x / 2, levelSize.y / 2));
    sound_start.play();
  }
}

function gameUpdatePost() {}

function gameRender() {
  drawRect(cameraPos, levelSize, hsl(0, 0, 0.02));
}

function gameRenderPost() {
  // use built in image font for text
  const font = new FontImage();
  font.drawText("Score: " + score, cameraPos.add(vec2(0, 9.6)), 0.15, true);
  if (!brickCount)
    font.drawText("You Win!", cameraPos.add(vec2(0, -5)), 0.2, true);
  else if (!ball)
    font.drawText("Click to Play", cameraPos.add(vec2(0, -5)), 0.2, true);
}

engineInit(gameInit, gameUpdate, gameUpdatePost, gameRender, gameRenderPost);

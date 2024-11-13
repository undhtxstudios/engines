class Paddle extends EngineObject {
  constructor() {
    super(vec2(0, 1), vec2(6, 0.5));
    this.setCollision();
    this.mass = 0;
  }
  update() {
    // clamp paddle to level size
    this.pos.x = clamp(
      mousePos.x,
      this.size.x / 2,
      levelSize.x - this.size.x / 2
    );
  }
}

class Ball extends EngineObject {
  constructor(pos) {
    super(pos, vec2(0.5)); // set object position

    this.velocity = vec2(-0.1, -0.1); // give ball some movement
    this.setCollision();
    this.elasticity = 1;
  }
  collideWithObject(o) {
    // prevent colliding with paddle if moving upwards
    if (o == paddle && this.velocity.y > 0)
        return 0;

    // speed up
    const speed = min(1.04*this.velocity.length(), .5);
    this.velocity = this.velocity.normalize(speed);

    // scale bounce sound pitch by speed
    sound_bounce.play(this.pos, 1, speed*2);

    if (o == paddle)
    {
        // put english on the ball when it collides with paddle
        this.velocity = this.velocity.rotate(.2 * (this.pos.x - o.pos.x));
        this.velocity.y = max(-this.velocity.y, .2);
        return 0;
    }
    
    // prevent default collision with paddle
    return 1;
  }
}

class Wall extends EngineObject {
  constructor(pos, size) {
    super(pos, size); // set object position and size
    this.color = new Color(0, 0, 0);
    this.setCollision(); // make object collide
    this.mass = 0; // make object have static physics
  }
}

class Brick extends EngineObject {
  constructor(pos, size) {
    super(pos, size);

    this.setCollision(); // make object collide
    this.mass = 0; // make object have static physics
  }

  collideWithObject(o) {
    ++score;
    sound_brick_collide.play(this.pos);

    // create explosion effect
    const color = this.color;
    new ParticleEmitter(
      this.pos,
      0, // pos, angle
      this.size,
      0.1,
      200,
      PI, // emitSize, emitTime, emitRate, emiteCone
      0, // tileInfo
      color,
      color, // colorStartA, colorStartB
      color.scale(1, 0),
      color.scale(1, 0), // colorEndA, colorEndB
      0.2,
      0.5,
      1,
      0.1,
      0.1, // time, sizeStart, sizeEnd, speed, angleSpeed
      0.99,
      0.95,
      0.4,
      PI, // damping, angleDamping, gravityScale, cone
      0.1,
      0.5,
      0,
      1 // fadeRate, randomness, collide, additive
    );

    this.destroy(); // destroy block when hit
    return 1;
  }
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    for (let value of fans) {
        value.vx = 0 - value.vx
        value.vy = 0 - value.vy
    }
    if (Math.percentChance(33)) {
        music.playMelody("A F E F - - - - ", 200)
    } else {
        if (Math.percentChance(50)) {
            music.playMelody("G B A G - - - - ", 200)
        } else {
            music.playMelody("G E C5 C - - - - ", 200)
        }
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite5, otherSprite) {
    otherSprite.destroy(effects.confetti, 100)
    mySprite.sayText(":)", 500, false)
    info.changeScoreBy(3)
    music.baDing.play()
})
scene.onHitWall(SpriteKind.Enemy, function (sprite, location) {
    if (Math.percentChance(50)) {
        sprite.vx = randint(10, 20)
    } else {
        sprite.vx = randint(-10, -20)
    }
    if (Math.percentChance(50)) {
        sprite.vy = randint(10, 20)
    } else {
        sprite.vy = randint(-10, -20)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`exit`, function (sprite6, location5) {
    game.over(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite7, otherSprite2) {
    tiles.placeOnRandomTile(otherSprite2, assets.tile`transparency16`)
    mySprite.sayText(":(", 500, false)
    music.zapped.play()
    info.changeScoreBy(-1)
})
let instruments: Sprite[] = []
let fans: Sprite[] = []
let mySprite: Sprite = null
scene.setBackgroundColor(13)
tiles.setTilemap(tilemap`level3`)
mySprite = sprites.create(assets.image`rockstar`, SpriteKind.Player)
controller.moveSprite(mySprite)
tiles.placeOnRandomTile(mySprite, assets.tile`stage`)
scene.cameraFollowSprite(mySprite)
fans.push(sprites.create(assets.tile`fan1`, SpriteKind.Enemy))
fans.push(sprites.create(assets.tile`fan2`, SpriteKind.Enemy))
fans.push(sprites.create(assets.tile`fan3`, SpriteKind.Enemy))
for (let value of fans) {
    tiles.placeOnRandomTile(value, assets.tile`transparency16`)
    value.vx = randint(-20, 20)
}
instruments.push(sprites.create(assets.image`i1`, SpriteKind.Food))
instruments.push(sprites.create(assets.image`i2`, SpriteKind.Food))
instruments.push(sprites.create(assets.image`i3`, SpriteKind.Food))
instruments.push(sprites.create(assets.image`i4`, SpriteKind.Food))
for (let value of instruments) {
    tiles.placeOnRandomTile(value, assets.tile`transparency16`)
}
info.startCountdown(200)

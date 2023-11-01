controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . 2 2 . . . . . . . . . . 
        . . . . 2 2 . . . . . . . . . . 
        . . . . 2 2 2 2 2 2 2 2 2 . . . 
        . . . . 2 5 4 5 2 2 2 4 5 2 . . 
        . . . . 2 5 4 5 2 2 2 4 5 2 . . 
        . . . . 2 2 2 2 2 2 2 2 2 . . . 
        . . . . 2 2 . . . . . . . . . . 
        . . . . 2 2 . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, mySprite, 25000, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy()
    info.changeScoreBy(2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy(effects.disintegrate, 500)
    scene.cameraShake(4, 500)
})
let Enemyplane: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
effects.starField.startScreenEffect()
mySprite = sprites.create(img`
    . . . . . . . . . . 5 5 5 5 . . 
    . . . . . . 8 8 8 8 5 5 5 5 . . 
    . . . . . 8 8 8 8 8 5 5 5 5 . . 
    . . . . . 8 8 . . . 5 5 5 5 . . 
    . . 4 4 6 6 6 6 2 . . . 4 4 . . 
    . 4 4 4 6 6 6 6 2 2 . 4 4 4 . . 
    . . 4 4 . . . 6 2 2 2 4 4 4 5 5 
    . . . . . . . 6 2 2 2 4 4 4 5 5 
    . . 4 4 6 6 6 6 2 2 . 4 4 4 . . 
    . 4 4 4 6 6 6 6 2 . . . 4 4 . . 
    . . 4 4 . 8 8 . . . . . . . . . 
    . . . . . 8 8 . . . . 5 5 5 . . 
    . . . . . . 8 8 8 8 5 5 5 5 . . 
    . . . . . . 8 8 8 8 5 5 5 5 . . 
    . . . . . . . . . . . 5 5 5 . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
info.setLife(5)
game.onUpdateInterval(5000, function () {
    Enemyplane = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . 4 4 4 4 4 4 4 4 4 4 4 . 
        . . . . 9 9 9 9 9 9 9 9 9 9 9 . 
        . . . . 9 9 9 4 9 4 9 4 9 9 9 . 
        . . . 4 9 9 9 9 9 9 9 9 9 9 9 . 
        . . 2 4 9 9 9 4 9 4 9 4 9 9 9 . 
        . 2 4 4 9 9 9 9 9 9 9 9 9 9 9 . 
        . . 2 4 9 9 9 4 9 4 9 4 9 9 9 . 
        . . . 4 9 9 9 9 9 9 9 9 9 9 9 . 
        . . . 4 9 9 9 4 9 4 9 4 9 9 9 . 
        . . . . 9 9 9 9 9 9 9 9 9 9 9 . 
        . . . . 4 4 4 4 4 4 4 4 4 4 4 . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Enemy)
    Enemyplane.x = scene.screenWidth()
    Enemyplane.vx = -20
    Enemyplane.y = randint(10, scene.screenHeight() - 10)
})
game.onUpdateInterval(1237, function () {
    Enemyplane = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . 2 2 . . . . 
        . . . . . . . . . 2 2 2 . . . . 
        . . . . . . . . 2 2 2 2 . . . . 
        . . . . . . . 2 2 9 2 2 2 . . . 
        . . 3 3 . . . 2 9 9 2 2 2 7 7 7 
        . . . 3 3 2 2 9 9 3 2 2 2 . . . 
        . 2 3 2 2 2 2 9 3 3 2 2 2 . . . 
        . . . 3 3 2 2 9 9 3 2 2 2 . . . 
        . . 3 3 . . 2 2 9 9 2 2 2 7 7 7 
        . . . . . . . 2 2 9 2 2 2 . . . 
        . . . . . . . . 2 2 2 2 . . . . 
        . . . . . . . . . 2 2 2 . . . . 
        . . . . . . . . . . 2 2 . . . . 
        . . . . . . . . . . 2 2 . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Enemy)
    Enemyplane.x = scene.screenWidth()
    Enemyplane.vx = -20
    Enemyplane.y = randint(10, scene.screenHeight() - 10)
})

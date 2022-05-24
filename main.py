def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 5 . . . . . . . . . 
                    . . . . . . 5 . . . . . . . . . 
                    . . . . . . 5 . . 9 . . . . . . 
                    . . . . . . 5 9 9 9 5 . . . . . 
                    . . . . . . 5 5 5 9 5 5 9 . . . 
                    . . . . . . 5 9 9 9 5 . . . . . 
                    . . . . . . 5 . . 9 . . . . . . 
                    . . . . . . 5 . . . . . . . . . 
                    . . . . . . 5 . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        25000,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy()
    info.change_score_by(2)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    otherSprite2.destroy(effects.disintegrate, 500)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Enemyplane: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . 2 2 2 2 2 . . . . . . . . . 
            . . 2 5 5 5 2 2 . . . . . . . . 
            . . 2 5 5 5 5 2 2 2 2 . . . . . 
            4 4 2 5 5 5 5 5 5 5 2 2 . . . . 
            4 4 2 5 5 5 5 5 5 5 5 2 2 2 . . 
            4 4 2 5 5 5 5 5 5 5 5 5 5 2 2 . 
            . . 2 5 5 2 2 2 2 5 5 5 5 5 2 2 
            . . 2 5 5 5 2 5 2 5 5 5 5 5 2 2 
            . . 2 5 5 5 5 5 2 5 5 5 5 5 2 2 
            4 4 2 5 5 5 5 5 5 5 5 5 5 2 2 . 
            4 4 2 5 5 5 5 5 5 5 5 2 2 2 . . 
            4 4 2 5 5 5 5 5 5 5 2 2 . . . . 
            . . 2 5 5 5 2 2 2 2 2 . . . . . 
            . . 2 5 2 2 2 2 . . . . . . . . 
            . . 2 2 2 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
info.set_life(5)

def on_update_interval():
    global Enemyplane
    Enemyplane = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    Enemyplane.x = scene.screen_width()
    Enemyplane.vx = -20
    Enemyplane.y = randint(10, scene.screen_height() - 10)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global Enemyplane
    Enemyplane = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    Enemyplane.x = scene.screen_width()
    Enemyplane.vx = -20
    Enemyplane.y = randint(10, scene.screen_height() - 10)
game.on_update_interval(500, on_update_interval2)

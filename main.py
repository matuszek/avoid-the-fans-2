def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument4
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tile_at(location2, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument2
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    info.change_score_by(1)
    tiles.set_tile_at(location3, assets.tile("""
        transparency16
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument1
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    tiles.set_tile_at(location4, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument0
    """),
    on_overlap_tile4)

def on_on_overlap(sprite5, otherSprite):
    mySprite.say_text(":)", 100, True)
    info.change_score_by(3)
    otherSprite.destroy(effects.confetti, 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_overlap_tile5(sprite6, location5):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        exit
    """),
    on_overlap_tile5)

def on_on_overlap2(sprite7, otherSprite2):
    mySprite.say_text(":(")
    info.change_score_by(-1)
    tiles.place_on_random_tile(otherSprite2, assets.tile("""
        transparency16
    """))
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite: Sprite = None
scene.set_background_color(13)
tiles.set_tilemap(tilemap("""
    level3
"""))
mySprite = sprites.create(assets.image("""
    rockstar
"""), SpriteKind.player)
controller.move_sprite(mySprite)
tiles.place_on_random_tile(mySprite, assets.tile("""
    stage
"""))
scene.camera_follow_sprite(mySprite)
mySprite2 = sprites.create(assets.tile("""
    fan1
"""), SpriteKind.enemy)
mySprite3 = sprites.create(assets.tile("""
    fan2
"""), SpriteKind.enemy)
mySprite4 = sprites.create(assets.tile("""
    fan3
"""), SpriteKind.enemy)
tiles.place_on_random_tile(mySprite2, assets.tile("""
    transparency16
"""))
tiles.place_on_random_tile(mySprite3, assets.tile("""
    transparency16
"""))
tiles.place_on_random_tile(mySprite4, assets.tile("""
    transparency16
"""))
mySprite3.follow(mySprite)
info.start_countdown(30)

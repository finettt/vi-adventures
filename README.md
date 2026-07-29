# Vi Adventures

## Story
This game about two friends: `V` and `i`. Someone bad stole `i` and put it to the dark-dark room, and now you need to find your friend

## Controls

- `h, j, k, l` - movement
- `a` - attack
- `e` - interract
- `i` - list inventory
- `q` - quit game
- `n` - next page (in intro)

You can write a number before letter (e.g. 10h) and this action will be executed N times.

## Items

- `sword` - increases damage to 0.5
- `boots` - increase max step to 1
- `rose` - increases max hp to 1
- `long sword` - increases max enemies and max attach range to 1

## Environment variables
Each variable has VIADV_ prefix, so they won't conflict with your env.

Name | Impact | Type | Default
| --- | --- | --- | --- |
VIADV_SKIP_LORE | Skips default intro wtih guide and story | bool | False
VIADV_FORCE_LEVEL | Sets the base level for game, impacts on game flow, monster spawning | int | 0
VIADV_FORCE_STATE | Forces game state, only for debugging, used to view final animation | int | 2
VIADV_ZEN_MODE | Sets game to the infinite loop without room with `i` | bool |False


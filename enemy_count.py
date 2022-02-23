enemy_count = -25

def decrement():
    global enemy_count
    enemy_count-=1
    print(enemy_count)
    return enemy_count

def increment_enemies():
  global enemy_count
  enemy_count+=1

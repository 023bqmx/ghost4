import pygame
import random
import sys

# เริ่มต้น pygame
pygame.init()

# ขนาดหน้าจอ
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# สี
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)

# ความถี่ของ frame
FPS = 60
clock = pygame.time.Clock()

# ฟอนต์
FONT = pygame.font.SysFont("Arial", 32)

# ตัวแปรนก
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
gravity = 0.5
bird_velocity = 0
jump_strength = -10

# ท่อ
pipe_width = 70
pipe_gap = 150
pipe_velocity = 3
pipes = []

# คะแนน
score = 0

def create_pipe():
    y = random.randint(100, HEIGHT - 200)
    top_rect = pygame.Rect(WIDTH, 0, pipe_width, y)
    bottom_rect = pygame.Rect(WIDTH, y + pipe_gap, pipe_width, HEIGHT)
    return [top_rect, bottom_rect]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(SCREEN, GREEN, pipe[0])
        pygame.draw.rect(SCREEN, GREEN, pipe[1])

def check_collision(pipes, bird_rect):
    for pipe in pipes:
        if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]):
            return True
    return False

# สร้างท่อเริ่มต้น
pipes.append(create_pipe())

# วนลูปเกม
running = True
while running:
    clock.tick(FPS)
    SCREEN.fill(BLUE)

    # อีเวนต์กดปุ่ม
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = jump_strength

    # อัปเดตตำแหน่งนก
    bird_velocity += gravity
    bird_y += bird_velocity
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius*2, bird_radius*2)

    # วาดนก
    pygame.draw.circle(SCREEN, WHITE, (bird_x, int(bird_y)), bird_radius)

    # อัปเดตตำแหน่งท่อ
    for pipe in pipes:
        pipe[0].x -= pipe_velocity
        pipe[1].x -= pipe_velocity

    # ลบท่อที่ออกนอกจอ + เพิ่มใหม่
    if pipes[0][0].x < -pipe_width:
        pipes.pop(0)
        pipes.append(create_pipe())
        score += 1

    # วาดท่อ
    draw_pipes(pipes)

    # ตรวจสอบชน
    if check_collision(pipes, bird_rect) or bird_y > HEIGHT or bird_y < 0:
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    # วาดคะแนน
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

    # อัปเดตหน้าจอ
    pygame.display.update()
# ปิด pygame
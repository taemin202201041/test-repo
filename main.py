#gim Taemin
import pygame
import sys
import math
import random

# =============================
# 창 크기
# =============================
nX = 500
nY = 500

pygame.init()
pygame.display.set_caption("Computer Programming Class")
pygame.key.set_repeat(10, 10)

screen = pygame.display.set_mode((nX, nY))
FPSCLOCK = pygame.time.Clock()

# =============================
# 폰트 설정
# =============================
font_size = 32
font = pygame.font.Font(None, font_size)

def display_message(message, color, x, y):
    text = font.render(message, True, color)
    screen.blit(text, (x, y))

# =============================
# 메인 함수
# =============================
def main():

    delta = 5

    posX = nX // 2
    posY = nY // 2
    hero_radius = 20

    # 과일 초기 위치 (정수!)
    fruit_X = random.randint(nX // 10, nX * 9 // 10)
    fruit_Y = random.randint(nY // 10, nY * 9 // 10)

    fruit_max_size = 50
    fruit_radius = random.randint(5, fruit_max_size)

    count = 0

    while True:
        screen.fill((0, 0, 0))

        # =============================
        # 이벤트 처리
        # =============================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                    posX -= delta
                    posY -= delta
                elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                    posX += delta
                    posY -= delta
                elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                    posX -= delta
                    posY += delta
                elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                    posX += delta
                    posY += delta
                elif keys[pygame.K_LEFT]:
                    posX -= delta
                elif keys[pygame.K_RIGHT]:
                    posX += delta
                elif keys[pygame.K_UP]:
                    posY -= delta
                elif keys[pygame.K_DOWN]:
                    posY += delta

        # =============================
        # 충돌 판정
        # =============================
        val = (posX - fruit_X) ** 2 + (posY - fruit_Y) ** 2
        d = math.sqrt(val)

        if d <= (hero_radius + fruit_radius):
            gain_factor = fruit_radius / fruit_max_size
            hero_radius += 10 * gain_factor

            count += 1

            # 과일 재생성 (정수!)
            fruit_X = random.randint(nX // 10, nX * 9 // 10)
            fruit_Y = random.randint(nY // 10, nY * 9 // 10)
            fruit_radius = random.randint(5, fruit_max_size)

        # =============================
        # 렌더링
        # =============================
        display_message(f"score: {count}", (0, 255, 0), 50, 50)

        pygame.draw.circle(
            screen,
            (0, 0, 255),
            (int(posX), int(posY)),
            int(hero_radius)
        )

        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (int(fruit_X), int(fruit_Y)),
            int(fruit_radius)
        )

        pygame.display.update()
        FPSCLOCK.tick(100)

# =============================
# 실행
# =============================
if __name__ == '__main__':
    main()


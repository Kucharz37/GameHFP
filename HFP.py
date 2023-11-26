# Importujemy moduły pygame i random
import pygame
import random

# Inicjujemy pygame i tworzymy okno gry
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gra o kurczakach")

# Ładujemy obrazki kurczaka, strzelca i mięsa
chicken = pygame.image.load("chicken.png")
shooter = pygame.image.load("shooter.png")
meat = pygame.image.load("meat.png")

# Tworzymy listę kurczaków i mięs
chickens = []
meats = []

# Tworzymy zmienną przechowującą liczbę punktów
score = 0

# Tworzymy zmienną przechowującą liczbę zamówionych mięs
order = random.randint(5, 10)

# Tworzymy zmienną przechowującą stan gry
running = True

# Tworzymy pętlę główną gry
while running:
    # Wypełniamy tło kolorem białym
    screen.fill((255, 255, 255))

    # Rysujemy strzelca na środku dolnej krawędzi okna
    screen.blit(shooter, (400 - shooter.get_width() // 2, 600 - shooter.get_height()))

    # Sprawdzamy, czy naciśnięto klawisz
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # Jeśli naciśnięto spację, tworzymy nowy kurczak w losowym miejscu na górze okna
        chickens.append([random.randint(0, 800 - chicken.get_width()), 0])

    # Aktualizujemy położenie i rysujemy każdego kurczaka
    for c in chickens:
        # Przesuwamy kurczaka w dół o losową liczbę pikseli
        c[1] += random.randint(1, 5)
        # Rysujemy kurczaka na ekranie
        screen.blit(chicken, c)
        # Sprawdzamy, czy kurczak dotknął dolnej krawędzi okna
        if c[1] >= 600 - chicken.get_height():
            # Jeśli tak, usuwamy kurczaka z listy i odejmujemy punkt
            chickens.remove(c)
            score -= 1

    # Aktualizujemy położenie i rysujemy każde mięso
    for m in meats:
        # Przesuwamy mięso w dół o stałą liczbę pikseli
        m[1] += 5
        # Rysujemy mięso na ekranie
        screen.blit(meat, m)
        # Sprawdzamy, czy mięso dotknęło dolnej krawędzi okna
        if m[1] >= 600 - meat.get_height():
            # Jeśli tak, usuwamy mięso z listy i dodajemy punkt
            meats.remove(m)
            score += 1

    # Sprawdzamy, czy nastąpiła kolizja między strzelcem a kurczakiem
    for c in chickens:
        # Obliczamy odległość między środkami obrazków
        distance = ((400 - c[0] - chicken.get_width() // 2) ** 2 + (600 - shooter.get_height() // 2 - c[1] - chicken.get_height() // 2) ** 2) ** 0.5
        # Sprawdzamy, czy odległość jest mniejsza niż suma połówek szerokości obrazków
        if distance < (shooter.get_width() + chicken.get_width()) // 4:
            # Jeśli tak, usuwamy kurczaka z listy i tworzymy nowe mięso w tym samym miejscu
            chickens.remove(c)
            meats.append([c[0], c[1]])

    # Wyświetlamy liczbę punktów i liczbę zamówionych mięs w lewym górnym rogu okna
    font = pygame.font.SysFont("Arial", 32)
    text = font.render(f"Punkty: {score} / Zamówienie: {order}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Odświeżamy okno gry
    pygame.display.flip()

    # Sprawdzamy, czy zamknięto okno gry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Jeśli tak, kończymy pętlę główną gry
            running = False

    # Sprawdzamy, czy ukończono zamówienie
    if score >= order:
        # Jeśli tak, wyświetlamy komunikat o zwycięstwie i kończymy pętlę główną gry
        font = pygame.font.SysFont("Arial", 64)
        text = font.render("Gratulacje! Ukończyłeś zamówienie!", True, (0, 255, 0))
        screen.blit(text, (100, 250))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

# Zamykamy pygame
pygame.quit()

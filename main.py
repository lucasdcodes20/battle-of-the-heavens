import pygame

print('Setup Start')
pygame.init()
screen = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    # Check for all events/verifique todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close screen/fecha janela
            quit()  # end pygame/fecha pygame

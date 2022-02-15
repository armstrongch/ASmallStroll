import pygame

class menu:

    current_view = "main"

    def handle_event(self, event):
        if self.current_view == "main":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    print("pressed z")
                elif event.key == pygame.K_x:
                    self.current_view = "host"
                elif event.key == pygame.K_c:
                    print("pressed c")

    def draw(self, screen, server_instance):

        screen.fill("white")
        font = pygame.freetype.Font(None, 24)
        print_height = font.size
        display_text = []

        if self.current_view == "main":

            display_text.append("A Small Stroll")
            display_text.append("a game by Chris 'Turd Boomerang' Armstrong")
            display_text.append("press Z play solo")
            display_text.append("press X to host a co-op game")
            display_text.append("press C to join a co-op game")

        elif self.current_view == "host":
            if server_instance:
                display_text.append("Awaiting player 2")
                display_text.append("Host, Port: " + server_instance.hostname + ", " + str(server_instance.port))
                 
        for t in display_text:
            surface, rect = font.render(t)
            screen.blit(surface, (font.size, print_height))
            print_height += font.size*1.5 
        pygame.display.flip()

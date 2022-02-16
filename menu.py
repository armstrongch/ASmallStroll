import pygame

class menu:

    current_view = "main"
    player_input = ""

    def handle_event(self, event):
        if self.current_view == "main":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    print("pressed z")
                elif event.key == pygame.K_x:
                    self.current_view = "host"
                elif event.key == pygame.K_c:
                    self.current_view = "join_prompt"
        elif self.current_view == "join_prompt":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return_val = self.player_input
                    self.player_input = ""
                    return return_val
                elif event.key == pygame.K_BACKSPACE:
                    self.player_input = self.player_input[:-1]
                else:
                    self.player_input += event.unicode
                        

    def draw(self, screen, server_instance, client_instance):

        screen.fill("white")
        font = pygame.freetype.Font(None, 24)
        print_height = font.size
        display_text = []

        if self.current_view == "main":

            display_text.append("A Small Stroll")
            display_text.append("a game by Chris 'Turd Boomerang' Armstrong")
            display_text.append("press Z start a local game")
            display_text.append("press X to host an online game")
            display_text.append("press C to join an online game")

        elif self.current_view == "host":
            if server_instance:
                display_text.append("Awaiting Player 2")
                display_text.append("Host, Port: " + server_instance.hostname + ", " + str(server_instance.port))

        elif self.current_view == "join_prompt":
            if client_instance:
                if not client_instance.hostname:
                    display_text.append("Enter Host IP (press Enter when complete):")
                    display_text.append(self.player_input + "_")
                elif not client_instance.port:
                    display_text.append("Host IP: " + client_instance.hostname)
                    display_text.append("Enter Host Port (press Enter when complete):")
                    display_text.append(self.player_input + "_")

        elif self.current_view == "successful_connect":
            display_text.append("Connected!")

        elif self.current_view == "failed_connect":
            display_text.append("Failed!")
             
        for t in display_text:
            surface, rect = font.render(t)
            screen.blit(surface, (font.size, print_height))
            print_height += font.size*1.5 
        pygame.display.flip()

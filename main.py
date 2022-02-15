import pygame
import threading
from menu import *
from server import *

pygame.init()

running = None
state = None
screen = None
menu_instance = None
server_instance = None
client_instance = None

def setup_game():
    global running, state, screen, menu_instance

    running = True
    state = "menu"
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('A Small Stroll')
    menu_instance = menu()

def run_game():
    global running, menu_instance, server_instance

    try:
        while running:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    running = False

                else:

                    if menu_instance.current_view == "host":
                        if not server_instance:
                            server_instance = server()
                            server_instance.open_socket()
                            threading.Thread(target=client_server_loop).start()

                    if state == "menu":
                        menu_instance.handle_event(event)
                        menu_instance.draw(screen, server_instance)
                        
        pygame.quit()
    except SystemExit:
        pygame.quit()

def client_server_loop():
    global server_intance
    
    while server_instance:
        client_message = server_instance.listen()
        print(client_message)

setup_game()
run_game()



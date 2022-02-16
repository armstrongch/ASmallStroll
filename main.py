import pygame
import threading
from menu import *
from server import *
from client import *

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
    global running, menu_instance, server_instance, client_instance

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
                    elif menu_instance.current_view == "join_prompt":
                        if not client_instance:
                            client_instance = client()

                    if state == "menu":
                        menu_output = menu_instance.handle_event(event)
                        if menu_output:
                            handle_menu_output(menu_output)  
                        menu_instance.draw(screen, server_instance, client_instance)
                        
        pygame.quit()
    except SystemExit:
        pygame.quit()

def handle_menu_output(output):
    global menu_instance, client_instance
    if menu_instance.current_view == "join_prompt":
        if client_instance:
            if not client_instance.hostname:
                client_instance.hostname = output
            elif not client_instance.port:
                client_instance.port = output
                try:
                    client_instance.open_socket()
                    threading.Thread(target=client_server_loop).start()
                    menu_instance.current_view = "successful_connect"
                except:
                    menu_instance.current_view = "failed_connect"
                    
                

def client_server_loop():
    global server_intance, client_instance, menu_instance

    if server_instance:
        server_instance.set_conn()
        while True:
            server_instance.receive_message()
            if server_instance.client_status_string and menu_instance.current_view == "host":
                    menu_instance.current_view = "successful_connect"
    elif client_instance:
        while True:
            client_instance.send_status()
                
            
setup_game()
run_game()



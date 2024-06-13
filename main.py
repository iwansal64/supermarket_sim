def main():
    '''Main Program Starts Here!'''
    main_ui = ui.SupermarketUI(800, 800)

    
    def event_handler(event: pygame.event.Event):
        '''Handle event'''
        global main_ui
        if event.type == pygame.QUIT:
            main_ui.running = False



    while main_ui.running:
        main_ui.check_event(event_handler)
        main_ui.fill_screen((255, 255, 255))
        main_ui.supermarket_handler.create_supermarket("Samsung Store", (20, 100), (200, 200))
        main_ui.update_screen()
    

if __name__ == "__main__":
    import pygame
    import ui
    import algorithms.pathfinding
    import algorithms.path_mechanism
    import global_variables
    main()
import pygame
freedom = " 1"
#Initialize Pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((540, 600)) #(9x60),(9x60+60) (more height for bottom buttons)
pygame.display.set_caption("Sudoku")

#Game States
running = True if __name__ == "__main__" else False
game_state = 0
"""
0 = main menu
1 = in-game
2 = game over
3 = win
"""
difficulty = 0
"""
0 = easy
1 = medium
2 = hard
"""
board = None
select = [4,4,None] #[x_coordinate, y_coordinate, typed-value]


#GUI Elements
main_font = pygame.font.Font(None, 80)
sub_font = pygame.font.Font(None, 40)

title = main_font.render("SUDOKU",True,"black","white")
difficulty_select = sub_font.render("Select Difficulty", True, "black", "white")

easy = sub_font.render("Easy", True, "black", "gray")
easy_alt = sub_font.render("Easy", True, "black", "white")

medium = sub_font.render("Medium", True, "black", "gray")
medium_alt = sub_font.render("Medium", True, "black", "white")

hard = sub_font.render("Hard", True, "black", "gray")
hard_alt = sub_font.render("Hard", True, "black", "white")

medium_pos = (screen.get_width()/2-medium.get_width()/2, screen.get_height()*2/3)
easy_pos = (medium_pos[0]-easy.get_width()-10, medium_pos[1])
hard_pos = (medium_pos[0]+medium.get_width()+10, medium_pos[1])

difficulty_positions = {easy: (easy_pos, easy_alt), medium: (medium_pos, medium_alt), hard: (hard_pos, hard_alt)}

reset = sub_font.render("Reset", True, "black", "grey")
reset_alt = sub_font.render("Reset", True, "black", "white")

restart = sub_font.render("Restart", True, "black", "grey")
restart_alt = sub_font.render("Restart", True, "black", "white")

exit_but = sub_font.render("Exit", True, "black", "grey")
exit_alt = sub_font.render("Exit", True, "black", "white")

restart_pos = (screen.get_width()/2-restart.get_width()/2, screen.get_height()-restart.get_height()/2-30)
reset_pos = (restart_pos[0]-reset.get_width()-10, restart_pos[1])
exit_pos = (restart_pos[0]+restart.get_width()+10, restart_pos[1])

game_button_positions = {reset: (reset_pos, reset_alt), restart: (restart_pos, restart_alt), exit_but: (exit_pos, exit_alt)}

game_won = main_font.render("Game Won", True, "black", "white")
game_over = main_font.render("Game Over", True, "black", "white")
over_positions = {restart_alt: ((restart_pos[0], medium_pos[1]),restart)}
won_positions = {exit_alt: ((screen.get_width()/2-exit_but.get_width()/2, medium_pos[1]), exit_but)}


#Checks if mouse is inside the button
def mouse_in_button(mouse_pos, positions, position):
    if (mouse_pos[0] >= positions[position][0][0]
        and mouse_pos[0] <= positions[position][0][0]+position.get_width()
        and mouse_pos[1] >= positions[position][0][1]
        and mouse_pos[1] <= positions[position][0][1]+position.get_height()):
        return True
    else:
        return False


#Game Loop
while running:
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == 1:
                select01_temp = select[0:2]
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if select[0] > 0:
                        select[0] -= 1
                        select[2] = None
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if select[0] < 8:
                        select[0] += 1
                        select[2] = None
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if select[1] > 0:
                        select[1] -= 1
                        select[2] = None
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if select[1] < 8:
                        select[1] += 1
                        select[2] = None
                if select01_temp != select[0:2]:
                    print("selected", select[0:2])
                if event.key == pygame.K_RETURN:
                    if select[2] != None:
                        #board.place_number(select[2])
                        print("confirmed", select[2], "at", select[0:2])
                        #if board.is_full():
                        #    if board.check_board():
                        #        game_state = 3
                        #    else:
                        #        game_state = 2
                    continue
                select2_temp = select[2]
                if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                    select[2] = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                    select[2] = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                    select[2] = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                    select[2] = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP_5:
                    select[2] = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP_6:
                    select[2] = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP_7:
                    select[2] = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP_8:
                    select[2] = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP_9:
                    select[2] = 9
                if select2_temp != select[2] and select[2] != None:
                    #board.sketch(select[2])
                    print("sketched", select[2],"at",select[0:2])
                    pass
            
    #Main Menu
    if game_state == 0:
        screen.blit(title, (screen.get_width()/2-title.get_width()/2, screen.get_height()/4))
        screen.blit(difficulty_select, (screen.get_width()/2-difficulty_select.get_width()/2, screen.get_height()/2))
        for position in difficulty_positions:
            if mouse_in_button(mouse_pos, difficulty_positions, position):
                screen.blit(difficulty_positions[position][1], difficulty_positions[position][0])
                if event.type == pygame.MOUSEBUTTONUP:
                    difficulty = 0 if position == easy else 1 if position == medium else 2
                    #board = Board(screen.get_width(), screen.get_height()-60, screen, difficulty)
                    select = [4,4,None]
                    print("selected", select[0:2])
                    #board.select(4,4)
                    game_state = 1
            else:
                screen.blit(position, difficulty_positions[position][0])


    #In Game
    if game_state == 1:
        #board.update_board()
        #board.draw()
        pygame.draw.rect(screen, "gray", (0, screen.get_height()-60, screen.get_width(), 60))
        for position in game_button_positions:
            if mouse_in_button(mouse_pos, game_button_positions, position):
                screen.blit(game_button_positions[position][1], game_button_positions[position][0])
                if event.type == pygame.MOUSEBUTTONDOWN:

                    #Press Reset
                    if position == reset:
                        #board.reset_to_original()
                        pass
                    
                    #Press Restart
                    elif position == restart:
                        game_state = 0

                    #Press Exit
                    elif position == exit_but:
                        running = False
            else:
                screen.blit(position, game_button_positions[position][0])

        #Click Select
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (mouse_pos[0] > 0 and mouse_pos[1] > 0
                and mouse_pos[0] < 540 and mouse_pos[1] < 540):
                print("clicked at", mouse_pos)
                #if board.click(mouse_pos[0], mouse_pos[1]) != None:
                #    select[0] = board.click(mouse_pos[0], mouse_pos[1])[0]
                #    select[1] = board.click(mouse_pos[0], mouse_pos[1])[1]
                #    select[2] = None
                pass


    #Game Over
    if game_state == 2:
        screen.blit(game_over, (screen.get_width()/2-game_over.get_width()/2, screen.get_height()/4))
        if mouse_in_button(mouse_pos, over_positions, restart_alt):
            screen.blit(over_positions[restart_alt][1], over_positions[restart_alt][0])
            if event.type == pygame.MOUSEBUTTONUP:
                game_state = 0
        else:
            screen.blit(restart_alt, over_positions[restart_alt][0])
    

    #Game Won
    if game_state == 3:
        screen.blit(game_won, (screen.get_width()/2-game_won.get_width()/2, screen.get_height()/4))
        if mouse_in_button(mouse_pos, won_positions, exit_alt):
            screen.blit(won_positions[exit_alt][1], won_positions[exit_alt][0])
            if event.type == pygame.MOUSEBUTTONUP:
                running = False
        else:
            screen.blit(exit_alt, won_positions[exit_alt][0])
        
    pygame.display.flip()


pygame.quit()

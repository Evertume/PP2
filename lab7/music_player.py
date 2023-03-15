# Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.

import pygame

pygame.init()

# Set the window size
WINDOW_SIZE = (400, 300)

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the font
FONT = pygame.font.Font('OpenSansItalic.ttf', 36)

# Load the music files
music_files = ["Сулу_кыз.mp3", "No_Role_Modelz.mp3", "light_of_the_seven.mp3"]

# Set the current music index
current_music = 0

# Load the first music file
pygame.mixer.music.load(music_files[current_music])

# Set the screen
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the caption
pygame.display.set_caption("Music Player")


# Define the function to update the screen
def update_screen():
    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the text on the screen
    text = FONT.render("Music Player", True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 50))
    screen.blit(text, text_rect)

    # Draw the current music name on the screen and convert from snake case to more readable and delete '.mp3' format at the end
    music_name = music_files[current_music]
    text = FONT.render(music_name.replace('_', ' ')[:-4], True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, 150))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

# Call the update_screen function to display the initial screen
update_screen()

# Start the main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Play the music if userpressed 'space' button
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                # Stop the music uf user pressed 's' button
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                # Play the next music if user pressed 'n' button
                current_music = (current_music + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                # Play the previous music if user pressed 'p' button
                current_music = (current_music - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()

    # Update the screen
    update_screen()

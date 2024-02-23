import pygame
import pymunk
import random_vertices

pygame.init()
screen = pygame.display.set_mode([800,600])
space = pymunk.Space()
space.gravity = [0,5]
clock = pygame.time.Clock()
random_colors = []

def create_object(space):
    global size
    body = pymunk.Body(1, 100, pymunk.Body.DYNAMIC)
    body.position = [400,0]
    shape = pymunk.Circle(body, 5)
    shape.elasticity = 0.7
    space.add(body, shape)
    return shape

def create_click_object(space):
    global size
    body = pymunk.Body(1, 100, pymunk.Body.DYNAMIC)
    body.position = mouse_coordinates
    shape = pymunk.Circle(body, 5)
    shape.elasticity = 0.7
    space.add(body, shape)
    return shape

def draw_object(objects):
    for object in objects:
        posX = int(object.body.position.x)
        posY = int(object.body.position.y)

        
        pygame.draw.circle(screen, [255, 0, 247], (posX, posY), 5)

def create_static_circle(space):
    body = pymunk.Body(0,0,pymunk.Body.STATIC)
    body.position = random_vertices.random_verticies()
    shape = pymunk.Circle(body, 7)
    shape.elasticity = 0.7
    space.add(body, shape)
    return shape  

def draw_static_circles(static_circles):
    for static_circle in static_circles:    
        pos_X = int(static_circle.body.position.x)
        pos_Y = int(static_circle.body.position.y)
        pygame.draw.circle(screen, [0, 48, 179], (pos_X, pos_Y), 7)   

def check_and_delete_circles(objects):
    for i in objects:
        if i.body.position.y > 600:
            objects.remove(i)
            print("object removed")
mouse_coordinates = []

def main():
    running = True
    objects = []
    objects.append(create_object(space))
    static_circles = []
    static_circles.append(create_static_circle(space))

    global mouse_coordinates
    
    for i in range(0,95):
        static_circles.append(create_static_circle(space))

    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                running = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                mouse_coordinates = pygame.mouse.get_pos()
                objects.append(create_click_object(space))
            
        

        screen.fill((0,0,0))
        draw_object(objects)
        draw_static_circles(static_circles)
        check_and_delete_circles(objects)
        space.step(1/50)
        pygame.display.update()
    clock.tick(130)


if __name__ == "__main__":
    main()



init python:

    def gen_randmotion(count, dist, delay):
        import random 
        args = [ ] 
        for i in range(0, count):
            args.append(anim.State(i, None, Position(xpos=random.randrange(-dist, dist), ypos=random.randrange(-dist, dist), xanchor='left', yanchor='top', ))) 

        for i in range(0, count): 
            for j in range(0, count): 
                if i == j:
                    continue 
                args.append(anim.Edge(i, delay, j, MoveTransition(delay))) 
                return anim.SMAnimation(0, *args) 

define randmotion1 = gen_randmotion(20, 40, 20)

image snow = SnowBlossom("gui/snow.png", count=10000, border=50, xspeed=(50), yspeed=(100), horizontal=False)
image snow2 = SnowBlossom(im.MatrixColor("gui/snow.png", im.matrix.opacity(0.07)), count=10000, border=50, xspeed=(-50), yspeed=(100), horizontal=False)

import pygame

class LevelMarker():
    """

    """
    def __init__(self) -> None:
        pass

    def level_clear():
        pass

class Player():
    def __init__(self) -> None:
        self.total_points = 0



class Block():
    def __init__(self, position : tuple[int, int], angle : int) -> None:

        self.position = position #position of center
        self.angle = angle

class Ball():
    def __init__(self, start_position : tuple[int,int], launch_angle : int) -> None:
        '''
            launch_angle based on the trig circle where 90 degree
        '''
        self.position = start_position

        self.current_angle = launch_angle

        #de
    
    def draw(self) -> None:
        pass
    def move(self) -> None:
        pass


class Goal():
    def __init__(self) -> None:
        pass
        
        
import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self,  **kwargs):
        self.contents = []
        for k in kwargs:
            for n in range(0, kwargs.get(k)):
                self.contents.append(k)
        self.contents.sort(reverse=True)

    def draw(self, num):
        balls_drawn = []

        if num >= len(self.contents):
          return self.contents

        # Pick a ball at random and remove from the bag
        for i in range(num):
            ball_picked = random.choice(self.contents)
            balls_drawn.append(ball_picked)
            self.contents.pop(self.contents.index(ball_picked))

        return balls_drawn
# todo fix test 1


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    num_matches = 0
    for num in range(1, num_experiments):
        _hat = copy.deepcopy(hat)
        picked = _hat.draw(num_balls_drawn)
        picked_dict = {ball: picked.count(ball) for ball in set(picked)}
        result = True
        for k, v in expected_balls.items():
            if k not in picked_dict or picked_dict[k] < expected_balls[k]:
                result = False
                break
        if result:
            num_matches += 1
    print(num_matches, num_experiments, float(num_matches)/num_experiments)
    return round(num_matches/num_experiments, 2)



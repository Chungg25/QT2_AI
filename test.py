from problem import Problem
from search import LocalSearchStrategy


def schedule(T):
    return 1 / (T ** 2)

def test_hill_climbing(title):
    problem = Problem('monalisa.jpg')
    best_path = LocalSearchStrategy.random_restart_hill_climbing(problem, 5)
    print(best_path)
    if best_path:
        problem.draw_path(best_path, title)

def test_local_beam_search(title):
    problem = Problem('monalisa.jpg', state_start=(40, 60))
    best_path = LocalSearchStrategy.local_beam_search(problem, 2)
    print(best_path)
    if best_path:
        problem.draw_path(best_path, title)

def test_simulated_annealing_search(title):
    problem = Problem('monalisa.jpg', state_start=(40, 60))
    best_path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
    print(best_path)
    if best_path:
        problem.draw_path(best_path, title)

test_hill_climbing('hill_climbing')
test_local_beam_search('local_beam_search')
test_simulated_annealing_search('simulated_annealing_search')

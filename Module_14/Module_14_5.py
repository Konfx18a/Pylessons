import arcade
import numpy as np
import cfg

# Класс

class GridWorld:

    def __init__(self):
    # Инициализация Q-таблицы
        self.Q = np.zeros((cfg.GRID_SIZE[0], cfg.GRID_SIZE[1], len(cfg.ACTIONS)))

    # Функции для выбора действий и обновления Q-таблицы
    def choose_action(self, state):
        if np.random.rand() < cfg.EPSILON:
            return np.random.randint(len(cfg.ACTIONS))
        else:
            return np.argmax(self.Q[state])

    @staticmethod
    def collision(self, stat, rect_grid):
        if stat in cfg.STOWNS or stat not in rect_grid.keys():
            return True

    def step(self, state, action, rects_grid):
        next_state = (state[0] + cfg.ACTIONS[action][0], state[1] + cfg.ACTIONS[action][1])
        # if next_state[0] < 0 or next_state[0] >= grid_size or next_state[1] < 0 or next_state[1] >= grid_size:
        if self.collision(next_state, rects_grid):
            next_state = state  # оставаться на месте, если выходит за пределы
        reward = 1 if next_state == cfg.LABY_OUTPUT else -0.1
        done = next_state == cfg.LABY_OUTPUT
        return next_state, reward, done

    def update_q(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.Q[next_state])
        td_target = reward + cfg.GAMMA * self.Q[next_state][best_next_action]
        td_error = td_target - self.Q[state][action]
        self.Q[state][action] += cfg.ALFA * td_error


class StalkerZone(arcade.Window):

    def __init__(self, window_x, window_y, title, grid=cfg.GRID_SIZE, stowns=cfg.STOWNS,
                 bg_color=cfg.BG_COLOR, staker_cur_cell=cfg.LABY_INPUT):
        super().__init__(window_x, window_y, title)
        self.stalker_cur_cell = staker_cur_cell
        self.grid = grid
        self.stowns = stowns
        self.window_x = window_x
        self.window_y = window_y
        self.bg_color = bg_color
        self.title = title
        rect_size = int((min(window_x, window_y) - 100) / max(self.grid))
        self.rects_dict = {(i, j): (50 + rect_size * (i+0.5), 50 + rect_size * (j+0.5), rect_size, rect_size)
                          for i in range(0, self.grid[0]) for j in range(0, self.grid[1])}
        self.setup()

    def setup(self):
        # arcade.start_render()
        self.clear((255,255,255))
        self.draw_zone()

    def draw_zone(self):
        for cords, rect in self.rects_dict.items():
            if cords in self.stowns:
                arcade.draw_rectangle_filled(*rect, (127, 127, 127))
            else:
                arcade.draw_rectangle_filled(*rect, (0, 255, 0))


    def draw_stalker(self, cell):
        arcade.draw_rectangle_filled(self.rect_dict[self.stalker_cur_cell], (0, 255, 0))
        arcade.draw_circle_filled(self.rect_dict[cell][0], self.rect_dict[cell][1],
                                self.rect_dict[cell][2], (255, 0, 0))
        arcade.stalker_cur_cell = cell


if __name__ == '__main__':
    gw = GridWorld()
    stz = StalkerZone(cfg.WINDOW_X, cfg.WINDOW_Y, cfg.SCREEN_TITLE)
    arcade.run()
    # Обучение агента
    for episode in range(cfg.EPISODZ):
        cur_state = cfg.LABY_INPUT
        done = False
        while not done:
            action = gw.choose_action(cur_state)
            next_state, reward, done = gw.step(cur_state, stz.rects_dict)
            stz.draw_stalker(next_state)
            gw.update_q(cur_state, action, reward, next_state)
            state = next_state




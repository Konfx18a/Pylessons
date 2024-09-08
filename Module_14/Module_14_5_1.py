import time

import pygame as pg
import numpy as np
import cfg
from time import sleep
# Класс
class MyRect(pg.Rect):
    def __init__(self, color, text, top_x, top_y, size_x, size_y, rect_text = '' , font_size = 0, bordres = False):
        super().__init__(top_x, top_y, size_x, size_y)
        self.color = color
        self.text = text
        self.top_x = top_x
        self.top_y = top_y
        self.size_x = size_x
        self.size_y = size_y
        self.rect_text = rect_text
        self.font_size = font_size
        self.borders = bordres
        self.rect_font = None
        self.text_xy = None



class StalkerZone():

    def __init__(self, window_x, window_y, title =cfg.SCREEN_TITLE , grid=cfg.GRID_SIZE, stowns=cfg.STOWNS,
                 bg_color=cfg.BG_COLOR, staker_cur_cell=cfg.LABY_INPUT):
        self.stalker_cur_cell = staker_cur_cell
        self.grid = grid
        self.stowns = stowns
        self.window_x = window_x
        self.window_y = window_y
        self.bg_color = bg_color
        self.title = title
        self.rects_dict = {}
        self.screen = None
        self.text_font = None
        self.setup()

    def check_stowns(self):
        if cfg.LABY_INPUT in self.stowns:
            self.stowns.remove(cfg.LABY_INPUT)
        if cfg.LABY_OUTPUT in self.stowns:
            self.stowns.remove(cfg.LABY_OUTPUT)
    def setup(self):
        self.check_stowns()
        rect_size = int((min(self.window_x, self.window_y) - 100) / max(self.grid))
        self.rects_dict = {(i, j): pg.Rect(50 + rect_size * i, 50 + rect_size * j, rect_size, rect_size)
                           for i in range(0, self.grid[0]) for j in range(0, self.grid[1])}
        pg.init()
        self.screen = pg.display.set_mode((self.window_x, self.window_y))
        pg.display.set_caption(self.title)
        self.text_font = pg.font.Font(None, 72)
        self.draw_zone()
        self.draw_stalker(self.stalker_cur_cell)

    def draw_zone(self):
        for cords, rect in self.rects_dict.items():
            if cords in self.stowns:
                pg.draw.rect(self.screen, (127, 127, 127), rect )
            else:
                pg.draw.rect(self.screen, (0, 255, 0), rect, 1)
            pg.display.update()

    def draw_stalker(self, cell):
        pg.draw.circle(self.screen, (0, 0, 0), (int(self.rects_dict[self.stalker_cur_cell][0] +
                                                    self.rects_dict[self.stalker_cur_cell][2] / 2),
                                                  int(self.rects_dict[self.stalker_cur_cell][1] + self.rects_dict[self.stalker_cur_cell][2] / 2)),
                       int(self.rects_dict[cell][2] / 2))
        pg.draw.circle(self.screen, (0, 180, 0), (int(self.rects_dict[cell][0]+ self.rects_dict[cell][2]/2),
                        int(self.rects_dict[cell][1] + self.rects_dict[cell][2]/2)),
                        int(self.rects_dict[cell][2]/2))
        pg.display.update()
        self.stalker_cur_cell = cell

    def move_data(self, cell, q_values):
        self.draw_stalker(cell)
        # for x in range(0, q_values.shape[0]):
        #     for y in range(0, q_values.shape[1]):
        #         text = self.text_font.render(str(q_values[x, y]), True, (255, 0, 0))
        #         self.screen.blit(text, self.rects_dict[cell[0], cell[1]].center)
        #         pg.display.update()

class GridWorld:

    def __init__(self):
    # Инициализация Q-таблицы
        self.Q = np.zeros((cfg.GRID_SIZE[0], cfg.GRID_SIZE[1], len(cfg.ACTIONS)))
        self.mass_cells = [(x, y) for x in range(0, cfg.GRID_SIZE[0]) for y in range(0, cfg.GRID_SIZE[1])]

    # Функции для выбора действий и обновления Q-таблицы
    def choose_action(self, state):
        if np.random.rand() < cfg.EPSILON:
            return np.random.randint(len(cfg.ACTIONS))
        else:
            return np.argmax(self.Q[state])

    def collision(self, stat):
        if stat in cfg.STOWNS or stat not in self.mass_cells:
            return True

    def step(self, state, action):
        next_state = (state[0] + cfg.ACTIONS[action][0], state[1] + cfg.ACTIONS[action][1])
        if self.collision(next_state):
            next_state = state  # оставаться на месте, если выходит за пределы
        reward = 1 if next_state == cfg.LABY_OUTPUT else -0.1
        done = next_state == cfg.LABY_OUTPUT
        return next_state, reward, done

    def update_q(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.Q[next_state])
        td_target = reward + cfg.GAMMA * self.Q[next_state][best_next_action]
        td_error = td_target - self.Q[state][action]
        self.Q[state][action] += cfg.ALFA * td_error



if __name__ == '__main__':
    gw = GridWorld()
    stz = StalkerZone(cfg.WINDOW_X, cfg.WINDOW_Y, cfg.SCREEN_TITLE)
    # Обучение агента
    for episode in range(cfg.EPISODZ):
        cur_state = cfg.LABY_INPUT
        done = False
        while not done:
            action = gw.choose_action(cur_state)
            next_state, reward, done = gw.step(cur_state, action)
            gw.update_q(cur_state, action, reward, next_state)
            cur_state = next_state

    policy = np.argmax(gw.Q, axis=2)
    print("Оптимальная политика:")
    print(policy)

    # while True:
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    cur_state = cfg.LABY_INPUT
    done = False
    while not done:
        action = gw.choose_action(cur_state)
        next_state, reward, done = gw.step(cur_state, action)
        stz.move_data(next_state, np.argmax(gw.Q, axis=2))
        gw.update_q(cur_state, action, reward, next_state)
        cur_state = next_state
        time.sleep(1)
    pg.quit()








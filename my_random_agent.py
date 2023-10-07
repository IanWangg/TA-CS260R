import gymnasium as gym
import numpy as np
import argparse
## random agent
class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()

class BiasedAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space
        self.action_always = self.action_space.sample()
    def act(self, observation, reward, done):
        return self.action_always


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--display', action='store_true')
    parser.add_argument('game', nargs="?", default="CartPole-v0")
    args = parser.parse_args()

    env = gym.make(args.game, render_mode='human')
    num_episodes = 20
    num_maxstep = 100

    agent_id = 1
    if agent_id == 1:
        agent = RandomAgent(env.action_space)
    elif agent_id == 2:
        agent = BiasedAgent(env.action_space)

    reward = 0
    done = False

    for i_episode in range(num_episodes):
        observation, _ = env.reset()
        for t in range(num_maxstep):
            # env.render()
            action = agent.act(observation, reward, done)
            observation, reward, terminated, truncated, info = env.step(action)
            done = np.logical_or(terminated, truncated)
            print('episode {}-step {}, taking action {}, observation {}'.format(i_episode, t, action, observation))
        
    env.close()




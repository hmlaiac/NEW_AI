import time  # to reduce the game speed when playing manually
import unittest

import gym  # Contains the game we want to play
from pyglet.window import key  # for manual playing

# import necessary blocks from keras to build the Deep Learning backbone of our agent
from keras.models import Sequential  # To compose multiple Layers
from keras.layers import Dense  # Fully-Connected layer
from keras.layers import Activation  # Activation functions
from keras.layers import Flatten  # Flatten function
from keras.optimizers import Adam  # Adam optimizer

# Now the keras-rl2 agent. Dont get confused as it is only called rl and not keras-rl

from rl.agents.dqn import DQNAgent  # Use the basic Deep-Q-Network agent

def gameInit():
    # https://stackoverflow.com/questions/56904270/difference-between-openai-gym-environments-cartpole-v0-and-cartpole-v1
    env_name = ENV_NAME = 'CartPole-v0'  # https://gym.openai.com/envs/CartPole-v1/
    env = gym.make(env_name)  # create the environment
    nb_actions = env.action_space.n  # get the number of possible actions
    print(nb_actions)  # Cartpole has only two possible actions: Either move left or right
    return env

def buildModel(env):
    nb_actions = env.action_space.n
    model = Sequential()
    # https://keras.io/api/layers/reshaping_layers/flatten/
    model.add(Flatten(input_shape=(1,) + env.observation_space.shape))

    model.add(Dense(16))
    model.add(Activation('relu'))

    model.add(Dense(32))
    model.add(Activation('relu'))

    model.add(Dense(nb_actions))
    model.add(Activation('linear'))

    return model

import unitest
class TestRLModules(unittest.TestCase):
    def test_start_game(self):
        env = gameInit()
        env.reset()  # reset the environment to the initial state
        for _ in range(200):  # play for max 200 iterations
            env.render(mode="human")  # render the current game state on your screen
            random_action = env.action_space.sample()  # chose a random action
            env.step(random_action)  # execute that action
        env.close()  # close the environment

    def test_play_game(self):
        env = gameInit()
        action = 0
        def key_press(k, mod):
            '''
            This function gets the key press for gym
            '''
            global action
            if k == key.LEFT:
                action = 0
            if k == key.RIGHT:
                action = 1

        env.reset()
        rewards = 0
        for _ in range(1000):
            env.render(mode="human")
            env.viewer.window.on_key_press = key_press  # update the key press
            observation, reward, done, info = env.step(action)
            rewards += 1
            if done:
                print(f"You got {rewards} points!")
                break
            time.sleep(0.1)  # reduce speed a little bit
        env.close()

    def test_build_model(self):
        env = gameInit()
        model = buildModel(env)
        print(model.summary())


    def test_train_model(self):
        env = gameInit()
        nb_actions = env.action_space.n
        model = buildModel(env)

        from rl.memory import SequentialMemory  # Sequential Memory for storing observations ( optimized circular buffer)
        memory = SequentialMemory(limit=20000, window_length=1)

        # LinearAnnealedPolicy allows to decay the epsilon for the epsilon greedy strategy
        from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

        policy = LinearAnnealedPolicy(EpsGreedyQPolicy(),
                                      attr='eps',
                                      value_max=1.,
                                      value_min=.1,
                                      value_test=.05,
                                      nb_steps=20000)

        dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
                       target_model_update=100, policy=policy)

        # Use learning_rate instead of lr if you get warning
        dqn.compile(optimizer=Adam(learning_rate=0.001), metrics=['mae'])

        dqn.fit(env, nb_steps=20000, visualize=False, verbose=2)

        # dqn.save_weights(f'dqn_{env_name}_weights.h5f', overwrite=True)

        # Testing
        dqn.test(env, nb_episodes=5, visualize=True)
        env.close()

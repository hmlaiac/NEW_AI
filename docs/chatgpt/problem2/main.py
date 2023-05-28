import gym
import tensorflow as tf
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy

# Set up the environment
env_name = 'CartPole-v1'
env = gym.make(env_name)
num_actions = env.action_space.n

# Define the Q-network architecture
model = Sequential([
    Dense(64, input_shape=(4,), activation='relu'),
    Dense(64, activation='relu'),
    Dense(num_actions, activation='linear')
])
print(model.summary())
# Set up the DQN agent
memory = SequentialMemory(limit=10000, window_length=1)
policy = EpsGreedyQPolicy()
dqn_agent = DQNAgent(
    model=model,
    nb_actions=num_actions,
    memory=memory,
    nb_steps_warmup=10,
    target_model_update=1e-2,
    policy=policy
)
dqn_agent.compile(optimizer=Adam(lr=1e-3), metrics=['mae'])

# # Train the agent

# dqn_agent.fit(env, nb_steps=10000, visualize=False, verbose=2)
#
# # Evaluate the agent
# dqn_agent.test(env, nb_episodes=5, visualize=True)
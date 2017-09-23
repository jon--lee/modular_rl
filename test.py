import knet
import gym
import argparse
import pickle
import IPython

ap = argparse.ArgumentParser()
ap.add_argument('--ident', required=True)
args = vars(ap.parse_args())
directory = 'data/' + args['ident'] + '/'

weights = pickle.load(open(directory + 'weights.pkl', 'r'))
stats = pickle.load(open(directory + 'stats.pkl', 'r'))

net = knet.Network([64, 64])
net.load_weights(directory + 'weights.pkl', directory + 'stats.pkl')

env = gym.envs.make('HalfCheetah-v1')

s = env.reset()
for t in range(200):
    a = net.predict([s])[0]
    s, _, _, _ = env.step(a)
    env.render()



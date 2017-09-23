This is not my code. This is from John Schulman's modular_rl. I made minor changes and added some files to make things easier.

#Getting started#


Packages for modular rl:

	virtualenv env
	source env/bin/activate
	pip install numpy tabulate scipy
	pip install keras==1.0.1
	pip install theano==0.8.2
	
Gym + optional mujoco-py if you don't already have it:

	git clone git@github.com:openai/gym.git
	cd gym
	pip install -e .
	pip install mujoco-py==0.5.7

If you would like to use mujoco-py make sure that you have mujoco 131 installed with a valid license.

Run both of these to make sure it's working:
	
	KERAS_BACKEND=theano python ./run_pg.py --env HalfCheetah-v1 --agent modular_rl.agentzoo.TrpoAgent

When you run this, a new directory will be created in data/IDENTIFIER/. Each iteration, it will save weights.pkl, which contains the network weights/biases,
and stats.pkl, which contains mean/std for inputs.

This code requires fairly specific packages. If you only care about getting a policy and not modifying/analyzing the RL part, then
the best thing to do is run the code in this env and then copy the weights/stats to your project and use your own project's env.

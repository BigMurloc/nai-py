# Breakout Reinforcement Learning Agent

This package contains two main python scripts `breakout_evaluation.py` and `breakout_trainer.py`  
`breakout_trainer.py` - trains the data model which is saved under training/model, the RL algorithm of choice is A2C.

`breakout_evaluation.py` - evaluates the trained model, the output is (average_score, standard_deviation)  

There are 4 available trained models in this repository with different amount of timesteps 
[**100k**, **300k**, **600k**, **900k**]

## A2C - 100k
Average score: 7.0  
Standard deviation: 2.79

## A2C - 300k
Average score: 10.8  
Standard deviation: 3.12

## A2C - 600k
Average score: 14.5  
Standard deviation: 3.74

## A2C - 900k
Average score: 17.3  
Standard deviation: 8.1

# Authors
- Dominik Pasymowski
- Michał Cichowski

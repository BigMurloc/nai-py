# Breakout Reinforcement Learning Agent

This package contains two main python scripts `breakout_evaluation.py` and `breakout_trainer.py`  
`breakout_trainer.py` - trains the data model which is saved under training/model, the RL algorithm of choice is A2C.

`breakout_evaluation.py` - evaluates the trained model, the output is (average_score, standard_deviation)  

There are 4 available trained models in this repository with different amount of timesteps 
[**100k**, **300k**, **600k**, **900k**]

## A2C - 100k
Average score: 7.0  
Standard deviation: 2.79


https://github.com/BigMurloc/nai-py/assets/57963469/881c965a-6597-48c4-9646-37d7a50ff61b


## A2C - 300k
Average score: 10.8  
Standard deviation: 3.12


https://github.com/BigMurloc/nai-py/assets/57963469/8aea4f7a-f602-4578-8406-bcba986d4728


## A2C - 600k
Average score: 14.5  
Standard deviation: 3.74


https://github.com/BigMurloc/nai-py/assets/57963469/5723dd12-1eb7-40a0-8041-a1dacf5f7c57


## A2C - 900k
Average score: 17.3  
Standard deviation: **8.1**


https://github.com/BigMurloc/nai-py/assets/57963469/c314cc8d-6bc8-4ed2-9814-e084fc1737b9


# Authors
- Dominik Pasymowski
- Michał Cichowski

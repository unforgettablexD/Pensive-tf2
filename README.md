# Pensieve Reproduce

Reproduce [pensieve](https://github.com/hongzimao/pensieve/tree/master).

Use the commands below to easily set up virtual envs and requirements without worrying about version issues.

## Setup

Set up conda env

```bash
conda create -n venev_tf1 pyhton=2.7
conda activate
```

Install dependencies

```bash
pip install tensorflow==1.1.0
pip install tflearn==0.3.1
conda install matplotlib
```

## Run

```bash
python multi_agent.py
```

To see how reward is changing over time.
```bash
python plot_reward.py
```

If you need to train on different videos, setup video files and run:
```bash
python get_video_sizes.py
```

## Test

Copy the model to abr_eval/models, change path in rl_no_training.py file.

```bash
python rl_no_training.py
python bb.py
python mpc.py
python dp.py
```

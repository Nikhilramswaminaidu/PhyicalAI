1. License

PyBullet is open source under the zlib license (very permissive).

Stable-Baselines3 is under MIT license.

PyTorch is also BSD-style open source license.
✅ So: your whole pipeline is free and open-source friendly.

2. Size of the Data Source

In RL, there isn’t a static dataset — the “data” is experience collected from simulation.

Typical small-scale PyBullet tasks (e.g., ReacherBulletEnv, Walker2DBulletEnv) generate on the order of hundreds of thousands to a few million timesteps.

Stored rollouts are usually lightweight — e.g., a few GBs if logged fully, but not like giant supervised datasets.
✅ So: “Data size is ~1–5 GB for logging 1M+ timesteps depending on task.”

3. Size of the Model

PPO/SAC policies for PyBullet robots are usually small feedforward neural nets (MLPs with 2–3 layers, 64–256 units each).

This comes to ~1–5 MB of parameters — tiny compared to vision or language models.
✅ So: “Model size is ~2–5 MB depending on architecture.”

4. Current Time to Train

On a single GPU (RTX 3050/3060/3090 class), training a simple robot (e.g., Reacher or Walker2D) to reasonable performance with PPO takes 2–6 hours for ~1M timesteps.

More complex environments (Ant, Humanoid) can take 12–24 hours.
✅ So: “Baseline task converges in ~4 hours on a single GPU; larger tasks may require 12–24 hours.”

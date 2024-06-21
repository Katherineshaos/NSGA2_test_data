import gym


def main():
    env = gym.make('CartPole-v0')
    for i_episode in range(20):
        observation = env.reset()  # 得到环境给出的初始反馈 Cart Position；Cart Velocity ；Pole Angle ；Pole Angular Velocity
        for t in range(100):
            env.render() # 画出当前场景情况
            # print(observation)
            action = env.action_space.sample()   # 产生一个允许范围内的随机行动  Push cart to the left；Push cart to the right
            observation, reward, done, info = env.step(action)  # 得到该次行动的反馈  env.step() 有四个返回值，分别代表着 反馈，奖励，是否结束，其他信息 。
            print(reward)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break
    env.close()


if __name__ == "__main__":
    print(1)
    main()

#https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Ben Kocan		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: bkocan3	  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903952660  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "bkocan3"  # replace tb34 with your Georgia Tech username.
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return 903952660  # replace with your GT ID number
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    win_prob = 0.47  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		  		 		  		  		    	 		 		   		 		  
    # print(get_spin_result(win_prob))  # test the roulette spin
    # plt.plot(episode_simulator(.47))gr

    create_fig_one(win_prob)
    create_fig_two(win_prob)
    create_fig_three(win_prob)
    create_fig_four(win_prob)
    create_fig_five(win_prob)


    # add your code here to implement the experiments

    # tester = np.empty(5)
    # tester[1] = 100
    # plt.plot(tester)
    # plt.show()
  		  	   		  		 		  		  		    	 		 		   		 		  

def episode_simulator(win_prob, realistic, bankroll):
    bet_num = 0
    episode_winnings = 0
    won80 = 0
    lost256 = 0
    # results = np.zeros(1000)
    results = np.full(1001, 80)

    while episode_winnings < 80:
        won = False
        bet_amount = 1

        while not won:
            if bet_num >= 1001:
                return results
            results[bet_num] = episode_winnings
            bet_num += 1
            # print("# of bets: " + str(bet_num))
            # print("you are betting " + str(bet_amount))
            if realistic and episode_winnings <= -bankroll:
                results[bet_num:] = -bankroll
                lost256 +=1
                return results

            if realistic and bet_amount > (bankroll - episode_winnings):
                bet_amount = bankroll - episode_winnings

            won = get_spin_result(win_prob)

            if won == True:
                episode_winnings = episode_winnings + bet_amount
                # print("you won, episode winnings are " + str(episode_winnings))
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount*2
                # print("you lost, episode winnings are " + str(episode_winnings))
                # print("better double down to " + str(bet_amount)
    return results


def create_fig_one(win_prob):
    plt.title("Figure 1")
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Number of Bets")
    plt.ylabel("Earnings")

    for i in range(10):
        episode = episode_simulator(win_prob, False, None)
        plt.plot(episode)

    plt.savefig("./images/fig1.png")
    plt.clf()

def create_fig_two(win_prob):
    matrix = np.zeros((1001, 1001))
    plt.title("Figure 2")
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Number of Bets")
    plt.ylabel("Earnings")

    for i in range(1000):
        episode = episode_simulator(win_prob, False, None)
        matrix[i] = episode

    mean = matrix.mean(axis = 0)
    standard_deviation = matrix.std(axis = 0)
    sd_plus = mean + standard_deviation
    sd_minus = mean - standard_deviation

    plt.plot(mean, label="Mean")
    plt.plot(sd_plus, label="Mean + SD")
    plt.plot(sd_minus, label="Mean - SD")
    plt.legend(loc="lower right")
    plt.savefig("./images/fig2.png")
    plt.clf()

def create_fig_three(win_prob):
    matrix = np.zeros((1001, 1001))
    plt.title("Figure 3")
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Number of Bets")
    plt.ylabel("Earnings")

    for i in range(1000):
        episode = episode_simulator(win_prob, False, None)
        matrix[i] = episode

    median = np.median(matrix, axis = 0)
    standard_deviation = matrix.std(axis = 0)
    sd_plus = median + standard_deviation
    sd_minus = median - standard_deviation
    # print(matrix)

    plt.plot(median, label="Median")
    plt.plot(sd_plus, label="Median + SD")
    plt.plot(sd_minus, label="Median - SD")
    plt.legend(loc="lower right")
    plt.savefig("./images/fig3.png")
    plt.clf()


def create_fig_four(win_prob):
    plt.title("Figure 4")
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Number of Bets")
    plt.ylabel("Earnings")

    matrix = np.zeros((1001, 1001))
    for i in range(1000):
        episode = episode_simulator(win_prob, True, 256)
        matrix[i] = episode

    mean = matrix.mean(axis=0)
    standard_deviation = matrix.std(axis=0)
    sd_plus = mean + standard_deviation
    sd_minus = mean - standard_deviation
    plt.plot(mean, label="Mean")
    plt.plot(sd_plus, label="Mean + SD")
    plt.plot(sd_minus, label="Mean - SD")
    plt.legend(loc="lower right")
    plt.savefig("./images/fig4.png")
    plt.clf()


def create_fig_five(win_prob):
    plt.title("Figure 5")
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Number of Bets")
    plt.ylabel("Earnings")

    matrix = np.zeros((1001, 1001))
    for i in range(1000):
        episode = episode_simulator(win_prob, True, 256)
        matrix[i] = episode

    median = np.median(matrix,axis=0)
    standard_deviation = matrix.std(axis=0)
    sd_plus = median + standard_deviation
    sd_minus = median - standard_deviation
    plt.plot(median, label="Median")
    plt.plot(sd_plus, label="Median + SD")
    plt.plot(sd_minus, label="Median - SD")
    plt.legend(loc="lower right")
    plt.savefig("./images/fig5.png")
    plt.clf()


if __name__ == "__main__":
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  

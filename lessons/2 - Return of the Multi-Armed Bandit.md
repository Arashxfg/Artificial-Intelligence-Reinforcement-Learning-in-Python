# Section Introduction The Explore-Exploit Dilemma

&nbsp;&nbsp;&nbsp;In this lecture I'm going to introduce you to this next section of the course which is all about the explore exploit dilemma and different algorithms for solving it. To start I'm going to introduce you to the problem that we're trying to solve. And then in the rest of the lecture I'll outline what we'll cover in the rest of this section.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_1.PNG)

&nbsp;&nbsp;&nbsp;so like many Problems in Probability the typical analogy we use for the exploit exploit problem starts with the casino. Let's pretend that we go into a casino and we have a choice between a two slot machines. Let's also assume that these are very simple slot machines. You either win or you lose. There is no in. And if you win the prize is always the same. So without loss of generality we can say that winning gives you one dollar and losing gives you zero dollars. Let's now go through an imaginary sequence of events and what I would like you to do is to think about how you would choose which machine to play.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_2.PNG)

&nbsp;&nbsp;&nbsp;So starting out all we see is two machines we know absolutely nothing about them other than what I just told you. You can either win or lose. And when you win you'll get a dollar. At this point how do we choose which slot machine to play. In fact it doesn't matter because we know nothing about either machine. Any choice would be equivalent.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_3.PNG)

&nbsp;&nbsp;&nbsp;So let's pick a slot machine number one and let's say Oh no. We lost. So what's our next move at this point. We know something about slot machine number one. We know that we played once and we lost once. What do we know about slot machine number two. Well we still don't know anything. Again I want you to think about which slot machine would you pick to play now. Most of us would probably pick number two and it's useful to think about why. Why pick Number two instead of number one. Well we all know how to calculate probabilities the probability of success would be the number of times we won divided by the number of times we played in the case of slot machine number one. That would be zero out of one which is 0 but for a slot machine number two it's zero out of zero which is undefined and is something in our intuition tells us that undefined is better than zero even though numerically you can't compare these numbers.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_4.PNG)

&nbsp;&nbsp;&nbsp;OK so let's say we played slot machine number two and we won. Here's where we stand now. We played slot machine number one once and we lost that one time we played slot machine number two once and we won that one time. So which one do we play next again. Most of us would pick slot machine number two. It appears so far that slot machine number 2 has a better chance of winning at one hundred percent than slot machine number one which is a 0 percent chance of winning at this point. You should be thinking statistically is there anything wrong with my calculations. Is it wrong for me to assign a zero percent to machine number one and one hundred percent to machine number two. You should recognize that these estimates are exactly what we would call the maximum likelihood estimate.But ask yourself Is there something incomplete about these measurements

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_5.PNG)

&nbsp;&nbsp;&nbsp;since we decide to play slot machine number two again. We observe the result and unfortunately we lose. But if we look at these machines in a maximum likelihood way machine number two still looks better. Machine number one has a 0 percent chance of winning and machine number 2 has a 50 percent chance of winning. So let's play again on slot machine number two.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_6.PNG)

&nbsp;&nbsp;&nbsp;So we play slot machine number two again and unfortunately we lose yet again at this point. Our updated probability of winning for a slot machine number two is 33 percent. Note that this is still better than slot machine number one. So if we use our maximum likelihood estimate to greedily choose which machine to play we will choose machine number two.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_7.PNG)

&nbsp;&nbsp;&nbsp;so we play machine number two again. And unfortunately we lose again. Now we've lost three times and won once so the probability of winning with machine number two is twenty five percent at this point. If I ask you which machine do you decide to play next. There would be more disagreement about whether a play machine number one or machine number two. And by that I mean relative to the first time we chose machine number two as you recall the first time we chose to play machine number two. We didn't know anything about it. We hadn't collected any data at that point. So our estimate of the win rate was zero out of zero which is undefined. Now we have more data. We've won once and we've lost three times. So we calculate our win rate as 25 percent. On the other hand for machine number one our calculated win rate is 0 percent but we've only played once we know that this is somehow less accurate. So we might want to play machine number one again so that we can be more certain. I want you to think about what kinds of mathematical tools do you use in your mind to come to that conclusion. Why do we go against making a greedy choice based on the maximum likelihood estimate of the win rates

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_8.PNG)

&nbsp;&nbsp;&nbsp;so if you're a traditional statistician doing frequent test a B tests you would be yelling at me saying that I'm approaching this problem all wrong. The correct way you say would be to decide before even walking into the casino how much data I should collect. This will help me to determine the statistical power of my experiment. I also need to determine what the effect size will be if you're not familiar with effect size. It's related to the difference between the win rates of the two slot machines then what I'll do is I'll take that do some fancy power calculation and that will tell me how many samples I need to collect at this point. Alarm bells should be ringing in your head. How do you know the effect size if you haven't even played any of the slot machines to begin with. That is just one of the many reasons why traditional statistical tests are very awkward .

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_9.PNG)

&nbsp;&nbsp;&nbsp;OK so let's say you do your fancy calculations and it says you need to play a slot machine at 10000 times. Now imagine the scenario you've played a slot machine 5000 times so far. Slot machine number one has won three times out of 5000 slot machine number two has won 4000 times out of 5000. So basically your prediction of the effect size was wrong. But in order for this to be a valid statistical test in the eyes of a statistician you must take your experiment to completion. You cannot simply stop your experiment at 5000 and say I think slot machine number two is better than slot machine number one. That would invalidate your results. Yet another reason why traditional statistical testing is quite awkward. You might also want to consider a more serious scenario. What if you were testing a lifesaving drug and it's been successful. Ninety seven percent of the time in your test group you still continue your experiment giving the placebo to the control group which has no effect at all.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_10.PNG)

&nbsp;&nbsp;&nbsp;Is that ethical? so maybe you say we should throw this traditional method and use a method that can adapt as new data is collected. This would be similar to what we originally did in this lecture using our intuition in this section. We will learn about how we can do that algorithmically and quantitatively rather than just by mere feelings. What you encountered earlier in this lecture was two opposing forces on one hand you wanted to be like a good statistician and collect lots of data so that you could make your estimate more accurate. We call that exploration on the other hand. We wanted to choose the slot machine that had the highest win rate so that we could earn more money. We call that exploitation and because these two objectives oppose one another. We call this a dilemma. Hence the term explore exploit dilemma.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_11.PNG)

&nbsp;&nbsp;&nbsp;All right so as I mentioned the rest of this section is devoted to algorithms that will solve this problem. We'll be looking at four main algorithms. The first is called Epsilon greedy which is something we'll be using all throughout reinforcement learning in this course and others. The second is called the optimistic initial value method. The third is called at UCB one UCB stands for upper confidence bound and finally the fourth is called Thompson sampling which makes use of Bayesian statistics. Sometimes people will call this the Bayesian bandit method and it just so we don't lose sight of the big picture. These are all algorithms you can use in place of a traditional a B test in your software system. They are methods that overcome some of the awkward problems like effect size wanting to stop your experiment early and the controversial p value B's methods are adaptive meaning that they learn on the fly which might be considered advantageous especially in high throughput online business settings.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_12.PNG)




# Epsilon-Greedy Theory

&nbsp;&nbsp;&nbsp;In this lecture we are going to study what is probably the most important algorithm of this section `Epsilon greedy`. The reason I say it's the most important is because if you're planning on studying reinforcement learning anywhere from Monte Carlo to Q learning to deep Q learning and other similar approaches you'll be using Epsilon greedy the whole way through. On the other hand you'll find that the other methods such as UCB one and the Bayesian method often perform better for this particular use case. Overall however these algorithms all have the same general API from a programming perspective they all give you a way to balance exploration with exploitation.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_13.PNG)

&nbsp;&nbsp;&nbsp;So what's the main idea behind Epsilon greedy. Well let's remember what the problem is with exploring and exploiting. We observe that if we just take a naive maximum likelihood estimate of the win rate. This is highly detrimental for exploration and data collection we might get lucky or unlucky with a particular bandit and then end up exploiting something suboptimal because the win rate on all the other bandits is just zero out of one. By the way it's important to give a name to that strategy. We call this the greedy method. If you've never taken a class on algorithms and data structures that might seem like a confusing term but basically it means to do something short sighted or to use only immediately available information as a higher risk stick to make a decision. In our case being greedy means playing the bandit with the highest maximum likelihood win rate without any regard to how much data we've collected or how confident we are in the win rates that we calculated.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_14.PNG)

&nbsp;&nbsp;&nbsp;so why is it important to call this the greedy strategy. Well as you can probably tell by its name Epsilon greedy is perhaps some kind of modification of this basic greedy strategy. And if that's what you guessed then you would be correct. So Epsilon greedy says instead of always taking the greedy action I'm going to have a small probability of just doing something completely random that is to say with some small probability I'm going to choose a slot machine at random without any regard to what its win rate is. And of course that small probability is given by the value of epsilon. Typically we would choose a value of epsilon like 10 percent or 5 percent

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_15.PNG)

&nbsp;&nbsp;&nbsp;if we were to write some pseudocode. Here's how greedy and epsilon greedy would compare. Let's assume that for each algorithm we never stop playing. So each algorithm goes inside an infinite loop in the purely greedy case we select the JF bandit which is the bandit that has the current largest mean ones we've selected the jade bandit. We play that bandit and collect the reward called X.. Remember that X can be 0 or 1. So far we'll see other cases where X can be a real number but just hold that thought for now. Once we have X we can update the estimate for the mean of the bandit we selected in the Epsilon greedy case. There's one extra step where we select the bandit instead of just taking the ARG Max. We start by choosing a random number p between 0 and 1. If p is less than epsilon we choose a bandit at random from a uniform distribution. Otherwise we choose the ARG Max. This ensures that we choose a random bet with probability Epsilon. Now a common question I get is shouldn't it be p greater than epsilon and not p less than epsilon. If that's the question you have I would strongly recommend writing some simple code and checking the frequency of how many times P is less than and greater than epsilon. That should help you clear things up. Finally the last few steps are the same. We play Ben AJ and then update the mean for bandage.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_16.PNG)

&nbsp;&nbsp;&nbsp;At this point. You should be ready to implement your own version of the Epsilon greedy algorithm but I want to go over a few more key points that are important to analyze its efficacy let's remember that the reason we want to explore which is accomplished by having a non-zero Epsilon is so that we can collect data about each band. And the reason we want to collect data about each band it is because we want our estimates of their win rate to be accurate. But at what point do we say we have enough data. Let's stop exploring. What happens if we let the algorithm continue to run forever. In that scenario our algorithm will never stop exploring and hence our total collected reward will be suboptimal by definition. If one of the bandits is optimal then the other bandits are not optimal. Let's suppose we have two bandits with win rates and 90 percent and 80 percent. Clearly if we knew this information beforehand we would only play the bandit with a 90 percent win rate and never play the bandit with the 80 percent win rate. Of course we can't do that without collecting data. So we run the Epsilon greedy algorithm instead in the long run however we will never reach a 90 percent win rate due to the fact that we always have a small chance of exploration and playing the suboptimal bandit we can break down our calculation of the average win rate like this. First suppose that after a long time we've identified the optimal bandit so that for one minus epsilon of the time we will select the optimal bandit which gives us expected reward. Zero point nine then epsilon of the time. We will choose either of the bandits with equal probability. So when that happens are expected reward is zero point eight five halfway between zero point nine and zero point eight. Therefore our total expected reward is 1 minus epsilon time zero point nine plus epsilon time zero point eighty five.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_17.PNG)

&nbsp;&nbsp;&nbsp;one option to improve This behaviour is to have a decaying Epsilon in the literature. There have been several different kinds of cooling schedules used. We want to be aware of what they are and perhaps do an experiment to see what works best for our use case. So one option is to have the value of epsilon decay proportional to one over the number of steps. Another option is to let Epsilon decay linearly and then stop at either zero or a small value slightly larger than zero Another option is to use exponential cooling or one over the logarithm. So there are many options for you to try out the common theme among them being that they all decrease over time.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_18.PNG)





# Calculating a Sample Mean
 
&nbsp;&nbsp;&nbsp;In this lecture we are going to do a little exercise that might help you in your implementation of epsilon greedy. This lecture is all about how to calculate a sample mean although it seems very simple. This lecture will introduce you to a very important concept that we are going to gradually build on. As we progressed throughout the course now you might object to this and say Wasn't the sample mean part of the warm up. I thought we already knew how to do this and the answer to that is just wait and see.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_19.PNG)

&nbsp;&nbsp;&nbsp;First let's start with a question you might have if we're working with binary rewards that can only be 0 or 1. What is the purpose of having a sample mean. You might say isn't the Bernoulli distribution a categorical distribution. In fact you can prove to yourself that if the values of the random variable can only be 0 or 1 then the sample mean is exactly the maximum likelihood estimate of the Bernoulli parameter. Please try this yourself at home. If you haven't done so before or if you don't understand how this works.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_20.PNG)

&nbsp;&nbsp;&nbsp;So now that we understand that we can unify real valued rewards and binary rewards under the same sample mean calculation. Let's talk about what's the best way to calculate the sample mean using the formula for the sample mean. You might suggest that this is quite obvious. Just take all the values of x that you've collected. Add them together and divide by the total number of X's that you have. The question is what's wrong with this. I'll give you a minute to think about it. 

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_21.PNG)

&nbsp;&nbsp;&nbsp;So hopefully you thought about why calculating the sample mean naively might not be such a good idea. Remember that we are going to run our algorithms essentially forever in order to run forever. We must have a forever amount of space to store those values of x that we collect and obviously our computers or our servers don't have an infinite amount of space. And even if they did calculating a summation is all then so the more data you have the longer it will take and that will increase linearly with how much data you collect. Here's my claim. I claim that you can make the calculation of a sample mean 0 of 1 in both space and time complexity no matter how much data you collect. Again as an exercise before moving on to the next slide I want you to think about how this might be the case.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_22.PNG)

&nbsp;&nbsp;&nbsp;So hopefully you thought about how you might calculate a sample mean using constant space and time.The key is that you can calculate the sample mean using the previous sample mean let's call the sample mean after collecting in samples x bar subscript n and this is so that the sample mean after collecting and minus one samples is x bar subscript N minus one. We can write down both of these which I hope is pretty obvious. Now that you know the main trick conceptually let's make this an exercise. Can you express x bar n in terms of x bar and minus one .

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_23.PNG)

&nbsp;&nbsp;&nbsp;Okay so here's what you do. First you can take x bar n and split up the summation so that you only sum up to end minus one. Then you leave x subscript n by itself. This is just the last sample that you've collected. The next step is to realize that the sum of the excise from one up to and minus one can be expressed in terms of x bar subscript N minus one. We just have to rearrange the equation from earlier. It's clear that the sum is just N minus one times x bar and minus one. We can substitute this into our expression for x bar n to get the sample mean at time n in terms of the sample mean at time and minus one.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_24.PNG)

&nbsp;&nbsp;&nbsp;One interesting thing you can do although it's not totally clear why you'd want to do this at this point is split this formula up as follows. The first step is to multiply out the one over n turn. This gives us and minus one of our n as the first coefficient and one over n as the second coefficient the second step is to simplify and minus one over n to one minus one over n the third step is to multiply out the X Bar and minus one term and then combine the terms that have the coefficient one over n at this point you may or may not know why we did this but that's OK. Just think of it as a fun math exercise and we'll return to it later. 

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_25.PNG)

&nbsp;&nbsp;&nbsp;So what have we learned in this section. We've seen that the sample mean at time n can be evaluated in constant time and the amount of space we need to make this calculation is also constant. We only ever need to store a few things. The previous sample mean the newest sample and the number of samples we've collected. This by itself is quite useful and should help you implement not just Epsilon greedy but many of the other algorithms will learn about. And although this is quite useful on its own you'll see later when you study reinforcement learning that it actually goes much deeper.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_26.PNG)



# Epsilon-Greedy Beginner's Exercise Prompt

[code_1](../code_files/1_epsilon_greedy_starter/epsilon_greedy_starter.py)



# Epsilon-Greedy in Code

[code_2](../code_files/2_epsilon_greedy/epsilon_greedy.py)




# Comparing Different Epsilons

&nbsp;&nbsp;&nbsp;In this lecture we are going to look at another script that will still use epsilon greedy but you'll learn a few new things. In particular you'll learn about what happens when we use different values of epsilon. So you see how the outcome changes and you'll be able to compare the results for different values of epsilon. In addition in this lecture we'll work with a real value add reward. Our reward will be Gaussian distributed. That's equivalent to saying that the reward is a sample drawn from and Amu sigma squared where Mew is the mean and sigma squared is the variance since the basic outline of this script is pretty much exactly the same as the previous scripts. I'm only going to go over the differences just to remind you there are three main parts. First we have the banded arm class. Second we have a function that runs an experiment over multiple trials. And third we print and plot the results. So let's start with the bandit arm class. What's different about this. In fact the only real difference here is the pull function because the reward distribution has changed. As you can see we are drawing a sample from a Gaussian distribution with mean M and A variance one rather than a Bernoulli but importantly you'll recall we discussed earlier that in both cases the way that you calculate the sample mean is exactly the same. So that's why the update function hasn't changed. Next we have the experiment function and this function we taken a few arguments. First we have M1 M2 and M3. These represent the means of each band. Of course this implies that we're going to have three bandits. After this we do our Epsilon greedy loop. You'll notice that it's exactly the same as before. No changes are required at the end of this function. When we plot the results you'll notice that I have this new line here. T X scale log. This makes it so that the plot shows up on a log scale rather than a linear scale. The reason for this is these algorithms will converge quite fast so it's difficult to truly see the differences between each value of epsilon using a log scale allows us to zoom in to the relevant parts of the plot. We also return the cumulative average reward from this function so that in the main section of this script we can plot the cumulative averages for different values of epsilon in the same plot. In the main section you can see the parameters of our experiment. The mean of each band it will be one point five 2.5 and three point five. The values of epsilon will try or zero point one zero point zero five and zero point zero one. Finally you will run each experiment for one hundred thousand trials so let's run this and see what we get. So if we look at the cumulative reward plots we can see that they all converge to the optimal band around three point five minus any penalty for occasionally selecting the suboptimal banded so here's a different Epsilon we can see that we get a little closer. And here's another Epsilon so the real interesting plot is when you compare all three together we can see that for Epsilon equals 5 percent and 10 percent they obtain a higher cumulative reward much more quickly than for Epsilon equals 1 percent Epsilon equals 1 percent. It still converges but does so more slowly on the other hand if we look at the long run cumulative reward we can see that for higher values of Epsilon the cumulative reward is worse and worse. So there is a tradeoff here. Do you want quick conversions or do you want a higher eventual reward on some applications. You might have to take into account the length of the experiment. So if you're doing a short experiment maybe you can't afford it to wait for the rewards to converge and therefore you would have to choose and epsilon that reflects your requirements. All right. So if we look at the printout here's what we see first. We can see that in all cases our estimate of the mean of each band it gets pretty close to the true values one point five two point five and three point five. At the same time we can see that the percentage of time that each algorithm spends selecting sub optimal bandits is very different for each value of epsilon for Epsilon equals 10 percent. We choose a suboptimal band it over 6 percent of the time for Epsilon equals 5 percent. We choose a suboptimal band it over 3 percent of the time in perhaps line equals 1 percent. We choose a suboptimal band approximately 1 percent of the time.


[code_3](../code_files/3_comparing_epsilons/comparing_epsilons.py)





# Optimistic Initial Values Theory

&nbsp;&nbsp;&nbsp;In this lecture we are going to talk about a different method of solving the explore exploit dilemma known as the optimistic initial values method. The optimistic initial values method is an extremely simple modification of the purely greedy method. In other words we don't even need any concept of epsilon and random exploration the way it works is this. As you recall in our measurement of the sample mean we update our current estimate based on our previous estimate. Our initial estimate is zero. To ensure that all the math works out and we get exactly the sample mean the optimistic initial values method says this. What if instead of initializing the initial estimate to zero we pick a really large value and include that in the estimate of the sample mean.   In this way we're not really estimating the mean per say we're actually overestimating the mean .

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_27.PNG)

&nbsp;&nbsp;&nbsp;Let's look at some pseudocode for how this would work. First we initialize all the bandits to have their initial means to be very large values. As a side note they must be finite because if you pick infinity then you can't do any further calculations with infinity plus anything is still infinity. Then inside our experiment instead of doing any kind of random exploration we simply choose the bandit with the highest estimated mean since we initialize this value to be very large. This isn't necessarily close to the true mean but rather it's an overestimate of the true mean .

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_28.PNG)

&nbsp;&nbsp;&nbsp;the next step is to consider the part of the code where we choose the Bandit. As I mentioned earlier we don't need to choose anything randomly. We can just act in a greedy manner and choose the bandit with the largest estimated me. The question is why does this even work. Let's think about it. Remember that our goal is to balance exploration and exploitation. Exploration is the same as saying you want to collect lots of data. So what happens with our estimated mean if it's early on in our experiment. Then we haven't collected a lot of data yet. Then our estimated mien will be very large not because the true mean is large but because we set the initial value very large and it has yet to converge to the true meaning. On the other hand after we've collected lots of data the estimated mean is going to get smaller and smaller and smaller until we stopped choosing that bandit. Remember that the sample mean is the arithmetic average of all the samples you collected. So even if you have one extremely large value its effect is going to disappear when you have 1000 or 10000 samples.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_29.PNG)

&nbsp;&nbsp;&nbsp;One interesting question to ask yourself Is this in absolute greedy. We saw that our estimate of the mean for each band converge to the true means. Do you think this will happen with the optimistic initial values method. In fact the answer is No. Remember that since we're using the greedy method there is no guarantee you will collect a large number of samples for any single band. What will happen is if the estimated means for the suboptimal bandits go below the estimated mean for the optimal band we will stop exploring those suboptimal bandits entirely and that's because we're being greedy. So the only result we can expect is that those estimated means are below the optimal band it's estimated mean not that they have converged to their true means in fact we can't even expect the optimal band it to have a good estimate of the true mean because the initial value could have been so high in the number of trials low enough that the estimated mean is still an overestimate. By the end of the experiment.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_30.PNG)

&nbsp;&nbsp;&nbsp;The next question I want to address is what is the role of the initial value. The intuition is hopefully clear by now. It's that if you set this value very high then it will cause the algorithm to explore because the greedy method will believe that the bandit has high mean reward even when it doesn't. To determine the role of the initial value you have to ask the question how high. So if you set the initial value extremely high then you're saying I want more exploration because it's going to take more time for the estimated mean to go down towards its true meaning. If you set the initial value only a little high then you're saying I want just a tiny bit of exploration because it's going to take much less time for the estimated mean to go down towards its true meaning. So the initial value is then a hyper parameter that controls the amount of exploration; high initial values mean more exploration and smaller initial values mean less exploration. But even when you set a small initial value it still should be greater than the typical set of rewards you would get in order for this algorithm to work.


![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_31.PNG)



# Optimistic Initial Values Beginner's Exercise Prompt

[code_4](../code_files/4_optimistic_starter/optimistic_starter.py)



# Optimistic Initial Values Code

[code_5](../code_files/5_optimistic/optimistic.py)



# UCB1 Theory

&nbsp;&nbsp;&nbsp;In this lecture we are going to talk about another method of solving the explore-exploit dilemma called UCB1. UCB stands for upper confidence bound. If you think about the sequence of algorithms we've gone through, I think it kind of makes sense why we go in this order in a very loose way. Each of the ideas takes the previous idea and makes it a little more complex. Epsilon greedy was our first algorithm that said just have a small probability of exploration so that we would never get stuck with an inaccurate maximum likelihood mean estimate. Optimistic initial values takes that a step further by using a more natural kind of exploration instead of just having a random probability of exploration. We just make the mean artificially high so that each bandit gets chosen more often until we learn that the true mean is not actually that high.

In this lecture we'll take that a step further and ask: Is there a way to think about this upper bound in a more probabilistic way? In other words, instead of trying to guess a good upper bound, can we use the rules of probability to infer an upper bound? 

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_32.PNG)

&nbsp;&nbsp;&nbsp;I alluded to the idea of confidence earlier. We want to be confident in our predictions and we know that in order to be confident in our predictions, we should collect lots of data. When we collect more and more data, our confidence in the mean prediction gets higher and higher.

Now you might assume that this leads us naturally to confidence intervals but we're going to go in a different direction. We're going to talk about inequalities later. I will use confidence intervals again to build some intuition but for now let's work through some theory. The basic form of an inequality looks like this. We're going to start with as few mathematical symbols as possible since it can be quite intimidating. So the inequality looks like this: It says the probability that the difference between the sample mean and the true mean is bigger than some error is less than or equal to some function of that error. This function is typically a function that decreases as the value of the error gets larger. That looks pretty complicated by itself, so let's break it down.

First think about why the left side makes sense since we would need to collect an infinite number of samples for a sample mean to equal the true mean; there's going to be some error in our measurement. What do we want to ask? How big is this error? Well, we can phrase this as a probability question: I can ask what's the probability that my error is bigger than some value and can I upper bound that probability? We know the right side is an upper bound because the two sides are related by a less than or equal to sign.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_33.PNG)

&nbsp;&nbsp;&nbsp;Actually, at this point, it probably helps to use an actual variable and a made-up function. Just as an example, we can ask what is the probability that my measurement error is bigger than some value, say T. And just to be clear, T must be positive. So we can say the probability that our measurement error is bigger than T is less than or equal to one over T. Remember, one over T is just an example of a decreasing function. This is not necessarily true but let's think about why this would make sense.

Let's say T is a very small value. In that case, the right side becomes bigger. That makes sense because the probability that my error is bigger than a very tiny value should get larger as that tiny value gets smaller. Conversely, let's say T is a very large value. That also makes sense because the probability that my error is bigger than a very large value should get smaller as T gets larger. In other words, the probability of being larger than a large error is smaller and the probability of being larger than a small error is larger.

So to summarize, we want to ask what is the probability that my error is bigger than some T. And it turns out we can upper bound this probability as a decreasing function of T

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_34.PNG)

&nbsp;&nbsp;&nbsp;In fact, when you have a function on the right-hand side that decreases proportionally to one over T, that's the mark of inequality. Yes, that's the same mark I will be talking about later when we talk about Markov decision processes. As you may have learned by now, Markov is a ubiquitous name in the field of probability and many fields that make use of it.

There is another inequality called the Chebyshev inequality that decreases proportionally to one over T squared. This would be considered better since the function on the right side decreases faster so we can guarantee that the error is below an even smaller number. Finally, we get to Hoeffding's inequality which is an even tighter bound. It decreases exponentially in T squared—that's like a gasping curve which decreases faster than any polynomial.

The reason I'm showing you all the individual variables for the Hoeffding inequality is because this is the one we're actually going to use for UCB1. In any case, I would consider the math behind the UCB1 algorithm to be optional for this course. Since while the math is kind of tricky, the algorithm itself is pretty easy to implement. So if you don't feel comfortable with this math, consider simply ignoring it and just implementing the algorithm.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_35.PNG)

&nbsp;&nbsp;&nbsp;It may be useful to try to understand all of the symbols in this inequality. But again, this is optional and we're not really going to make use of it. This is just for your own understanding. So let's look a little more closely at each item.  
First Xn  is the sample mean of X after we've collected n samples. E[X] s the expected value of X. In other words, it's the true mean. So Xn - E[X] is the error in our measurement of E[X]. T is some arbitrary error value. Well, we can tell from this that as we collect more and more samples the error gets smaller and smaller since the exponential function gets smaller as n increases. So if we use this as a basic sanity check, everything seems good so far.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_36.PNG)

&nbsp;&nbsp;&nbsp;But again, that was just for some extra intuition. In fact, I'm going to take this rare opportunity to skip over the math completely. Basically, what's going to happen is you're going to do a few probability manipulations and after a bunch of hard work you're only going to end up choosing your own heuristic anyway. Heuristic basically means just pick some function that seems to make sense but doesn't have any foundation based on first principles. So it kind of doesn't make sense to go through a lot of principled probability calculations when in the end you just end up picking a function at random. It's basically a hyperparameter. The specific hyperparameter that we use is what makes this method UCB1. There are other kinds of UCB that are less popular and so are outside the scope of this course.

If you want to look at the math behind UCB1 in depth, you're encouraged to check out the paper titled "Finite-Time Analysis of the Multi-Armed Bandit Problem," which you can find as extra reading (not 60) in the course repo. So let's look at how it works and then we can talk about why it makes sense.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_37.PNG)

&nbsp;&nbsp;&nbsp;Basically, the idea is this: looking at the pseudocode should be helpful since we've seen other bandit algorithms before and they all just follow the same basic pattern. So inside a loop we choose using a greedy algorithm based on the sum of these two terms. The first term is the sample mean on bandit 
j
j. The second term is an error upper bound. We'll discuss where this formula comes from later. It's just like the optimistic initial values method except that instead of using an optimistic estimate for the mean, we use the actual sample mean plus some upper bound on the error.

If you want, you can think of it as using the upper bound on the confidence interval as intuition, as you can see. This is still greedy with respect to the upper bound.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_38.PNG)

&nbsp;&nbsp;&nbsp;So first let's just think about the intuition in terms of confidence intervals. Even though we know that's not exactly what we're doing, why would using the upper bound on the confidence interval work in the first place?

As discussed, we're still going to act in a greedy manner with respect to this upper bound. This is still similar to how we use optimistic initial values. And so there are two cases to consider. The first case is where we haven't collected a lot of samples yet, so our estimate is bad and our confidence interval is large. In that case, I want to explore this bandit so that I can collect more samples. Using the upper bound of the confidence interval would be useful since it would be very high. And if I take the bandit with the maximum upper bound then I can explore this band.

In the second case, I've collected lots of samples so my estimate is very accurate and I no longer need to explore this band. In that case, the only way I can explore this band is if its true mean is actually high and is higher than the upper bounds on other bands. So I hope that's intuitive. Using the upper bound of a confidence interval will allow you to explore and exploit in a reasonable way.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_39.PNG)

&nbsp;&nbsp;&nbsp;Now let's look at how UCB1 in particular implements this strategy. Let's focus on the first term: the sample mean. If we only look at this, how it works is obvious. If the sample mean is bigger, it makes this bandit more likely to be chosen, which is what we want. This would be the exploitation aspect. How about the second term? At UCB1, the upper bound for bandit j is given by the sample mean of bandit j plus the square root of 2 x log(n/nj). Let's look at each of the terms inside the square root. It's important to differentiate between a big N and little nj. Big N represents the total number of plays we have made so far. So if we played three bandits once each, big N would be three. On the other hand, little nj represents the number of times we played bandit j only. So if we played all three bandits once each, then little nj would be one for each of the bandits. Finally, I want to point out this strange constant 2. In fact, this doesn't come from any probability derivation. This is just the hyperparameter. As you recall, I said that this is a heuristic. So if you made this constant bigger, then it would give you a larger upper bound, and if you made it smaller, then it would give you a smaller upper bound.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_40.PNG)

&nbsp;&nbsp;&nbsp;The next question to consider is why does this even work? Let's consider what happens to big N and little nj. Let's say I ignore bandit j for a long time so that little nj is very small. Then big N will become larger and eventually the numerator will become bigger than the denominator. And this will make the upper bound large. Then I will choose bandit j because its upper bound is large, larger than all the other choices.  
On the other hand, let's say I have explored bandit j already so that little nj is large. Big N may be large too but its effect on the upper bound is muted because of the log function. As you recall, the log function grows much more slowly than linear. So let's say you played bandit j one thousand times and you only played bandit j all of those times. Then you get  log1000/1000×2, which is approximately equal to 0.01.  
So as you can see, as these values grow, the denominator overtakes the numerator and the upper bound shrinks down to zero and all you're left with is the actual means, which is what you want. That makes sense because after you collected lots of data your estimates are accurate and there's no need to explore further. In general, the limit of log(n/n) as n approaches infinity is zero.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_41.PNG)

&nbsp;&nbsp;&nbsp;Although I said earlier that I consider all the math to be optional, I do want to consider the question: where does this upper bound come from? Intuitively, you can take the right side of the Hoeffding inequality and realize that if you take the log of both sides and solve for t, you get the square root of the log divided by nj, the number of samples collected. We can just set this upper bound to be some letter called P just so we can give it a name, UCB1. It just says that as a heuristic, let's take the numerator to be 4logN, which means that we want P to be N^-4 . In other words, we want that probability upper bound to drop off as one divided by N^4

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_42.PNG)

&nbsp;&nbsp;&nbsp;So finally I want to discuss one small detail about the pseudocode that you may have missed. Our upper bound contains the ratio log n divided by NJ But what happens if NJ equals the zero. And on top of that what if Big N is also zero. I've actually seen a few ways to hack around this one method that actually makes sense is to just consider zero on the denominator with a positive numerator. As a calculus limit in that case your upper bound is infinity and therefore you are guaranteed to select this bandit. Of course you have to ignore the first few values since log of zero over zero is minus infinity and then log of 1 over zero is zero or zero. But that would only be on the first few iterations. Instead I found that what the authors did in their original paper was the simplest solution. It says that there is an initialization step for the algorithm where you just play all the bandits once then you're big n that just starts out as the number of bandits and NJ is just one for each band.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_43.PNG)



# UCB1 Beginner's Exercise Prompt

[code_6](../code_files/6_ucb1_starter/ucb1_starter.py)



# UCB1 Code

[code_7](../code_files/7_ucb1/ucb1.py)



# Bayesian Bandits  Thompson Sampling Theory

&nbsp;&nbsp;&nbsp;In this lecture we are going to look at a new algorithm that makes use of Bayesian statistics. Some people like to refer to this algorithm as the Bayesian bandit's algorithm. To begin this discussion, we want to recall the digression I made into confidence intervals. The confidence interval is a nice intuitive tool for us because even though we're not going to actually use it, it provides us with a nice picture. It kind of exemplifies the explore-exploit dilemma: when we have only a small amount of data, the confidence interval is large, and when we have a large amount of data, the confidence interval is small. When the confidence interval is fat, that means we should explore more. When the confidence interval is skinny, that means we should explore less; we should exploit. When the confidence interval is skinny and has a high value. What's good about the confidence interval is that it tells us in a sort of roundabout way where the true mean could possibly be. If we look at this fat confidence interval, that means the true mean could be here or it could be over here because these areas have probability mass. These are not improbable locations where one might find the true mean.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_44.PNG)

&nbsp;&nbsp;&nbsp;But let's ask ourselves a question: why is the confidence interval symmetric? Why does it always have this bell-shaped curve? In fact, that's because confidence intervals are based on the central limit theorem, which says that sums of random variables tend to a normal distribution. Since this lecture is about the Bayesian approach, we are not going to use confidence intervals because that's the classical frequentist approach. However, the concept of confidence intervals gives us intuition. What we really want when we look at a graph like this is the distribution of the true mean. Bayesian machine learning gives us the tools we need to calculate this because in the Bayesian paradigm everything is a random variable—even the parameters of distributions. That means whereas before we said that the reward came from some distribution with some mean, now we are seeing that mean also comes from some other distribution since everything is a random variable. Everything has a distribution.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_45.PNG)

&nbsp;&nbsp;&nbsp;In order to determine the distribution of the mean, which we're going to call theta, we have to structure the problem in terms of a Bayesian statistics problem. The quantity we're looking for is p(theta | X), where theta is the mean of the Bernoulli random variable X and the X inside this expression refers to the data we've collected. For convenience, we'll conflate the two but realize that these are overloaded symbols. When I use capital X, I could be referring to the random variable or I could be referring to the data I've collected. Just pay attention to the context and you shouldn't have any issues.

Of course, the place we start from in Bayesian statistics is Bayes' rule. On the left-hand side, we have p(theta | X), which is a distribution we call the posterior. On the right, we have three items: p(X | theta), called the likelihood—the same likelihood you would use in maximum likelihood estimation. We can interpret that as the probability of the data given the parameter theta. p(theta) by itself is called the prior. It's the distribution of theta when we don't know anything about X, or in other words, when we haven't collected any data. p(X) in the denominator is called the evidence. Since we're trying to find p(theta | X), which is a distribution over the random variable theta, it turns out that p(X) is constant with respect to theta and therefore we can write this as a proportionality instead of an equation.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_46.PNG)

&nbsp;&nbsp;&nbsp;So why would we want to get rid of the evidence and turn this into a proportionality? Well, in general, we don't know this denominator and it's intractable or infeasible to calculate. As you recall, we can express the denominator as an integral over the numerator since they both express a joint probability over X and theta. Since theta is a continuous random variable, we integrate instead of summing. The problem is, if you remember from your calculus studies, that integration is very hard. It's not just a matter of mechanically applying a set of rules like differentiation. As a side note, some students taking this course may have heard of Monte Carlo methods as a way to approximate this integral. However, as you know, these methods are designed to run in real time and therefore it's also not feasible to run a Monte Carlo simulation to obtain an answer.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_47.PNG)

&nbsp;&nbsp;&nbsp;The trick in Bayesian statistics is there are special pairs of distributions where we can take advantage of the proportionality and ignore the evidence. These are called conjugate pairs, and in this context, the prior would be called a conjugate prior. The basic story is this: in probability, we pretty much use a fixed set of common distributions. We have the Gaussian, the binomial, the Poisson, and so forth. In general, the posterior doesn't fit nicely into one of these common distributions. For example, I can't say if my likelihood is a Gaussian and my prior is a uniform, then my posterior will be a Gaussian—that won't work. However, conjugate priors are special because when you combine the prior and the likelihood to get the posterior, the posterior comes from the same kind of distribution as the prior. So if your prior is a Gaussian, then your posterior will also be a Gaussian. This is contingent on the fact that your likelihood matches the prior such that they are conjugate. So you can't pick any or all likelihoods. This only works for certain distributions.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_48.PNG)

&nbsp;&nbsp;&nbsp;So what distributions are we interested in? As you know, our likelihood is a Bernoulli given a set of coin tosses X1 up to n. We can express the likelihood as the product of p(x) for each x. In this instance, we are using theta to represent the Bernoulli parameter. So if we plug this into the PMF for the Bernoulli, we get theta to the power of x times (1 minus theta) to the power of (1 minus x).

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_49.PNG)

&nbsp;&nbsp;&nbsp;Well, it turns out that if we choose our prior to be the beta distribution, this is a conjugate prior for the Bernoulli likelihood. In the next few slides, we are going to show that that's the case. By the way, just so that the beta doesn't seem like a completely arbitrary choice, it does make sense. We know that in a win or lose situation where the reward is only binary, the mean of that distribution must be a number between 0 and 1. It turns out that the support of the beta distribution is in the range 0 to 1. So that checks out.

We can start by writing down the numerator of the posterior, which is the joint distribution between theta and x, and the expression for the beta distribution. We have two parameters, alpha and beta. These are the parameters of the beta distribution. The B function is called the beta function and it's equal to gamma of alpha times gamma of beta divided by gamma of alpha plus beta. Gamma itself is a special function which turns out to be a fancy integral. But basically, you can think of it as a generalization of the factorial function for non-integer numbers. In actuality, the gamma function is defined for both real and complex numbers, although that would be outside the scope of this course. In any case, we actually never have to worry about computing the beta function as you'll soon see.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_50.PNG)

&nbsp;&nbsp;&nbsp;So why do we like expressions like this in Bayesian machine learning? Well, if you look closely, we see that both theta and 1 minus theta appear in the base of both the prior and the likelihood. In addition, since the beta function is constant with respect to theta, it can be dropped out of the proportionality. To make this clearer, we can first bring the product into the exponent and turn it into a sum. So we get the sum over x_i and the sum over 1 minus x_i. Then we can combine all the theta terms and all the one minus theta terms until we just get a single theta term and a single one minus theta term.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_51.PNG)

&nbsp;&nbsp;&nbsp;But here's the trick: as you can see, this posterior is in exactly the same form as a beta distribution, which, as you recall, is the same kind of distribution we chose for the prior. This is because the beta distribution has the form constant times theta to the power alpha minus one times one minus theta to the power beta minus one. We never have to worry about what that constant actually is since it's just whatever value it needs to be so that the PDF integrates to 1. So unless for some reason you need to compute that value, its actual value is unnecessary.

In conclusion, we can say that the posterior for theta given some dataset X is a beta distribution with parameters alpha plus the sum of X and beta plus n minus the sum of X. This is contingent on the fact that the prior is a beta with parameters alpha and beta and that the likelihood is a Bernoulli.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_52.PNG)

&nbsp;&nbsp;&nbsp;One part of the process that we can't forget about in Bayesian machine learning is how to choose the value of alpha and beta. In the first place, this defines the shape of our prior distribution. Although there are many interesting shapes the beta distribution can have, we are fortunate that the beta distribution is expressive enough to give us something that makes a lot of sense, and that is the uniform distribution: Beta(1,1) just happens to be a uniform distribution. And this usually makes a good choice for the beta prior. It says that we have no clue what the result may be, and so we assign equal probability to every possible value.

If you come from an industry where you do actually have prior knowledge, then you should make use of that knowledge. For example, we know that click-through rates on ads are usually very small, around 1 percent or 2 percent. So if you have that knowledge due to domain expertise, then it should be encoded into your prior.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_53.PNG)

&nbsp;&nbsp;&nbsp;One minor point of confusion for students is how to update the posterior when it comes to the actual bandit problem. Recall that in the bandit problem we update our model after every sample X is collected. So unlike in our theoretical calculation where we have many samples, we always just have one sample. Of course, over the course of an experiment, we may collect many samples. The trick is that in Bayesian machine learning, what you consider the posterior in one step actually becomes the prior in the next step.

So here's an example of how we can do this update over several steps. We start with a prior Beta(1,1), the uniform distribution. Next, we pull the arm and we get X equals 1. The posterior therefore is Beta(1+1, 1+1-1), which is Beta(2,1). On the next pull, Beta(2,1) becomes the prior. Now let's say we pull one again, so X equals 1. Then our new posterior is Beta(2+1, 1+1-1), which is Beta(3,1). So this is our new posterior, but on the next step, Beta(3,1) becomes the prior. So let's say on the next pull we get X equals zero. Then our posterior is now Beta(3+0, 1+1-0), which is Beta(3,2).

So just keep this in mind when you're coding that in Bayesian statistics and Bayesian machine learning, we usually define the posterior in terms of several samples, while in applications with online updating, usually we're computing the posterior in terms of a single sample.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_54.PNG)



&nbsp;&nbsp;&nbsp;In this lecture we are going to continue our discussion of the Bayesian bandit algorithm. Previously we covered the fundamentals such as conjugate priors and how to update the prior to obtain the posterior after collecting data. In this lecture, we are going to discuss how to actually use this in an algorithm.

To start, we're going to again return to our intuitive picture of confidence intervals, except now we're not going to use confidence intervals anymore. Instead, now that you know about posteriors in the Bayesian paradigm, we can plot the exact posterior and come to the same conclusions. As you know, this posterior represents our belief about the distribution of theta, the mean of a bandit. Theoretically, theta could be anywhere in this range, although obviously the areas with more probability mass are more probable.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_55.PNG)

&nbsp;&nbsp;&nbsp;The Bayesian method involves a different strategy than what we previously used, which was basically to use an upper bound. Instead, what we are now going to do is simply draw a sample from this distribution. This method is also called Thompson sampling. I think it actually makes a lot of sense once you think about it. What is a distribution in the first place? It tells you what values a random variable is likely to take on by drawing samples from this distribution. We're saying give me a value from this distribution and let that determine which band we choose instead of just using one value which is the upper bound. We can use all of its values by drawing samples. As we draw more and more samples, this distribution will become skinnier and skinnier as we get more and more confident in our belief of where the true mean lies. When we draw a sample from a very skinny distribution, we're going to get a value very close to the center and it will be as if we were just comparing each bandit by their actual means.

If you don't understand this right away, we'll be looking at the same idea a few more times from a variety of perspectives. Just remember the main fact, which is that instead of using some kind of upper bound, we pick randomly from any value that the mean can take on according to the posterior distribution.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_56.PNG)

&nbsp;&nbsp;&nbsp;The pseudocode is another perspective that I think makes the idea clear. Inside the band class, we define a new function called sample which just returns a sample from the beta distribution given by its current values of A and B. I use a and b here instead of alpha and beta since normally in programming we use ASCII characters. As you can see, when we choose our band, if we take the argmax with respect to the sample, this is opposed to our previous algorithms where we took the argmax with respect to an upper bound. It's like saying be greedy but with respect to samples from the posterior rather than some statistic estimated from the samples.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_57.PNG)

&nbsp;&nbsp;&nbsp;The next thing I think is useful to do is to look at graphs of the posterior distributions and reason about how they will change as we collect our samples. Let's start by looking at a common scenario where we have one skinny posterior and one fat posterior. With the skinny posterior, when we sample from this distribution, the range of values we can get is pretty narrow. For the fat distribution, when we sample, we can potentially get a lot of different values. As you can see, there is some chance of the sample from the fat distribution to be greater than the sample from the skinny distribution, but there's also a decent chance of the sample from the fat distribution to be less than the sample from the skinny distribution.

Let's suppose that we draw a sample from each band and that the sample from the fat distribution turns out to be larger. Since the fat distribution gave us a larger sample, that means we are now going to pull that bandit's arm. So let's say we play that band and we win so that we get X equals 1.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_58.PNG)

&nbsp;&nbsp;&nbsp;Then when we update our fat distribution, two things happen. First, it gets a little skinnier because we become more confident in our mean estimate. In addition, its peak moves up a bit since getting a one increases the mean.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_59.PNG)

&nbsp;&nbsp;&nbsp;Next, let's consider the situation where we sample from the fat distribution and it turns out to be larger, but when we pull the bandit's arm we get X equals zero.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_60.PNG)

&nbsp;&nbsp;&nbsp;In this case, two things happen. First, it still gets a little skinnier because whether we win or lose, we still obtain a sample and therefore we become more confident in our mean estimate. But instead of the peak moving up, now the peak was down since a zero would decrease the mean.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_61.PNG)

&nbsp;&nbsp;&nbsp;Let's consider another scenario where we again have a fat bandit and a skinny bandit, but this time the fat bandit's distribution is such that most of the probability mass is less than where the skinny bandit's distribution is. What happens when we draw a sample? Well, it doesn't matter what we draw for the fat bandit because most of those samples will be less than the sample from the skinny band and therefore we won't end up playing that arm very often. And that's a good thing. Why is that a good thing? There are two things to pay attention to. First, its mean, and second, its fatness. As you can see, its mean is low. Therefore, we don't want to play this bandit because it's suboptimal and doesn't yield a reward as often as the skinny band. Second, because it's fat, that means we have low confidence in our estimate, which also means we haven't collected a lot of data on this band. And that's a good thing. Why is that a good thing again? Because it's a suboptimal band, so we don't actually want to play this band. So in this situation, Thompson sampling is protecting us from playing that band. And we don't actually want to play it because it's suboptimal. Compare that to epsilon-greedy, where we would continue to play that band anyway since our choice would be uniform random.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_62.PNG)

&nbsp;&nbsp;&nbsp;To solidify these concepts, we're going to look at a demo of the Bayesian method in action. You'll also get to code this yourself. So this is a preview of what you will be making. This is the same script we'll be looking at later. So I'm kind of presenting it in reverse order, and what we usually do is to look at the results before looking at the code.

So if I run this script, here's what I would get at the fifth iteration. As you can see, the 0.2 bandit has one zero out of two times, the 0.5 bandit has one zero one time, and the 0.75 bandit has one two out of two times. And this leads to the distributions on the mean that you see. For the 0.2 bandit, more probability mass is concentrated near the zero side. For the 0.5 bandit, probability mass is concentrated near the zero side as well, but this is more pronounced for the 0.2 bandit because it has lost more times and therefore we're more confident that its mean is closer to zero.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_63.PNG)

&nbsp;&nbsp;&nbsp;Here's the distribution after ten trials. As you can see, the 0.2 bandit still only has zero out of two wins. That means in the last five trials it was never selected. That makes sense since sampling from a distribution where most of the probability mass is near zero will give you a smaller number, and since the samples were smaller, we didn't select that bandit. We can see that both the 0.5 bandit and the 0.75 bandit have been updated. The 0.5 bandit has won one, and the 0.75 bandit has now lost. That changes their distributions to now look more like bumps rather than monotone quickly increasing or decreasing slides.

So why do we get bumps instead of slides? Let's take the 0.75 bandit for example. Before, most of the probability mass was at the value one because we had only ever gotten ones in the data. But now that we've gotten a zero, the probability that the mean is truly one is zero. That's because if the mean was 100 percent, then we should win 100 percent of the time. So the Bayesian update is very logical. Previously, we believed that the mean could possibly be 100 percent, but now that we've lost, we know that the mean being 100 percent is impossible. The same thing happened to the 0.5 bandit. Most of its probability mass was at zero percent because we only ever lost. But now that we've won, we know that the probability of the win rate for that bandit cannot possibly be 0 percent. That is now an impossible inference. The probability for the 0.5 bandit and the 0.75 bandit both go down to zero at zero and one because if we can win and we can lose, then we know that those win rates are impossible.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_64.PNG)

&nbsp;&nbsp;&nbsp;Now we see the distribution at 20 trials. As you can see, most of the probability mass for the optimal bandit is concentrated much higher than the mass for the other two bands. So when we draw samples from these distributions, the optimal bandit gets elected a lot more often. It's still not impossible, but it's getting more and more unlikely. The count on the number of times the optimal bandit was selected is growing the fastest, and the worst bandit still has not been selected.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_65.PNG)

&nbsp;&nbsp;&nbsp;Here's the distribution at 50 trials. Pretty much the same story as at 20 trials. You can see that for the optimal bandit, the distribution is getting skinnier and taller because more of its probability mass is being centered around the true mean. We are becoming more confident in that estimate as we collect more data. On the other hand, our estimates for the other bandits are still not confident, and that's a good thing because they are suboptimal.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_66.PNG)

&nbsp;&nbsp;&nbsp;Here's the distribution at 100 trials. Again more of the same pattern.

At 200 trials we see something a little interesting. Although the bandit distribution generally still has the same shape, we see that the worst bandit has been selected one more time. Its win rate is now zero out of three. But keep in mind it was only selected once out of 100 times, so it just so happened that one set of those 100 times the sample that we got from the 0.2 bandit was higher than the samples from the other bandits. However, since we lost again, its distribution is now more peaked around zero and we will be less likely to pick it again in the future.

At 500 trials we essentially see the same thing. The 0.75 bandit gets played a lot more than the 0.5 bandit, which gets played a bit, and surprisingly even the 0.2 bandit gets played once. However, notice that the probability of being selected is much lower. Before we chose it 1 out of 100 times, but in between the last plot and this plot we played 300 times, so now it's become 1 out of 300.

Now we're at 1000 trials. Again the 0.75 bandit is played most often, the 0.5 bandit gets played a bit, and even the 0.2 bandit was played twice. However, notice that we ended up winning one of those times, which eliminates the possibility of its win rate being zero. So now even this distribution turns from a slide into a bump. Notice that the 0.75 bandit has a very tall and very skinny distribution at this point, and the other two bandits remain short and fat.

Let's look at the number of times the suboptimal bandits were played so that we can compare them to the next plot. So the 0.2 bandit has been played six times and the 0.5 bandit has been played twenty-five times.

Here we are at 1500 trials. We can see that the 0.2 bandit has not been played any times in the past 500 trials, and the 0.5 bandit has been played once. This would be the correct thing to do since those bandits are suboptimal, and now we are pretty confident of this fact given our posterior distributions.

This is our final plot at 1999 trials. As expected, the posterior distribution for the 0.75 bandit has gotten even taller and even skinnier, and this bandit has been played for a large majority of the last few hundred trials. Interestingly, we see that the 0.2 bandit played once more even though the 0.5 bandit didn't.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_67.PNG)

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_68.PNG)

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_69.PNG)

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_70.PNG)

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_71.PNG)

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_72.PNG)

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_73.PNG)

&nbsp;&nbsp;&nbsp;Let's summarize the Thompson sampling method. While I think it's very intuitive, it also has the most theory out of all the bandit algorithms. We started with the intuitive idea that we're interested in something like the confidence interval of our win rate estimate. This perfectly encapsulates the explore-exploit dilemma. When the confidence interval is fat, we want to explore to improve our confidence interval. When confidence intervals are small, we want to exploit this fact by choosing the band with the highest mean which we are now confident about. But confidence intervals are based on the central limit theorem, and they do not accurately portray the true distribution of the bandit win rates. Instead, the Bayesian method is to treat the win rate as a random variable, which is to give it its own distribution. In general, computing a posterior from Bayes' rule is not easy because they usually involve intractable sums or unsolvable integrals. We use conjugate priors to show that instead of calculating the posterior by hand, we can instead use proportionality to prove that the shape of the posterior fits some particular distribution. And from there, the normalizing constant can be found since the integral of any distribution must equal one.

Next, we introduce the Thompson sampling algorithm, which says that in order to choose a bandit, just rank each band based on samples drawn from their posterior. As we saw, over time this does exactly what we want. When distributions are fat, we explore more, and when distributions are skinny, we explore less. But importantly, when the optimal distribution becomes skinny, we can leave the suboptimal distributions fat since in this scenario the optimal bandit still usually has the highest sample. This leads to us choosing the optimal band and more, which is how we exploit.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_74.PNG)

&nbsp;&nbsp;&nbsp;One final question I want to answer is: out of all these methods we discussed, which one should you use in practice? They all seem equally easy to implement, and only the algorithms and reasoning behind them are different. It all comes down to my rule: machine learning is experimentation, not philosophy. In order to choose the best algorithm, you should experiment and collect data so that you have a definitive answer for your particular dataset. You don't want to do something like say such and such works better for BuzzFeed; therefore, we think it will also work better for us. What if your problem looks nothing like BuzzFeed's problem? But that's not to say that if it works for BuzzFeed, it won't be a useful data point. It certainly is, and it does give us more confidence that it will work for us.

And keep in mind that while we were doing a very simple simulation in this class, real-world problems may have hundreds or thousands of choices. When the dimensionality of the problem increases, that could possibly change the characteristics of these algorithms. On the other hand, because bandit algorithms are so simple to implement and so popular, we can draw on the experiences of many other companies in the industry. So it's good to use the experiences of others in aggregate. All this is to say that Thompson sampling seems to be the winner in many experiments done by those in the industry. So that's why we've been building up our Bayesian algorithms in order to eventually get to this point.

At the same time, in reinforcement learning, algorithms are usually discussed in the context of using epsilon-greedy for balancing the explore-exploit trade-off. So just keep that in mind while you could apply these algorithms to the techniques we'll discuss in the future, it's not conventional.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_75.PNG)



# Thompson Sampling Beginner's Exercise Prompt

[code_8](../code_files/8_bayesian_starter/bayesian_starter.py)



# Thompson Sampling Code

[code_9](../code_files/9_bayesian_bandit/bayesian_bandit.py)



# Thompson Sampling With Gaussian Reward Theory

&nbsp;&nbsp;&nbsp;In this lecture, we are going to extend our application of the Thompson sampling method to real value reward signals. Previously, we looked at the scenario where you can only win or lose. But what if the reward comes from a different distribution, such as a Gaussian? That is the scenario we're going to look at in this lecture. Keep in mind that there are other possible distributions you could use as well, such as the person distribution or the gamma distribution. However, I think once you know the main principle, it's easy to extend it to different kinds of distributions. The only requirement is that you have a conjugate prior.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_76.PNG)

&nbsp;&nbsp;&nbsp;So let's start with the Gaussian likelihood, given some mean in some precision, how we can write the likelihood as follows, notice that I'm not using the typical Sigma squared for the variance, since it is usually more convenient and therefore customary to use the precision in Bayesian machine learning. The precision is just one of the variance. So if you ever want to know what the variance is, just take one over tau. So where you would usually see two Pi Sigma squared in the denominator of the coefficient. Now you see the square root of tau over two pi and in the exponent, instead of seeing two sigma squared in the denominator, we now see tau over two.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_77.PNG)

&nbsp;&nbsp;&nbsp;Now, one question you might have is, how do we actually find conjugate Pryors like how do we know the banally goes with the beta? Luckily, people have already compiled tables for us, so we can just look them up, for example, on Wikipedia or your favorite Bayesian statistics textbook. It turns out that for the Gaussian, there are a few possible variations, since the Yasiin has two parameters MU and Tau, instead of just a single parameter that the MINOLI has, we can potentially have a very complicated prior. But in fact, treating both MU and Tower's distributions is only one possibility. It's also possible to assume that Tau is known so that you only have to find MU, and it's possible to assume that MU is known so that you only have to find tau. In the case where both MU and tower unknown, the conjugate prior is a normal gamma distribution. This is a joint distribution on MU Intel. In the case where only MU is known, the conjugate prior is a gamma distribution. In the case where only tau is known, the conjugate prior is just a normal distribution. For this course we will be interested only in the case where the mean is unknown, but the precision is known. If you want, I would recommend doing similar derivations for the other cases on your own as an exercise.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_78.PNG)

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_79.PNG)

&nbsp;&nbsp;&nbsp;Given that we're going to ignore tão so that the only posterior distribution we're worried about is Mbewe, how many different posterior parameters are we interested in finding? I'll give you a minute to think about this, or you can pause the video. And so you think you have the answer. In fact, the answer is to because Mbewe is assumed to come from a Gaussian distribution, since that is the conjugate prior, Mbewe will have two parameters its own mean and its own precision. Note that it's important not to confuse the mean and precision of Mbewe with the mean and precision of X. That might be confusing because they are both Gaussian. So the way we can write it is X comes from a distribution with mean mu and precision tau. But Mu comes from a different normal distribution with mean M and precision lambda. So don't get these confused. As a side note, if we create both Mew and Tau as random variables, then we would have four parameters since the normal gamma has four parameters.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_80.PNG)

&nbsp;&nbsp;&nbsp;Before we start doing any math, it's helpful to ask, what do we actually need to find at this point? Remember that in general, the Thompson sampling algorithm remains the same regardless of what distributions you use. So the structure of the code will not change. The only thing we need to solve in this lecture is how do we calculate the posterior parameters from the prior parameters. In other words, let's say we start with prior parameters M zero and Lambda zero. Our goal that is defined M and lambda the parameters of the posterior distribution of MU as a function of the data X and the prior parameters zero and lambda zero. So that's what we want to do, find some expression for the posterior parameters that we can plug into our code. But the actual code itself is largely the same. And just to make things less ambiguous, we differentiate between the posterior parameters and the parameters by adding a subscript. So the prior parameters are zero and lambda zero, while the posterior parameters will just be M and lambda.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_81.PNG)

&nbsp;&nbsp;&nbsp;We're going to start with our usual statement that the posterior is proportional to the joint, which is the likelihood at times the prior note that I've dropped the precision of X from the distribution's, since it is assumed to be a fixed number, then we can plug in the expressions for these distributions. Immediately, I know the next step is to expand the product over I from one to end, this gives us the square root of tau over two pi to the power end, which is irrelevant since it's a constant. And for the exponent term, the products can be brought up into the exponent where it becomes a sum.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_82.PNG)

&nbsp;&nbsp;&nbsp;In the next line, we can simply drop all of the coefficient terms because we're interested only in the shape of the distribution, you might think that LAMDA shouldn't be dropped because the posterior depends on LAMDA, but in fact, we are only interested in terms that depend on itself in the next line. We combine the exponents into one big exponent in the next line and we expand the squares. The next step will be to collect all the like terms. So if you want to pause and write all of this down, I would strongly recommend doing so.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_83.PNG)

&nbsp;&nbsp;&nbsp;So in the first line here, I've just repeated what we had on the previous slide, except now I use XP notation rather than putting all the relevant stuff in the exponent to make things more readable. In the next line, I expand the summation so we get end Times Square minus two MUE times the sum of X plus sum of X squared. From there. We have to remember again that we don't care about any terms that don't involve HMU so we can drop the X squared term and the M0 square term. In the following step, I'm going to do something that might seem a bit strange, but I'm going to collect like terms. I want to collect all the terms that involve me square together and all the terms that involve MUE together.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_84.PNG)

&nbsp;&nbsp;&nbsp;So why do we want to collect, like, terms with respect to Mbewe, let's remember that Mbewe comes from a normal distribution, as you recall, the posterior distribution, bew, given X as mean M and precision lamda. Well, if I were to write out this distribution and ignore everything except the exponent, I can do a similar thing where I expand the square and collect like terms. If I drop the coefficient and the squirter and just say it's proportional, I end up with a very similar expression to what we had before. I have a squared term and I have a midterm.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_85.PNG)

&nbsp;&nbsp;&nbsp;But this is exactly what we had before. In other words, what this is telling us is in the posterior distribution we found before the coefficient in front of you square is the posterior lambda and the coefficient in front of Mbewe is the posterior M times lambda. We can rearrange the second expression to Sofra M so that Lambda goes on the other side. Or alternatively we can replace Lambda with tau times N plus lambda zero. Either way is fine.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_86.PNG)

&nbsp;&nbsp;&nbsp;Now, let's look at these carefully to determine whether or not our answer makes sense. First, consider lamda the precision. This tells us that as we collect more and more data and approaches infinity and therefore LAMDA will also approach infinity, that makes sense because as the variance shrinks, the precision increases and the Gaussian bell curve, it turns into a spike. Looking at the posterior for the mean is also interesting. We see that as an approaches infinity. This expression will actually approach the sum of excise over Overeem, which is exactly the sample mean. Therefore, this also makes sense. It says that as you collect more and more data, the sample mean and the posterior mean actually both converge to the same value, which is the true meaning.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_87.PNG)

&nbsp;&nbsp;&nbsp;Let's summarize what we just did since it was a little long. First, we recognize that instead of newly distributed rewards, we can apply the Thomson sampling approach to any kind of distribution. We noted that if we ever want to look up conjugate priors, we can simply use Wikipedia or your favorite baozi machine learning textbook. And so that gives us a selection of possible distributions we can use. Next, for our example, we chose the Gaussian likelihood with a fixed position Tiao. We realized that four times in sampling the algorithm is the same regardless of the distribution. So the only thing in this lecture that we really need to discuss is how to calculate the posterior parameters for the likelihood mean mu. Once we have that, we are ready to implement our algorithm as an exercise. Recall that when we implement this in code we will not have a batch of end samples whenever we update our posterior, but rather we'll update our posterior after collecting a single sample. Then the posterior in one step becomes the prior in the next step. So something you want to think about is what do these formulas look like when we update after collecting a single sample instead of N samples?

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_88.PNG)

&nbsp;&nbsp;&nbsp;This will be the next exercise, which you should do before watching the next lecture, which will reveal the answer in this exercise, you should implement Thompson sampling for a Gaussian distributed reward with fixed precision for convenience. You can set the precision to one. Don't forget that in addition to updating the posterior parameters of the model, you will also have to make sure that the poll function samples from an actual Gaussian distribution. You can set the true means to whatever values you feel like and test your algorithm to make sure that it works. Good luck and I'll see you in the next lecture.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_89.PNG)



# Thompson Sampling With Gaussian Reward Code

[code_10](../code_files/10_bayesian_normal/bayesian_normal.py)



# Exercise on Gaussian Rewards

&nbsp;&nbsp;&nbsp;In this lecture you will be assigned the next exercise for this course. This exercise was inspired by a question I got from a student on the forum on my website. The exercise goes like this. Take the Bayesian Bandit Code for Gaussian rewards. Currently, the true mean rewards are just one, two and three. That is to say the rewards are Gaussian distributed, and those Gaussians have true means one, two and three. Remember that our algorithm does not know these values. But what if we change the true means to be five, ten and 20 instead? Your exercise is to make this work. Note that if you just take the code and replace the list containing one, two and three with five, ten and 20, this will not work. The code will often converge to a suboptimal choice. Your exercise is to consider why this is the case and to make the necessary changes to fix the issue. As a small hint, consider what assumptions we have to make when we're using the Bayesian method and how the result you get may be sensitive to those assumptions.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_90.PNG)



# Why don't we just use a library

&nbsp;&nbsp;&nbsp;In this lecture we are going to discuss a practical matter. We're going to cover a question I get very often from beginners which is why do we have to do all this programming and math. Why can't we just use a library. I often hear that in order to be so-called practical one must use libraries. Now first let's start with being practical is a great thing. Putting all this theory into practice is obviously the end goal. There are two problems with this beginner question. Number one people often use this as an excuse for the fact that they don't have the ability to do the math or write the code. So that's very important. A library can be a replacement for a lack of ability and skill. Number two there are no libraries that will fit your use case. So what you're asking for it does not even exist. A true matter of practicality is that if you're going to ask for something you have to know what you're asking for in the first place. And many people who do ask this question simply don't. The rest of this lecture will explain why?

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_91.PNG)

&nbsp;&nbsp;&nbsp;OK so why are there no libraries that will help us implement these algorithms in a so-called practical manner. Well let's think about the code we just wrote. How much of it was devoted to the actual algorithm itself. Let's count. We have one line of code a sample from our posterior distribution. We have two lines of code to update the posterior distribution. And finally we have one more line of code to select a bandit. By choosing the ARG Max over the samples in total that's four lines of code. Let's ask ourselves do we need a library for four lines of code.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_92.PNG)

&nbsp;&nbsp;&nbsp;In actuality we do not need a library for just a few lines of code. Most of the work that you need to do when implementing this algorithm in the real world is actually outside of this so-called library and has more to do with back end engineering. In order to make this lecture complete I'm going to explain what this back engineering involves. Even though some of you may not be back in engineers I hope that it at least helps you understand why the idea of looking for a library to do this job does not make any sense. First let's consider that many back in servers do not use python. Python is a slow language. Some companies do use python as a back end. But it's not as ubiquitous as it is for say data science and machine learning. Many companies use other languages and frameworks such as Ruby on Rails Java Scala Erlang GO P. HP and C++ and in many of these languages doing data science is not a popular thing. So you're unlikely to find something like a P HP library for Bayesian statistics. It just doesn't exist. But again you don't need a library for a few lines of code anyway.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_93.PNG)

&nbsp;&nbsp;&nbsp;So what are the tasks that actually need to be done. First you're going to need a centralized data store whether that's an ASKEW Well database or a key value store which holds all of your band at arm's parameters. Unlike our toy examples that's not going to exist in memory in the real world. You might have 10 or 20 servers all around the world. Obviously you can't keep the data on each machine synchronized then replicated exactly on all of these servers. You need to have a database of some kind in addition your data might be stored in log files. If you don't want to deal with them in real time due to performance issues so you might need to have some batch job that ingests these log files periodically and then uses that data to update the parameters of your model in an off line setting. That would be an entirely separate computer program living on separate machines so clearly a single library on a single machine is not going to do the job you're going to have your batch job workers and your web servers and they're both responsible for two totally different things. In fact your batch jobs and your Web services may not even be written in the same programming language in the first place. So where does a library fit into this architecture.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_94.PNG)

&nbsp;&nbsp;&nbsp;In reality code like this is not fit for a library. The libraries you do need to worry about might be as follows. First you want to have a web server framework. Obviously this falls more into the responsibilities of the backend engineering team rather than the data scientist team. Maybe that's Django or ruby on rails or the C++ active framework. Then you need to figure out what database you're going to use that could be post grass. Might as well read as or many cached you'll also need a library in your programming language that connects to that database. And if you're processing large amounts of data in your batch jobs you might need to perform these jobs on a cluster of machines. In that case you might use a library like Apache Spark so this is the kind of thing you need to worry about in terms of libraries in comparison to actual lines of code that implement your banded algorithm are miniscule. Overall I hope it's clear that a library for doing such a task in this context would not make sense.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_95.PNG)



# Nonstationary Bandits

&nbsp;&nbsp;&nbsp;In this lecture we are going to consider a new scenario which will provide some depth to what we have been doing this whole time. Earlier I did a lecture that was all about how to calculate a sample mean without having to store all the values so that you would need to some of them altogether in one go. This is a sequel to that lecture. So it's the next stage of what we need to discuss when it comes to calculating a sample mean. Now again I want to mention that you probably at first glance think this is a very trivial topic and that perhaps there should be no need at all to discuss why one would have to talk about calculating sample means to such great depth. However as you learn more about reinforcement learning you will progressively connect the dots. So let's start with just reviewing what we've established already. First we figured out how we could calculate a sample mean out of N samples in terms of the sample mean from the first and minus one samples. Then we did some basic algebra on this equation to turn it into a new form. When the kind of looks like gradient descent.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_96.PNG)

&nbsp;&nbsp;&nbsp;In this lecture we are going to answer the question What happens if the reward is non stationary. Well first we have to talk about what stationary means in the first place. So let's start with that in our previous examples. A reward always came from the same distribution to state it in the usual way the rewards from each band it were I'd be independent and identically distributed. This is not unrealistic. But what about another possible scenario. What if the distribution of the rewards changes over time so that in essence our sample mean calculation doesn't make any sense because the mean at some previous time is not the same as the mean currently to give it a more concrete definition. A stationary process is generally a random process whose distribution does not change over time. That's usually what we refer to as Strong sense stationary most of the time in statistics and signal processing. We are interested in a week sense stationary which relaxes the idea that the entire distribution has to remain constant over time. Instead only the mean and auto covariance of the reward has to be constant over time in order to have a weak sense stationary. Now if you don't know where any of these things mean it's optional. So just kind of remember the basic ideas. Stationary means things don't change over time. If today your slot machine is giving you a win rate of 10 percent and tomorrow your slot machine is giving you a win rate of 90 percent. That's non stationary. Also you can look at these examples that I've shown you here. So on the left we have white noise which is stationary. The distribution doesn't change over time on the right we have Bitcoin's U.S. dollar exchange rate as you can see both the mean and auto covariance change over time.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_97.PNG)

&nbsp;&nbsp;&nbsp;So what do you do when your reward signal is non stationary. Clearly taking the sample mean won't work. Well let's look at our equation for updating the sample mean again. I claim that if I take this equation and I say instead of taking my learning rate to be 1 over n I take my learning rate to be constant. This will give me an exponentially weighted moving average. So what we are going to do with the rest of the lecture is number one and talk about why an exponentially weighted moving average makes sense and number two. I'm going to prove to you that if you do the update with a constant learning rate that indeed gives you the exponentially weighted moving average.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_98.PNG)

&nbsp;&nbsp;&nbsp;First let's talk about why an exponentially weighted moving average makes sense. Let's start by recognizing what the arithmetic mean is in terms of a weighted song the sample mean of the first N samples is the weighted some of those n samples where each of the weights is constant and equal to one over and that makes sense because if your true mean it never changes you would want each sample to contribute equally to the sample mean. But what if your mean does change over time. You want your sample mean to reflect the most recent data into account for the fact that the older the data is the more unreliable it probably is. So what does the exponentially weighted moving average do. Well it does exactly what it sounds like. It gives weights to each sample that exponentially decay over time. That makes perfect sense since if the mean is changing over time then the most recent sample is the most reliable the last sample is a little less reliable and the sample before that is even less reliable and so forth. So this seems like a good way to keep track of the mean as it changes. 

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_99.PNG)

&nbsp;&nbsp;&nbsp;The next question we want to answer is how does this update actually implement an exponentially weighted moving average. Can we show that this is true. In fact it's not too difficult. It helps if we rearrange or mean update so that we can state the sample mean A time t to be a convex combination of the sample mean at time T minus one and the new sample at time t so this means something like give 90 percent of the weight to the previous sample mean and 10 percent of the weight to the latest sample. And that would be if you chose alpha equals zero point one now what we can do is just keep recursively plugging in older and older values of the sample mean so we can replace x bar at T minus one with its representation in terms of x bar t minus two. Then we can multiply out the one minus alpha term so that we get x bar t minus two by itself. Now we have three terms x bar t minus two. The sample at T minus one in the sample at time t the next step of course is to replace X by T minus two with its representation in terms of x bar T minus three. From there we can do the same thing. Multiply out the one minus alpha and get each of the terms by themselves at this point. You should see a pattern. The number of individual samples keeps growing and the power on the one minus alpha term also keeps growing if we keep repeating this pattern at t times we end up with this expression in evolving a summation over all the past samples from one up to T and of course these weights are exactly exponentially decaying since Alpha is a number between 0 and 1 1 minus alpha is also a number between 0 and 1 and when you raise a number between 0 and 1 to a power it gets smaller and smaller exponentially as K gets larger and larger.

![](../Assets/photos/Return%20of%20the%20Multi-Armed%20Bandit_100.PNG)


# Bandit Summary, Real Data, and Online Learning






















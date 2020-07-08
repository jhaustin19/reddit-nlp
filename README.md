# Executive Summary

- The goal of this project was to build an NLP model capable of classifying a Reddit post as being from [/r/Christianity](https://www.reddit.com/r/Christianity/) or [/r/Catholicism](https://www.reddit.com/r/Catholicism/) based solely on its title.
- I used an API to grab 25,000 posts from each subreddit, and was left with a little less than 30,000 total to model with after cleaning.
- Two separate NLP models (one using logistic regression, another using naive Bayes) were constructed, each with an accuracy rate of around 75%. I consider such an accuracy rate a success given the large degree of overlap between the two communities.
- I was also highly interested in inference, hoping to discover important theological distinctions. This turned out to be less fruitful than I hoped, but perhaps understandably so. The model ended up using the strongly predictive but trivial trend of people in */r/Christianity* self-identifying as Christians, but those in */r/Catholicism* self-identifying as Catholics

# Background

Here is how each subreddit describes itself:

> /r/Christianity is a subreddit to discuss Christianity and aspects of Christian life. All are welcome to participate.

> /r/Catholicism is a place to present new developments in the world of Catholicism, discuss theological teachings of the Catholic Church, provide an avenue for reasonable dialogue amongst people of all beliefs, and grow in our own spirituality. Catholic Christianity offers the world the fullness of the Christian Faith.

The assumption I made is that */r/Christianity* is primarily used by [Protestants](https://en.wikipedia.org/wiki/Protestantism), whereas */r/Catholicism* is primarily used by [Catholics](https://en.wikipedia.org/wiki/Catholic_Church). It's fair to question whether or not this assumption is valid. It was made partly based on intuition, but there was some confirmation in the data. With this in mind, my hope was to understand some fundamental differences between Protestants and Catholics.

# Data Acquisition & Cleaning

The [Pushshift API](https://github.com/pushshift/api) allows you to pull posts from any subreddit of your choosing. I wrote the functions in [pushshift_functions.py](./code/pushshift_functions.py) to work on top of the API, allowing me to manually grab the number of posts I wanted. Cleaning included:
- Removing superfluous columns
- Removing posts for which the content had been deleted by the community moderators
- Removing reposts

# EDA

Perhaps the most useful bit of EDA was confirming that the two subreddits were mostly segregated - that is, only about 3% of people post in both communities. This was essential, because the underlying assumption was that the two communities represent different theological leanings.

# Modeling

Two separate NLP models (logistic regression and naive Bayes) both achieved an accuracy rate of about 75%. Given that the two models each achieved roughly the same accuracy rate, it's possible that it's something of an upper bound for this problem.
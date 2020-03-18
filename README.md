# Mental health forums | A language analysis 

#### GA | DSI Capstone Project 

In our current climate, a focus on online solutions to mental illness is critical.
 
The SuicideWatch Reddit forum has over 190k members with only 10 human moderators that monitor and remove abusive posts. This is tedious and timely. 

Exposure of Reddit comments to the online community are based on their ‘score’ and the time in which they are posted. Exposure is **not** related to the content of the post. For sensitive online communities, it is vital that we are able to filter and detect any comments that may impose harm.  

If one is able to identify important features in high and low scoring comments in mental health threads, this could help improve the handling and moderation of suicidal intentions on social media platforms.  

## Problem statement:
 
Can we identify language based features that predict low or high scores on Reddit mental health forums? 
 
## Methodology:
 
1.    Collect Reddit data to extract comments from submissions
2.    Clean, engineer features and prepare data for analysis 
3.    Model non-language features and analyse their importance 
4.    Model the language sentiment and topics
5.    Model language features and analyse their importance 
6.    Explore the context of the language coefficients and whether they align with external research 

## Data collection: 
 
#### Reddit API 
Praw Python wrapper to extract data to perform keyword or phrase analysis. 
Collect Reddit data dating back to 2009 from SuicideWatch, Anxiety, MentalHealth forums. These were chosen due to fairly similar numbers of active users and comments. 
 
#### Features obtained via the API
Comment score, user id, post title, post creation time, number of comments, comment depth, comment edited, comment awards, comment controversiality, comment creation time, comment archived, replies to comment. 
 
## Data prep: 
 
#### Clean data
Rename columns; infer missing values; convert data into correct format; separate the removed/deleted comments that have been moderated or removed by the user for later analysis and remove most recent comments posted 1 hour prior to data collection.
Convert language to lowercase and remove digits.
 
#### Feature engineering
Extract comment length, special characters, uppercase ratio of words, emojis, URLs, instances of I, time (hour, week and year) comment was posted. 
 
#### Target metric preparation
Create four equal sized classes, using a qcutting method and resampling technique to improve the comment score distribution. 
Random down sampling method chosen due to its computational speed and ease in implementation.  
 
## Modelling:
 
**Baseline** 0.25 
 
#### Model non-language features
* Ran a number of classification models on all 39 engineered features; KNN, Logistic regression, Random forest, Bagging, AdaBoost and GradBoost. 

#### Model language features
* In order to find the optimal number of features and model, I ran a grid search and PCA; TfidfV was utilised, where rare words were weighted most highly, creating a corpus of 5000 features and n grams with a range of 1 to 3. Stop words were removed and words were stemmed and lemmatised. 
* Transforming the vector to a sparse matrix to speed up computational efficiency,  I ran a number of classification models. 
* Ran LDA using TfidfV model which used unsupervised learning to return salient topic and word clusters for the whole corpus. However, topics were found to be very similar in both low and high scoring comments. I found similar issues when running sentiment analysis. 
 
*I ran models on all three subforums, individually and combined, creating a merged data frame with a global corpus. Accuracy was highest in the SuicideWatch forum. I chose to explore this further, as I believed that it was vital to accurately analyse due to the serious nature of this thread.* 
 
## Results: 

#### Non language results
 
Grid search: GradBoost
* Achieved the optimal accuracy score of **49.7%**
 
The length of post time; the popularity of thread; the position of comment and its length, are just some of the important coefficients that contribute  towards driving up the comment score.   
However, these aren’t useful features for immediate detection of harmful or helpful comments being made.. 
 
#### Language results
 
Grid search: Logistic regression 
* Achieved an optimal accuracy score of **55.3%** (30% above baseline)
* Average K fold cross validated testing score **50.01%**

According to the confusion matrix, classification report and ROC curves, the model performs the best in classifying the lowest and highest scoring comments; accuracy and F1 scores are highest. Given the nature of this sensitive forum, increasing the detection and classification of potentially harmful comments is desirable, thus increasing false negatives and tuning towards a higher recall at the expense of precision.

#### Terms that decrease comment score

* **'change world', 'changes', 'meaning life'**
*Generic uplifting comments. Vague,over-simplistic language.*
* **'bad thing', 'makes sad', 'destructive’**
*Casting blame and guilt-tripping terms. Judgement can be damaging.*     
* **'Passion', 'lots love'**
*Highly emotive language*
* **'doesn sound'** 
*Trivialising the situation, downplaying one’s agency and lacking compassion.**
* **'hotline', 'proving wrong'**
*Offering solutions or posing too aggressively as a role model.*

#### Terms that increase comment score
* **'im sorry', 'ive got' 'just felt', 'did try', 'reminds', 'did help'**
*Engaging and relates to the situation validating ones emotions.*
* **'taboo'** *Addressing the concept of stigma*
* **'thoughts feelings', 'people struggle'**
*Evokes compassion*
* **'service', 'laws'**
*Factual and possibly clinical*

## Analysis 

***These findings were consistent with research done in a 2019 survey!***
*The survey consisted of participants rating descriptors pertaining to suicidal behaviour according to perceived acceptability.*
 
**Drawbacks to this analysis**
- Difficult to interpret what these terms represent without context.
- Varies for what people find helpful, making it very difficult to predict.
- Huge variety of people are ranking the comments
- Comments have already been moderated. (When analysing removed comments, their replies were mostly removed and deleted as well).
- Lacks generalizability to other forums 
 
 
* When looking through the comments containing the coefficients associated with low scores, I often found patterns of downvoting where people offered ‘preachy’ advice and blanket solutions.
 
* When looking through coefficients associated with higher scores, softer, more personal language was perceived as empathetic and less rigid. 
 
## Future directions:
 
* Explore T-SNE; a popular method for visualising high dimensional data.
* Explore Word2Vec; a pre trained corpus containing over 100 billion words.
* Perform a Gradboost on language model and optimise the accuracy score further. 
* Determine unique patterns in other forums, allowing strategies to become more specific 
 
## Conclusion:
 
Sensitive online communities may need a customise their comment ranking systems based on the content of comments. Filtering out harmful content and prioritising helpful content. 
 
This could be applied to any other online forum that offers community based feedback to posts on suicide, self-harm, or other mental health related themes. 

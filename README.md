**AutoShop Churn Customer Classification Model**

**Author:** Muhammad Erico Ricardo

**Background:**

AutoShop, an e-commerce marketplace specializing in automotive products, aims to improve customer retention. The data analysis team developed a churn prediction model to identify customers at risk of leaving. This model allows the marketing team to target these customers with incentives and support.

**Model Overview:**

This multiclass classification model categorizes customers based on a churn score. The churn score predicts the likelihood of a customer abandoning AutoShop.

**Churn Score Categories:**

| Churn Score | Description | Action |
|---|---|---|
| 0 | Very Low | Retain with loyalty program |
| 1 | Slightly Below Average | Offer small promotions |
| 2 | Slightly Above Average | Increase customer interaction |
| 3 | Average | Offer special deals or referral programs |
| 4 | High | Make direct contact, offer personalized solutions |
| 5 | Very High | Try to save the customer with attractive offers |

**Model Evaluation:**

The model achieved an accuracy of 82% on the training set and 78% on the test set. However, the lower test set accuracy indicates some overfitting.

**Model Advantages:**

* Decent accuracy (78% on test set)
* Optimized for fast performance on large datasets
* Successfully classifies data with medium to high churn scores (f1-score > 70% for scores 1-5)
* Easy deployment through a single pipeline with feature engineering and modeling

**Model Disadvantages:**

* Limited accuracy with room for improvement
* Difficulty classifying churn score 0 due to limited data
* Tendency to overfit

**Future Improvements:**

* Increase data for churn score 0 to improve classification accuracy
* Perform comprehensive hyperparameter tuning
* Utilize a more robust model like LightGBM for enhanced performance and stability

**Insights from Exploratory Data Analysis (EDA):**

* Customers with basic or no membership have a higher churn risk.
* Lower average transaction value correlates with higher churn potential.
* Time spent on the website indicates higher customer loyalty.
* Complaint history is not a strong churn predictor.
* Customer feedback highlights product quality, excessive advertising, poor website design, and bad customer service as significant churn factors.

**Recommendations Based on Feedback:**

* **Target Basic/No Membership Customers:**
    * Offer loyalty programs to incentivize membership upgrades or subscriptions.
    * Provide special deals or discounts to encourage frequent transactions.
* **Improve Product Quality:**
    * Conduct product evaluations and identify areas for improvement.
    * Develop new products or enhance existing features to meet customer needs.
* **Enhance Website User Experience:**
    * Consider a user-friendly and visually appealing website redesign.
    * Limit website ads to improve user experience.
* **Improve Customer Service:**
    * Train customer service teams for enhanced service quality.
    * Increase communication channels (e.g., live chat, social media) for feedback and inquiries.

**Hugging Face Space:**

[https://huggingface.co/spaces/EricoR/Milestone2](https://huggingface.co/spaces/EricoR/Milestone2)

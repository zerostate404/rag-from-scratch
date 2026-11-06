---
title: Precision vs Recall
topic: evaluation
difficulty: easy
---
# Question
What is the difference between precision and recall?

# Key points
- Precision = TP / (TP + FP): of predicted positives, how many are correct
- Recall = TP / (TP + FN): of actual positives, how many were found
- Precision rewards not crying wolf; recall rewards not missing positives
- The tradeoff: lower the threshold → higher recall, lower precision (and vice versa)

# Reference answer
Precision answers "when the model says positive, how often is it right?" — TP / (TP + FP). Recall answers "of all the actual positives, how many did it find?" — TP / (TP + FN). They trade off as you move the classification threshold: a lower threshold catches more positives (recall up) but drags in more false positives (precision down); a higher threshold is stingier and more accurate when it fires. Which matters more depends on the cost of errors. Spam filtering cares about precision — a false positive (ham in the spam folder) is worse than a missed spam. Cancer screening cares about recall — missing a positive is far worse than a false alarm. The F1 score combines them.
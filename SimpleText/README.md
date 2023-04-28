pyterrier_and_bert.py
  gets top 500 results per topic_id with both pyterrier and bert independently
  
combine_scores.py
  merges both files by combining scores with magic formula if both models predicted same document and returning top 100 per topic (highest scores)
  if not found in other file, the score will be penalized since the score would potentially be doubled if found in both
  also fixes problems when originally getting intersection as if there is no intersection, we will still have a top 100 results

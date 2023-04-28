# pyterrier_and_bert.py
  - gets top 500 results per topic_id with both pyterrier and bert independently
  
# combine_scores.py
  - merges both files by combining scores with magic formula if both models predicted same document and returning top 100 per topic (highest scores)
  - if not found in other file, the score will be penalized since the score would potentially be doubled if found in both
  - also fixes problems when originally getting intersection as if there is no intersection, we will still have a top 100 results

the nbt text files are the two text files made in pyterrier_and_bert.py
the combined text file is the result of combine_score.py when using the nbt files for the arguments

you can run pyterrier_and_bert.py with no arguments. need to manually change directories and names of output files in code
combine_score.py takes 3 arguments, [filename] [other_filename] [new_output_filename]

# current results:
  - ndcg = 0.14616064921841457
  - map = 0.1113105463024071

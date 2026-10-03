data = LOAD '/social_media/input/social_media_posts_5kb.csv'
       USING PigStorage(',')
       AS (
           target:int,
           tweet_id:long,
           tweet_date:chararray,
           flag:chararray,
           username:chararray,
           text:chararray,
           hashtags:chararray
       );

clean_data = FILTER data BY target IS NOT NULL;

STORE clean_data INTO '/social_media/processed'
USING PigStorage(',');

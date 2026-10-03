data = LOAD '/social_media/input/social_media_final.tsv'
       USING PigStorage('\t')
       AS (target:int, tweet_id:long, tweet_date:chararray, flag:chararray, username:chararray, text:chararray, hashtags:chararray);

clean_data = FILTER data BY tweet_id IS NOT NULL AND text IS NOT NULL;

clean_data = FOREACH clean_data GENERATE
             target,
             tweet_id,
             tweet_date,
             username,
             text,
             hashtags;

STORE clean_data INTO '/social_media/pig_output' USING PigStorage('\t');

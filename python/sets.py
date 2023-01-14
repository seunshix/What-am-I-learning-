# Creating a set
genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results)
print(survey_genres)

survey_abbreviated = {genre[:3] for genre in survey_genres}
print(survey_abbreviated)


# Using frozen set
top_genres = ['rap', 'rock', 'pop']

# Write your code below!
frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)

#adding to a set
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
tag_set = set(song_data['Retro Words'])
print(tag_set)
print()
tag_set.update([user_tag_1, user_tag_2, user_tag_3])
#or 
# tag_set.add(user_tag_1)
# tag_set.add(user_tag_2)
# tag_set.add(user_tag_3)

print(tag_set)
song_data['Retro Words'] = tag_set

# deleting from set
song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
print(tag_set)
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')
# OR
tag_set.discard('onion')
tag_set.discard('helloworld')
tag_set.discard('spam')
print(tag_set)
song_data_users['Retro Words'] = tag_set

# finding data in set

allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
print(tag_set)
print()
bad_tags = [tag for tag in tag_set if tag not in allowed_tags]
print(bad_tags)

for tag in bad_tags:
  tag_set.remove(tag)

print(tag_set)

song_data_users['Retro Words'] = tag_set


#finding unions with set
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
new_song_data = {}
for key, value in song_data.items():
  song_data_set = set(value)
  user_tag_data_set = set(user_tag_data[key])
  new_song_data[key] = song_data_set.union(user_tag_data_set)
  # OR
  # new_song_data[key] = song_data_set | user_tag_set

print(new_song_data)


# Set Intersection
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
tags_int = set(user_recent_songs['Retro Words']).intersection(set(user_recent_songs['Lowkey Space']))
# Or
# tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])
print(tags_int)

recommended_songs = {}
for key, value in song_data.items():
  for tag in value:
    if tag in tags_int:
      if key not in user_recent_songs:
        recommended_songs[key] = value

print(recommended_songs)


# Set Difference

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!
tag_diff = set(user_liked_song['Back To Art']).difference(set(user_disliked_song['Retro Words']))

# OR

# tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])
print(tag_diff)

recommended_songs = {}
for key, value in song_data.items():
  for tag in value:
    if tag in tag_diff:
      if key not in user_liked_song.keys() and key not in user_disliked_song.keys():
        recommended_songs[key] = value
print(recommended_songs)

# Set Symmetric Difference
user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
user_tags = set()

for key, value in user_song_history.items():
  user_tags.update(set(value))
  
print(user_tags)

friend_tags = set()

for key, value in friend_song_history.items():
  friend_tags.update(set(value))
  
print(friend_tags)

unique_tags = user_tags.symmetric_difference(friend_tags)

# OR
# unique_tags = user_tags^friend_tags

# lil exercise
music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

regular_tag_intersect = music_tags & my_tags
print()
print(regular_tag_intersect)


frozen_tag_difference = my_tags - music_tags
print()
print(frozen_tag_difference)

regular_tag_sd = music_tags ^ my_tags
print()
print(regular_tag_sd)
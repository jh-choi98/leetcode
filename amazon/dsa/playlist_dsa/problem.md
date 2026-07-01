Imagine you are building a music streaming service. A core feature is the user's playlist. We need you to design and implement a Playlist class in the language of your choice.

Requirements: The Playlist class must support the following operations:

- add_song(song_name: str): Adds a new song to the very end of the
  playlist.
- remove_nth_from_end(n: int) -> str: Finds and removes the nth song
  from the end of the playlist. n=1 represents the last song, n=2 the
  second to last, and so on. This method should return the name of the
  song that was removed. If n is an invalid value (e.g., out of bounds),
  it should handle the error gracefully.
- print_playlist(): Displays the current playlist in order, from the
  first song added to the last. If the playlist is empty, it should
  indicate that.

  Example Usage:

```python
playlist = Playlist()
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Stairway to Heaven")
playlist.add_song("Hotel California")
playlist.add_song("Sweet Child O' Mine")

# Current playlist:
# 1. Bohemian Rhapsody
# 2. Stairway to Heaven
# 3. Hotel California
# 4. Sweet Child O' Mine

playlist.print_playlist()

removed = playlist.remove_nth_from_end(2)
# Should remove "Hotel California"
print(f"\nRemoved: {removed}")

# Current playlist:
# 1. Bohemian Rhapsody
# 2. Stairway to Heaven
# 3. Sweet Child O' Mine

playlist.print_playlist()
```

Follow-up Question: After you've implemented the class, let's discuss how you would add a shuffle() method to the playlist. What would be an efficient algorithm to implement this?

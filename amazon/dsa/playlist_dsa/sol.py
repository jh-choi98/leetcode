import random


class Song:
    def __init__(self, title):
        self.title = title
        self.next: Song | None = None
        self.prev: Song | None = None

# doubly linked list
class Playlist:
    def __init__(self) -> None:
        self.head = Song("dummy_head")
        self.tail = Song("dummy_tail")
        self.length = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_song(self, song_name: str):
        new_song = Song(song_name)
        
        cur_last_song = self.tail.prev
        
        self.tail.prev = new_song
        new_song.next = self.tail
        new_song.prev = cur_last_song
        cur_last_song.next = new_song
        
        self.length += 1
        
    def remove_nth_from_end(self, n: int) -> str:
        if n > self.length or n <= 0:
            raise ValueError(f"Invalid index {n}")
        
        target = self.tail
        while n > 0:
            target = target.prev
            n -= 1
        
        prev_target = target.prev
        next_target = target.next
        
        prev_target.next = next_target
        next_target.prev = prev_target
        
        self.length -= 1
        
        return target.title
        
    def print_playlist(self):
        if self.length == 0:
            print("The playlist is empty")
            return
        
        list_of_songs = []
        
        node = self.head.next
        while node.next:
            list_of_songs.append(node.title)
            node = node.next
        
        print(list_of_songs)
        
    def shuffle(self):
        if self.length <= 1:
            return
        
        nodes = []
        node = self.head.next
        while node is not self.tail:
            nodes.append(node)
            node = node.next
        
        # Fiher-Yates on the array (O(n))
        for i in range(len(nodes) - 1, 0, -1):
            j = random.randint(0, i)
            nodes[i], nodes[j] = nodes[j], nodes[i]
        
        prev = self.head
        for node in nodes:
            prev.next = node
            node.prev = prev
            prev = node
            
        prev.next = self.tail
        self.tail.prev = prev
            
            
def test():
    # ---------- add_song + print_playlist ----------
    playlist = Playlist()
    playlist.add_song("Bohemian Rhapsody")
    playlist.add_song("Stairway to Heaven")
    playlist.add_song("Hotel California")
    playlist.add_song("Sweet Child O' Mine")

    print("Initial playlist:")
    playlist.print_playlist()
    assert playlist.length == 4

    # ---------- remove from the middle (n=2) ----------
    removed = playlist.remove_nth_from_end(2)
    print(f"\nRemoved: {removed}")
    assert removed == "Hotel California"
    assert playlist.length == 3
    print("\nAfter removing 2nd from end:")
    playlist.print_playlist()

    # ---------- remove the last song (n=1) ----------
    removed = playlist.remove_nth_from_end(1)
    assert removed == "Sweet Child O' Mine"
    assert playlist.length == 2

    # ---------- remove the first song (n = length) ----------
    removed = playlist.remove_nth_from_end(2)   # 2 songs left, so n=2 is the first
    assert removed == "Bohemian Rhapsody"
    assert playlist.length == 1

    # ---------- invalid n ----------
    for bad_n in (0, -1, 5):
        try:
            playlist.remove_nth_from_end(bad_n)
            print(f"FAILED: n={bad_n} should have raised")
        except ValueError:
            pass  # expected

    # ---------- remove down to empty ----------
    removed = playlist.remove_nth_from_end(1)
    assert removed == "Stairway to Heaven"
    assert playlist.length == 0

    print("\nAfter removing everything:")
    playlist.print_playlist()   # should say empty

    # ---------- remove from empty playlist ----------
    try:
        playlist.remove_nth_from_end(1)
        print("FAILED: removing from empty should raise")
    except ValueError:
        pass  # expected

    print("\nAll tests passed")

test()

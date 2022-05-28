class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self , name , age , tracks, score ):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def change_age(self, new_age):
        self.age = int(new_age)
        return self.age

    def add_track(self, new_track):
        track = self.tracks
        track.append(new_track)
        return track
    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
final_name = Bob.change_name("Peter")
final_age = Bob.change_age(34.6)
final_tracks = Bob.add_track("UI/UX")
score = Bob.get_score()

print(f"My name is {final_name}.\nI am {final_age} years old.\nI am currently enrolled in the Zuri training and studying the following courses:")
for courses in range(len(final_tracks)):
    print(f"{courses + 1}. {final_tracks[courses]}")
print(f"So far, I have scored {score} averagely.")

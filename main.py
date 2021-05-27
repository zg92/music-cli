from scale_generator import scale_generator 
from verse_generator import verse_generator 
import sys

def route_args():
    if sys.argv[1] == 'scale':
        scale_gen = scale_generator()
        scale_gen.create_scale(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'progression':
        prog_gen = scale_generator()
        prog_gen.create_progression(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'lyrics':
        lyrics_gen = verse_generator()
        lyrics_gen.lyrics(sys.argv[2])


if __name__ == '__main__':
    print('Welcome to the MusicBox!')
    route_args()


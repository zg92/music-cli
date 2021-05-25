class scale_generator():
    def __init__(self):
        self.notes = ['A', 'A#', 'B', 'C', 'C#',
                      'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.major_pent = [0, 2, 4, 7, 9]
        self.minor_pent = [0, 3, 5, 7, 10]
        self.major_scale = [0, 2, 4, 5, 7, 9, 11]
        self.minor_scale = [0, 2, 3, 5, 7, 8, 10]

    def return_note_list(self, root, interval_list):
        returned_interval_list = []
        root_index = self.notes.index(root)
        for interval in interval_list:
            adjusted_index = root_index + (int(interval))
            if adjusted_index >= len(self.notes):
                adjusted_index = len(self.notes) - (adjusted_index)
                if adjusted_index < 0:
                    adjusted_index = 0 + (adjusted_index * -1)
            returned_interval_list.append(self.notes[adjusted_index])
        return returned_interval_list

    def create_scale(self, root, interval):
        if interval == 'minor_pent':
            print(self.return_note_list(root, self.minor_pent))
        elif interval == 'major_pent':
            print(self.return_note_list(root, self.major_pent))
        elif type(interval) is str:
            print(self.return_note_list(root, interval_list))

    def create_progression(self, root, chords, *mm):
        if type(chords) is str:
            if not mm or mm == 'major':
                scale_degrees = self.return_note_list(root, self.major_scale)
            elif mm[0] == 'minor':
                scale_degrees = self.return_note_list(root, self.minor_scale)
            progression_list = [scale_degrees[int(chord_interval)] if chord_interval == '0' else scale_degrees[int(
                chord_interval) - 1] for chord_interval in chords]
            print(progression_list)


x = scale_generator()

# x.create_scale('C', '09876543')
# x.create_progression('A', '000044005405', 'minor')
# x.create_scale('D', 'major_pent')
x.create_progression('B', '000044004505')

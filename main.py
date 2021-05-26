class scale_generator():
    def __init__(self):

    #Hard Coded Scales + Notes
        self.notes = ['A', 'A#', 'B', 'C', 'C#',
                      'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.major_pent = [0, 2, 4, 7, 9]
        self.minor_pent = [0, 3, 5, 7, 10]
        self.major_scale = [0, 2, 4, 5, 7, 9, 11]
        self.minor_scale = [0, 2, 3, 5, 7, 8, 10]

    #Function to convert scale formulas notes
    def return_note_list(self, root, interval_list):
        returned_interval_list = []
    #Get root note by looking at index of root argument
        root_index = self.notes.index(root)
    #Loop through interval list and adjust the index when it is < 0 or > len(notes)
        for interval in interval_list:
            adjusted_index = root_index + (int(interval))
            if adjusted_index >= len(self.notes):
                adjusted_index = len(self.notes) - (adjusted_index)
                if adjusted_index < 0:
                    adjusted_index = 0 + (adjusted_index * -1)
            returned_interval_list.append(self.notes[adjusted_index])
        return returned_interval_list

    #Method to route input if input is scale or potentially reroute to proper method.
    def create_scale(self, root, interval):
        if interval == 'minor_pent':
            print(self.return_note_list(root, self.minor_pent))
        elif interval == 'major_pent':
            print(self.return_note_list(root, self.major_pent))
        elif type(interval) is str:
            print(self.create_progression(root, interval))

    #Method to take any numbers input and convert it into notes
    def create_progression(self, root, chords, *mm):
        if not mm or mm[0] == 'major':
            scale_degrees = self.return_note_list(root, self.major_scale)
        elif mm[0] == 'minor':
            scale_degrees = self.return_note_list(root, self.minor_scale)
        progression_list = [scale_degrees[int(chord_interval)] if int(chord_interval) == 0 else scale_degrees[int(
        chord_interval) - 1] for chord_interval in chords]

        if isinstance(chords, (list, str, int)) is False: 
            print('Make sure to pass in a string, list, or integer or results may not function properly')
        print(progression_list)


x = scale_generator()

# x.create_scale('C', '09876543')
x.create_progression('A', '000044005405')
# x.create_scale('D', 'major_pent')
x.create_progression('A', [0,0,0,0,4,4,5,5,4,0,5])

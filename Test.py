import math

def note_to_frequency(note):
    # Define the base frequency of A4 (440 Hz)
    A4 = 440
    
    # Map each note to its relative distance from A4
    notes = {
        'C': -9,
        'C#': -8,
        'Db': -8,
        'D': -7,
        'D#': -6,
        'Eb': -6,
        'E': -5,
        'F': -4,
        'F#': -3,
        'Gb': -3,
        'G': -2,
        'G#': -1,
        'Ab': -1,
        'A': 0,
        'A#': 1,
        'Bb': 1,
        'B': 2
    }
    
    # Split the note into its pitch and octave
    pitch = note[:-1]
    octave = int(note[-1])
    
    # Calculate the distance from A4 for the given note
    distance = (octave - 4) * 12 + notes[pitch]
    
    # Calculate the frequency using the distance
    frequency = A4 * math.pow(2, distance / 12)
    
    return frequency

def major_sixth(note):
    # Get the frequency of the starting note
    frequency = note_to_frequency(note)
    
    # Calculate the major sixth frequency by multiplying by 5/3
    major_sixth_frequency = frequency * (5 / 3)
    
    return major_sixth_frequency

# Example usage
note = 'C4'
major_sixth_frequency = major_sixth(note)
print(f"The major sixth above {note} is {major_sixth_frequency} Hz.")

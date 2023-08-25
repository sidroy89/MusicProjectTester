import streamlit as st


def analyse_BPM(data):

  print ("FULL DATASTRUCTURE")
  print(data)
  
  

  BPMsum = 0

  bpm_list = []  # Empty list to store the BPM values

  for item in data:
    bpm = item['BPM']
    bpm_list.append(bpm)

  print(bpm_list)



  #BPMavg = BPMsum / len(BPMlist)
  #st.write("The average BPM of all your pieces is: " + str(BPMavg))

  largo = 0
  adagio = 0
  andante = 0
  allegro = 0
  presto = 0

  for item in bpm_list:
    if int(item) <= 60:
        largo += 1
    elif int(item) <= 76:
        adagio += 1
    elif int(item) <= 110:
        andante += 1
    elif int(item) <= 180:
        allegro += 1
    else:
        presto += 1

  BPMclassifications = [largo, adagio, andante, allegro, presto]
  sorted_BPMclassifications = sorted(BPMclassifications, reverse=True)
  
  max_bpm_classification = max(sorted_BPMclassifications)
  
  if max_bpm_classification == largo:
      st.write("The majority of your pieces are classified as 'Largo'. This means a majority of the pieces have a very slow and broad pace.")
  elif max_bpm_classification == adagio:
      st.write("The majority of your pieces are classified as 'Adagio'. This means a majority of the pieces have a leisurely relaxed pace.")
  elif max_bpm_classification == andante:
      st.write("The majority of your pieces are classified as 'Andante'. This means a majority of the pieces have a moderate pace.")
  elif max_bpm_classification == allegro:
      st.write("The majority of your pieces are classified as 'Allegro'. This means a majority of the pieces have a fast and energetic pace.")
  else:
      st.write("The majority of your pieces are classified as 'Presto'. This means a majority of the pieces have an extremely rushed pace")


def hold_analyse_notes(data_structure):
    note_array = []
    for item in data_structure:
        note_array.extend(item['NOTES'])
    
    # Finding the top 5 most commonly used notes
    note_frequencies = {}
    for note in note_array:
        if note in note_frequencies:
            note_frequencies[note] += 1
        else:
            note_frequencies[note] = 1
    
    top_notes = sorted(note_frequencies, key=note_frequencies.get, reverse=True)[:5]
    
    st.write("Top 5 Most Commonly Used Notes:")
    for i, note in enumerate(top_notes):
        st.write(f"{i+1}. Note: {note}, Frequency: {note_frequencies[note]}")
    
    # Finding three-note patterns that occur more than three times
    pattern_frequencies = {}
    for i in range(len(note_array) - 2):
        pattern = tuple(note_array[i:i+3])
        if pattern in pattern_frequencies:
            pattern_frequencies[pattern] += 1
        else:
            pattern_frequencies[pattern] = 1
    
    frequent_patterns = sorted(pattern_frequencies, key=pattern_frequencies.get, reverse=True)
    frequent_patterns = [pattern for pattern in frequent_patterns if pattern_frequencies[pattern] > 3]
    
    st.write("\nThree-Note Patterns Occurring More Than Three Times (Descending Order):")
    for i, pattern in enumerate(frequent_patterns):
        pattern_str = ' - '.join(pattern)
        st.write(f"{i+1}. Pattern: {pattern_str}, Frequency: {pattern_frequencies[pattern]}")



def hold_analyse_chords(data):
    print("Time to analyze chords")

    # Extract the chords from the data structure
    chord_array = []
    for item in data:
        chords = item['CHORDS']
        chord_array.extend(chords)

    chord_patterns = {}
    chord_types = {}
    top_chords = []

    for i in range(len(chord_array) - 2):
        if chord_array[i] != 'N' and chord_array[i+1] != 'N' and chord_array[i+2] != 'N':
            chord_pattern = tuple(chord_array[i:i+3])
            if chord_pattern in chord_patterns:
                chord_patterns[chord_pattern] += 1
            else:
                chord_patterns[chord_pattern] = 1

    chord_patterns = {pattern: count for pattern, count in chord_patterns.items() if count >= 2}

    for chord in chord_array:
        if chord != 'N':
            if len(chord) == 1:
                chord_type = 'maj'
            else:
                chord_type = chord[1:]  # Exclude the root note
            if 'b' in chord_type or '/' in chord_type:
                continue
            if chord_type in chord_types:
                chord_types[chord_type] += 1
            else:
                chord_types[chord_type] = 1

    st.write("Chord Patterns:")
    for chord_pattern, count in chord_patterns.items():
        chord_pattern_str = ' - '.join(chord_pattern)
        st.write(chord_pattern_str + ': ' + str(count))

    st.write("\nChord Types:")
    for chord_type, count in chord_types.items():
        st.write(chord_type + ': ' + str(count))

    chord_frequencies = {}
    for chord in chord_array:
        if chord != 'N':
            if len(chord) == 1:
                chord_type = 'maj'
            else:
                chord_type = chord[1:]  # Exclude the root note
            if 'b' in chord_type or '/' in chord_type:
                continue
            if chord in chord_frequencies:
                chord_frequencies[chord] += 1
            else:
                chord_frequencies[chord] = 1

    sorted_chords = sorted(chord_frequencies.items(), key=lambda x: x[1], reverse=True)

    for i in range(min(3, len(sorted_chords))):
        chord, frequency = sorted_chords[i]
        top_chords.append(chord)

    st.write("Top 3 Most Used Chords:")
    for chord in top_chords:
        st.write(chord + ': ' + str(chord_frequencies[chord]))

    return chord_patterns, chord_types
    
    
def hold_analyse_key(data):
    correlations = {}
    
    # Calculate the total correlation for each key
    for item in data:
        key_correlation = item['KEY']
        for key, correlation in key_correlation.items():
            correlation = float(correlation)
            if key in correlations:
                correlations[key] += correlation
            else:
                correlations[key] = correlation
    
    # Sort keys based on correlation in descending order
    sorted_keys = sorted(correlations, key=correlations.get, reverse=True)
    
    # Print the top 10 keys with their correlations
    st.write("Top 10 Keys with the Highest Correlation:")
    for i, key in enumerate(sorted_keys[:10]):
        correlation = round(correlations[key], 3)
        st.write(f"{i+1}. Key: {key}, Correlation: {correlation}")
        
        
        
        




def analyse_chords(data):
    # Extract chords from the data structure
    chord_array = [item['CHORDS'] for item in data]
    chord_array = [chord for sublist in chord_array for chord in sublist]

    # Perform chord analysis
    chord_patterns = {}
    chord_types = {}
    top_chords = []

    for i in range(len(chord_array) - 2):
        if chord_array[i] != 'N' and chord_array[i+1] != 'N' and chord_array[i+2] != 'N':
            chord_pattern = (chord_array[i], chord_array[i+1], chord_array[i+2])
            if chord_pattern in chord_patterns:
                chord_patterns[chord_pattern] += 1
            else:
                chord_patterns[chord_pattern] = 1

    chord_patterns = {pattern: count for pattern, count in chord_patterns.items() if count >= 2}

    for chord in chord_array:
        if chord != 'N':
            if len(chord) == 1:
                chord_type = 'maj'
            else:
                chord_type = chord[1:]  # Exclude the root note
            if 'b' in chord_type or '/' in chord_type:
                continue
            if chord_type in chord_types:
                chord_types[chord_type] += 1
            else:
                chord_types[chord_type] = 1

    chord_frequencies = {}
    for chord in chord_array:
        if chord != 'N':
            if len(chord) == 1:
                chord_type = 'maj'
            else:
                chord_type = chord[1:]  # Exclude the root note
            if 'b' in chord_type or '/' in chord_type:
                continue
            if chord in chord_frequencies:
                chord_frequencies[chord] += 1
            else:
                chord_frequencies[chord] = 1

    sorted_chords = sorted(chord_frequencies.items(), key=lambda x: x[1], reverse=True)
    for i in range(min(3, len(sorted_chords))):
        chord, frequency = sorted_chords[i]
        top_chords.append(chord)

    # Display chord patterns in a table
    st.write("Chord Patterns:")
    chord_patterns_table = []
    chord_patterns_table.append(["Chord Pattern", "Frequency"])
    for chord_pattern, count in chord_patterns.items():
        chord_pattern_str = ' - '.join(chord_pattern)
        chord_patterns_table.append([chord_pattern_str, count])
    st.table(chord_patterns_table)

    # Display chord types in a table
    st.write("Chord Types:")
    chord_types_table = []
    chord_types_table.append(["Chord Type", "Frequency"])
    for chord_type, count in chord_types.items():
        chord_types_table.append([chord_type, count])
    st.table(chord_types_table)

    # Display top 3 most used chords in a table
    st.write("Top 3 Most Used Chords:")
    top_chords_table = []
    top_chords_table.append(["Chord", "Frequency"])
    for chord in top_chords:
        top_chords_table.append([chord, chord_frequencies[chord]])
    st.table(top_chords_table)



import streamlit as st

def analyse_notes(data_structure):
    note_array = []

    for item in data_structure:
        note_array.extend(item['NOTES'])

    # Finding the top 5 most commonly used notes
    note_frequencies = {}

    for note in note_array:
        if note in note_frequencies:
            note_frequencies[note] += 1
        else:
            note_frequencies[note] = 1

    top_notes = sorted(note_frequencies, key=note_frequencies.get, reverse=True)[:5]

    # Display top 5 most commonly used notes in a table
    st.write("Top 5 Most Commonly Used Notes:")
    notes_table = []
    notes_table.append(["Note", "Frequency"])
    for i, note in enumerate(top_notes):
        notes_table.append([note, note_frequencies[note]])
    st.table(notes_table)

    # Finding three-note patterns that occur more than three times
    pattern_frequencies = {}

    for i in range(len(note_array) - 2):
        pattern = tuple(note_array[i:i+3])
        if pattern in pattern_frequencies:
            pattern_frequencies[pattern] += 1
        else:
            pattern_frequencies[pattern] = 1

    frequent_patterns = sorted(pattern_frequencies, key=pattern_frequencies.get, reverse=True)
    frequent_patterns = [pattern for pattern in frequent_patterns if pattern_frequencies[pattern] > 3]

    # Display three-note patterns in a table
    st.write("\nThree-Note Patterns Occurring More Than Three Times (Descending Order):")
    patterns_table = []
    patterns_table.append(["Pattern", "Frequency"])
    for i, pattern in enumerate(frequent_patterns):
        pattern_str = ' - '.join(pattern)
        patterns_table.append([pattern_str, pattern_frequencies[pattern]])
    st.table(patterns_table)





def analyse_key(data):
    correlations = {}

    # Calculate the total correlation for each key
    for item in data:
        key_correlation = item['KEY']
        for key, correlation in key_correlation.items():
            correlation = float(correlation)
            if key in correlations:
                correlations[key] += correlation
            else:
                correlations[key] = correlation

    # Sort keys based on correlation in descending order
    sorted_keys = sorted(correlations, key=correlations.get, reverse=True)

    # Display top 10 keys with their correlations in a table
    st.write("Top 10 Keys with the Highest Correlation:")
    keys_table = []
    keys_table.append(["Key", "Correlation"])
    for i, key in enumerate(sorted_keys[:10]):
        correlation = round(correlations[key], 3)
        keys_table.append([key, correlation])
    st.table(keys_table)


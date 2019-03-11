s = 'azcbobobegghakl'
curr_tmp_seq = []
tmp_seqs = []
s_charcodes = [ord(char) for char in s] + ['stop']

for i, code in enumerate(s_charcodes):
    # this will throw an error on the last charcode
    # cant compare str to int on if
    try:
        if code <= s_charcodes[i+1]:
            curr_tmp_seq.append(code)
        else:
            curr_tmp_seq.append(code)
            tmp_seqs.append(curr_tmp_seq)
            curr_tmp_seq = []
    # this runs with last charcode
    except:
        curr_tmp_seq.append(code)
        tmp_seqs.append(curr_tmp_seq)
        break

longest_tmp_seq = []
for seq in tmp_seqs:
    if len(seq) > len(longest_tmp_seq):
        longest_tmp_seq = seq

longest_sequence = ''.join([chr(code) for code in longest_tmp_seq])
print(longest_sequence)

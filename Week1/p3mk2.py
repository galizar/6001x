s = 'azcbobobegghakl'
curr_tmp_seq = []
tmp_seqs = []

for i, char in enumerate(s):
    charcode = ord(char)
    next_char = s[i+1] if i != (len(s)-1) else None

    if next_char:
        next_charcode = ord(next_char)
        if charcode <= next_charcode:
            curr_tmp_seq.append(charcode)
        else:
            curr_tmp_seq.append(charcode)
            tmp_seqs.append(curr_tmp_seq)
            curr_tmp_seq = []
    else:
        curr_tmp_seq.append(charcode)
        tmp_seqs.append(curr_tmp_seq)

longest_tmp_seq = []
for seq in tmp_seqs:
    if len(seq) > len(longest_tmp_seq):
        longest_tmp_seq = seq

longest_sequence = ''.join([chr(code) for code in longest_tmp_seq])
print(longest_sequence)

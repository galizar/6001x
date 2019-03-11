s = 'azcbobobegghakl'
curr_tmp_seq = []
longest_tmp_seq = []

def check_if_longer(candidate, prev_longest):
    if len(candidate) > len(prev_longest):
        return [code for code in candidate]
    else:
        return prev_longest

for i, char in enumerate(s):
    charcode = ord(char)
    next_char = s[i+1] if i != (len(s)-1) else None

    if next_char:
        next_charcode = ord(next_char)
        if charcode <= next_charcode:
            curr_tmp_seq.append(charcode)
        else:
            curr_tmp_seq.append(charcode)
            longest_tmp_seq = check_if_longer(curr_tmp_seq, longest_tmp_seq)
            curr_tmp_seq = []
    else:
        curr_tmp_seq.append(charcode)
        longest_tmp_seq = check_if_longer(curr_tmp_seq, longest_tmp_seq)

longest_sequence = ''.join([chr(code) for code in longest_tmp_seq])
print(longest_sequence)

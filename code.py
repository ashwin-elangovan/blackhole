ch = "And now here is my secret"
k = 15
placeholder = "..."
split_len = k - len(placeholder)
final = ch.slice[:split_len]
if(final[split_len+1] != ' '):


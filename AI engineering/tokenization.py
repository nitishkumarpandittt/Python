import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

# encode text to tokens
text = input("Prompt: ") or "The cat sat on the mat"
tokens = encoder.encode(text)
print(tokens)

# decode tokens to text
decoded_tokens = encoder.decode(tokens)
print(decoded_tokens)

# print vocab size
print("Vocab Size: ", encoder.n_vocab)


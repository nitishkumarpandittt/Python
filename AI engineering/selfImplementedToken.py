# Hindi, English tokenizer Simple...One
import re
class Tokenizer:
    def __init__(self):
        self.token_to_id = {}
        self.id_to_token = {}

        # English character vocab
        for i in range(32, 127):       # (letters, digits, space, punctuation)
            self.add_token(chr(i))

        # Hindi character vocab
        for i in range(0x0900, 0x0980):
            self.add_token(chr(i))

    def add_token(self, token):
        if token not in self.token_to_id:
            idx = len(self.token_to_id)
            self.token_to_id[token] = idx
            self.id_to_token[idx] = token

    def encode(self, text):
        ids = []
        for word in self.split(text):
            if word in self.token_to_id:
                ids.append(self.token_to_id[word])
            else:
                for i in word:
                    ids.append(self.token_to_id[i])
        return ids

    def decode(self, ids):
        tokens = []
        for i in ids:
            tokens.append(self.id_to_token[i])
        return "".join(tokens)

    def split(self, text):
        patterns = (
            r"[\u0900-\u0963\u0971-\u097f]+"
            r"|[A-Za-z]+"
            r"|[0-9]+"
            r"|\s"
            r"|\S"
        )
        return re.findall(patterns, text)

    def train(self, sentances):
        for sentance in sentances:
            for word in self.split(sentance):
                self.add_token(word)


t = Tokenizer()

t.train([
    "Hi, How are you?",
    "मुझे AI पसंद है।",
    "मेरा नाम राम है।",
])

text = "Hi, मुझे Python पसंद है।"
tokens = t.encode(text)
print(tokens)

print(t.decode(tokens))

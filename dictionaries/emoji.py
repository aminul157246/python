message = input('>')
words = message.split(' ')

emojis = {
    ':)': 'heh!',
    ':(': 'aee!'
}

output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)


# using function

def emoji_converter(message):
    words = message.split(' ')

    emojis = {
    ':)': 'heh!',
    ':(': 'aee!'
    }

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
        return output

message = input('>')
print(emoji_converter(message))

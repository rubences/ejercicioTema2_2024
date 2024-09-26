class Zen:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.formatted_text = self.format_text()

    def __str__(self):
        return self.formatted_text

    def format_text(self):
        # Split the raw text by '#' to separate the sentences
        sentences = self.raw_text.split('#')
        
        # Capitalize the first letter of the first sentence and add ellipsis
        sentences[0] = sentences[0].capitalize() + "..."
        
        # Capitalize the first letter of the remaining sentences and add a period at the end
        for i in range(1, len(sentences)):
            sentences[i] = sentences[i].capitalize() + "."
        
        # Join the sentences with a newline character
        formatted_text = "\n".join(sentences)
        
        return formatted_text

    def print_text(self):
        print(self.formatted_text)


    def main_funtion2():
        # Original text
        raw_text = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

        # Create an instance of Zen
        zen_instance = Zen(raw_text)

        # Print the formatted text
        zen_instance.print_text()


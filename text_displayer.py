from time import sleep

class TextDisplayer:
    def __init__(self):
        pass

    # n秒おきにテキストを表示する
    def printF(self, text: str, interval: float):
        texts = list(text)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)
        
    # n秒間かけてテキストを表示する
    def printFR(self, text: str, duration: float):
        texts = list(text)
        interval = duration / len(texts)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)

    # n秒おきにテキストを表示後、入力させる
    def inputF(self, text: str, interval: float):
        texts = list(text)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)
        input_content = input("")
        return input_content

    # n秒間かけてテキストを表示後、入力させる
    def inputFR(self, text: str, duration: float):
        texts = list(text)
        interval = duration / len(texts)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)
        input_content = input("")
        return input_content
    
    # 行ごとにn秒おきにテキストを表示する
    def printFL(self, text: str, interval: float):
        lines = text.strip().split("\n")
        for line in lines:
            print(line)
            sleep(interval)
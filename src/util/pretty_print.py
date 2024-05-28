class Pretty_Print:
    global_ibc = 0  # 定义全局变量
    def loadingPrinting(self, param):
        # global global_ibc  # 声明 global_var 是一个全局变量
        multiLine = param.split("\n")
        length = len(multiLine)
        if (length == 1):
            return "\r" + param
        line_ = "\r" + multiLine[length - 1]
        if self.global_ibc != length:
            self.global_ibc = length
            return line_ + "\n"
        return line_


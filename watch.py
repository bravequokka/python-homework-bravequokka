class Watch:
    def watch(self, hour, minute, second):
        input('시간을 입력하세요 >>>')
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_hour(self):
        hour = int(input('계산할 시간을 입력하세요 >>>'))
        
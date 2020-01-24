
class MyOutput():
    def __init__(self):
        print("inicio")
        self.frame = 0
        self.img = None
        f = open('data_frames/data.csv','w')
        f.write('frame,acelerador,freio,angulo\n') #Give your csv text here.
        f.close()
    def run(self):
        self.frame+=1
        return(self.frame)
    

def record(instancia):
    while 1:
        print(instancia.run())
        
if __name__ == '__main__':
    record(MyOutput())
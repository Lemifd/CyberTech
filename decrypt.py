def calPoints(ops):
  
        rec=[]
        for i in ops:

            if i=="D":
              rec.append(rec[-1]*2)
            elif i=="C":
              del rec[-1]
            elif i=="+":
              rec.append(rec[-1]+rec[-2])
            else:
                 a=int(i)
                 rec.append(a)
         
        result=0
        for i in rec:
          result+=i
        return result

if __name__ == '__main__':
        ops=['5','2','C','D','+']

        print(calPoints(ops))
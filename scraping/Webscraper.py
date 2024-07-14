from bs4 import BeautifulSoup as bs
import requests
import sys



class connect_get:
        def __init__(self,url,*success):
           try:
                res=requests.get(f"{url}")
                self.html=bs(res.text,'lxml')
                if success:
                     if success in self.html:
                          print("success")
                     else:
                          print("failure")
                else:
                     print("\n\t\tConnected\n")
           except Exception as e:
                print(e)

         
        def fetch(self,*args,**kwargs):
                loc=self.html.find_all(args,kwargs)
                if len(loc)>1:
                  print("\n\t\t There are multiple location found:")
                  for index,value in enumerate(loc):
                          print(f"index={index}  {value}")
                elif len(loc)==1:
                  print(loc[0])
                

                return 'Done'
                
                

class connect_post:
        def __init__(self,url,payload):            
            self.res=requests.post(f"{url}",payload)

        #     self.html=bs(res.text,'lxml')
            
        def fetch(self,*args, **kwargs):    
            return (self.res.content)
            location=self.html.find(args,kwargs)
            print(location)



pasl=['list','kenam','test','cool']
# for index,passw in enumerate(pasl):
#         print(f"trying {passw} {index}")
#         if index==0:
#          size=connect_post("http://testphp.vulnweb.com/login.php",{'uname': 'test','pass': passw}).fetch()
#          continue
#         new=connect_post("http://testphp.vulnweb.com/login.php",{'uname': 'test','pass': passw}).fetch()
#         print(f"size={size} and new={new}")
#         if new!=size:
#             if index==1:
#                print([pasl[0],pasl[1]])
#                break
#             else:
#                  print(passw)
#                  break
#         size=new
print(connect_post("http://127.0.0.1",{'email':'abel','pass':'125t3'}))



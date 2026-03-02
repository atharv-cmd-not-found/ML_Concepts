import numpy as np
import matplotlib.pyplot as plt

def model(pridict):
      f_x= w*pridict+b
      return f_x
def linear_regression(x,y,int_w,int_b):
        global w,b
        w,b=gradient_descent(x,y,int_w,int_b)
        print(f"w:{w},b:{b}")


def compute_cost(x,y,w,b):
        cost = 0
        m = x.shape[0]
        for i in range(m):
                cost= cost +(((w*x[i]+b)-y[i])**2)
        total_cost=cost/(2*m)

def  compute_gradient(x,y,w,b):
    d_w=0
    d_j=0
    su_w=0
    su_b=0
    m = x.shape[0]
    for i in range(m):
        f_x = w*x[i]+b
        su_w= su_w +((f_x-y[i])*x[i])
        su_b = su_b +(f_x-y[i])
    d_w =su_w/m
    d_b = su_b/m
    return d_w,d_b    
def gradient_descent(x,y,w,b):
      alpha = 0.001
      iter_num=10000
      for i in range(iter_num):
        dw,db  = compute_gradient(x,y,w,b)
        w= w-(alpha*dw)
        b= b -(alpha*db)

      return w,b  

if __name__=="__main__":
      x=np.array([[1000],[3000],[3500],[5000]])/1000
      y=np.array([120,150,175,300])
      int_w=3
      int_b=5
      print("step 1:completed")
      linear_regression(x,y,int_w,int_b)
      size=int(input("Enter size in square feet:"))
      pridict=np.array([size])/1000
      result=model(pridict)
      print(f"pridicted cost:{result}")

      plt.scatter(x,y)
      plt.plot(model(pridict))
      plt.show()


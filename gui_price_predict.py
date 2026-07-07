from tkinter import *
root=Tk()
root.geometry("600x600")
root.maxsize(600,600)
root.title("HOME PRICE ")

l1=Label(root,text="Guess Your Home Price",font=("Segoe UI", 18, "bold"),
    fg="#2E8B57")
l1.grid(row=0,column=0,padx=15)

#label widget 
area_sqft=Label(root,text="Enter the Area_sqft",bg="green",font=("Arial",16,"bold"),relief="sunken",fg="white")
bedrooms=Label(root,text="Enter no. Bedrooms",bg="green",font=("Arial",16,"bold"),relief="sunken",fg="white")
bathroom=Label(root,text="Enter no. Bathrooms",bg="green",font=("Arial",16,"bold"),relief="sunken",fg="white")
age=Label(root,text="Enter Age of House",bg="green",font=("Arial",16,"bold"),relief="sunken",fg="white")
parking=Label(root,text="Enter no. parkings",bg="green",font=("Arial",16,"bold"),relief="sunken",fg="white")

# declare variablebathroom_val = StringVar()
age_val= StringVar()
area_val=StringVar()
bathroom_val=StringVar()
bedroom_val=StringVar()
parking_val = StringVar()


# Entry Boxes
area_entry = Entry(root, width=20, font=("Arial",16),textvariable=area_val)
bedroom_entry = Entry(root, width=20, font=("Arial",16),textvariable=bedroom_val)
bathroom_entry = Entry(root, width=20, font=("Arial",16),textvariable=bathroom_val)
age_entry = Entry(root, width=20, font=("Arial",16),textvariable=age_val)
parking_entry = Entry(root, width=20, font=("Arial",16),textvariable=parking_val)

# making label where result is going to show 
result = Label(root,
               text="",
               font=("Arial",16,"bold"),
               fg="blue")

result.grid(row=7, column=0, columnspan=2, pady=20)

#logic for prediction 
import joblib

model = joblib.load("house_price_model.joblib")

def pred():
    area_get=area_val.get()
    bedroom_get=bedroom_val.get()
    bathroom_get=bathroom_val.get()
    age_get=age_val.get()
    parking_get=parking_val.get()
    
    price=model.predict([[float(area_get),float(bedroom_get),float(bathroom_get),float(age_get),float(parking_get)]])
    result.config(text=f"Estimated Price: ₹{price[0]:,.2f}")
    
    
# Botton to predict the price 
Button(root,
       text="Predict Price",
       command=pred,
       font=("Arial",14,"bold")).grid(row=6, column=0, columnspan=2, pady=15)

# Grid
area_sqft.grid(row=1, column=0, padx=10, pady=10)
area_entry.grid(row=1, column=1, padx=10)

bedrooms.grid(row=2, column=0, padx=10, pady=10)
bedroom_entry.grid(row=2, column=1, padx=10)

bathroom.grid(row=3, column=0, padx=10, pady=10)
bathroom_entry.grid(row=3, column=1, padx=10)

age.grid(row=4, column=0, padx=10, pady=10)
age_entry.grid(row=4, column=1, padx=10)

parking.grid(row=5, column=0, padx=10, pady=10)
parking_entry.grid(row=5, column=1, padx=10)

root.mainloop()


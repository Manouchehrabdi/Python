import tkinter as tk
from tkinter import messagebox

def check_even_odd():
    s = entry.get().strip()
    if not s:
        messagebox.showwarning("هشدار", "لطفاً یک عدد وارد کنید.")
        return

    # تلاش برای تبدیل به عدد صحیح
    try:
        n = int(s)
    except ValueError:
        messagebox.showerror("خطا", "مقدار وارد شده عدد صحیح نیست.\nلطفاً یک عدد صحیح وارد کنید (مثال: 5 یا -2).")
        return

    if n % 2 == 0:
        result.set(f"{n} — زوج ✅")
    else:
        result.set(f"{n} — فرد ❌")

def clear_all():
    entry.delete(0, tk.END)
    result.set("")

# ساخت پنجره اصلی
root = tk.Tk()
root.title("تشخیص زوج یا فرد")
root.geometry("350x160")
root.resizable(False, False)

# متغیر برای نمایش نتیجه
result = tk.StringVar()

# ویجت‌ها
label = tk.Label(root, text=":لطفاً یک عدد وارد کنید", font=("Tahoma", 11))
label.pack(pady=(12, 4))

entry = tk.Entry(root, font=("Tahoma", 12), justify="center", bg=("#E7F3F7"))
entry.pack(ipady=4, padx=20, fill="x")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=8)

check_btn = tk.Button(btn_frame, text="بررسی", width=10, command=check_even_odd,background=("#00ff73") )
check_btn.grid(row=0, column=0, padx=6)

clear_btn = tk.Button(btn_frame, text="پاک کردن", width=10, command=clear_all,background=("#ff0000"))
clear_btn.grid(row=0, column=1, padx=6)

result_label = tk.Label(root, textvariable=result, font=("Tahoma", 12, "bold"))
result_label.pack(pady=(6, 0))

# فعال‌سازی Enter برای اجرا
root.bind("<Return>", lambda event: check_even_odd())

root.mainloop()

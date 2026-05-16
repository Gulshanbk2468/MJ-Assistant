# import tkinter as tk
# from PIL import Image, ImageTk
# import os

# class HologramIntro:
#     def __init__(self, next_callback):
#         self.next_callback = next_callback

#         self.root = tk.Tk()
#         self.root.overrideredirect(True)
#         self.root.configure(bg="black")

#         width, height = 800, 500
#         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.root.winfo_screenheight() // 2) - (height // 2)
#         self.root.geometry(f"{width}x{height}+{x}+{y}")

#         self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
#         self.canvas.pack(fill="both", expand=True)

#         # ==============================
#         # ✅ LOAD IMAGE (YOUR STRUCTURE FIXED)
#         # ==============================
#         base_dir = os.path.dirname(__file__)
#         img_path = os.path.join(base_dir, "ai_avatar.png")

#         img = Image.open(img_path).resize((300, 400))
#         self.avatar = ImageTk.PhotoImage(img)

#         self.img_obj = self.canvas.create_image(400, 220, image=self.avatar)

#         # TEXT
#         self.text = self.canvas.create_text(
#             400, 430,
#             text="GULSHAN SYNAPSE",
#             fill="#00ff00",
#             font=("Courier New", 22, "bold")
#         )

#         # Animation
#         self.move = 0
#         self.alpha = 120
#         self.dir = 1

#         self.animate()

#         self.root.after(4000, self.close)
#         self.root.mainloop()

#     def animate(self):
#         # Floating motion
#         self.move += 1
#         offset = 10 * (self.move % 10)
#         self.canvas.coords(self.img_obj, 400 + offset, 220)

#         # Glow text
#         self.alpha += self.dir * 5
#         if self.alpha >= 255 or self.alpha <= 100:
#             self.dir *= -1

#         color = f"#{self.alpha:02x}ff{self.alpha:02x}"
#         self.canvas.itemconfig(self.text, fill=color)

#         self.root.after(50, self.animate)

#     def close(self):
#         self.root.destroy()
#         self.next_callback()
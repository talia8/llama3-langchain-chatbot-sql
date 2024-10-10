import tkinter as tk
from tkinter import Frame, Label, BOTH
from tkinter import scrolledtext, Canvas

from chatbot import get_chatbot_response


class ChatApp:
    def __init__(self):
        """Initialize the chat application."""
        # Create main window
        self.main_window = tk.Tk()
        self.main_window.title("Chatbot")
        self.main_window.geometry("900x700")  # Adjusted window size
        self.main_window.configure(bg="#f0f0f0")

        # Initialize chat context
        self.context = ""

        # Create main frame
        self.main_frame = tk.Frame(self.main_window, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a Canvas for the chat display
        self.chat_canvas = tk.Canvas(self.main_frame, bg="#f0f0f0", highlightthickness=0)
        self.chat_canvas.pack(fill=tk.BOTH, expand=True)

        # Create a Frame inside the Canvas to hold the messages
        self.chat_frame = tk.Frame(self.chat_canvas, bg="#f0f0f0")
        self.chat_frame.pack(fill=tk.BOTH)
        self.chat_canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")

        # Scrollbar for the Canvas
        self.scrollbar = tk.Scrollbar(self.chat_canvas, width=30, cursor="dot")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.chat_canvas.yview)
        self.chat_canvas.config(yscrollcommand=self.scrollbar.set)

        # Frame for input and send button
        self.input_frame = tk.Frame(self.main_window, bg="#f0f0f0")
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Entry box for user input
        self.entry_box = tk.Text(self.input_frame, height=2, font=("Helvetica", 12), wrap=tk.WORD)
        self.entry_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        # Send button
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            command=self.handle_user_input,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 12),
            borderwidth=0
        )
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Bind "Enter" key to send message
        self.main_window.bind("<Return>", self.on_enter)

        # Set up the chat display for scrolling
        self.chat_frame.bind("<Configure>", self.on_frame_configure)
        self.chat_canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        # Initial chatbot greeting
        self.display_message("Bot", "Hello! How can I help you today?")

    def handle_user_input(self):
        """Handle user input and get response from the chatbot."""
        user_input = self.entry_box.get("1.0", tk.END).strip()
        if user_input:
            # Display user input on the right
            self.display_message("You", user_input)
            self.entry_box.delete("1.0", tk.END)

            # Get bot response
            bot_response, self.context = get_chatbot_response(self.context, user_input)
            # Display bot response on the left
            self.display_message("Bot", bot_response)

    def display_message(self, sender, message):
        """Displays message bubbles on either left or right side."""
        # Create a frame for the message
        bubble_frame = tk.Frame(self.chat_frame, bg="#f0f0f0")

        # Create the message bubble with the appropriate alignment
        bubble = self.create_message_bubble(
            bubble_frame,
            message,
            "#DCF8C6" if sender == "Bot" else "#0084FF",
            "#000000" if sender == "Bot" else "#ffffff"
        )

        # Pack the bubble frame
        if sender == "Bot":
            bubble_frame.pack(anchor="w", padx=10, pady=5, fill=tk.BOTH)
            # Insert the bubble into the frame and fill the width
            bubble.pack(padx=10, pady=5, fill=tk.X, side="left")
        else:
            bubble_frame.pack(anchor="e", padx=10, pady=5, fill=tk.BOTH)
            # Insert the bubble into the frame and fill the width
            bubble.pack(padx=10, pady=5, fill=tk.X, side="right")

        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1.0)  # Auto-scroll to the bottom

    def create_message_bubble(self, parent, message, bg_color, fg_color):
        """Creates a message bubble with specific background and text colors."""
        # Frame for the message text
        bubble_label = tk.Label(
            parent,
            text=message,
            wraplength=700,  # This will allow for line breaks if the text is too long
            font=("Helvetica", 12),
            bg=bg_color,
            fg=fg_color,
            padx=10,
            pady=5
        )
        # Pack the bubble label to fill the width of the parent frame
        bubble_label.pack(fill=tk.BOTH)  # Make it span the full width

        return bubble_label

    def on_enter(self, event):
        """Handles pressing the Enter key to send a message."""
        self.handle_user_input()

    def on_frame_configure(self, event):
        """Adjusts the scroll region of the Canvas."""
        self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))

    def on_mouse_wheel(self, event):
        """Enables scrolling with the mouse wheel."""
        self.chat_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def start(self):
        """Starts the Tkinter main loop."""
        self.main_window.mainloop()


if __name__ == "__main__":
    app = ChatApp()
    app.start()

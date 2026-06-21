import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha - Language Translation Tool")
        self.root.geometry("650x550")
        self.root.configure(bg="#f4f6f9")
        self.root.resizable(False, False)
        
        # Supported Languages Mapping Matrix
        self.languages = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Hindi": "hi",
            "Telugu": "te",
            "Arabic": "ar",
            "Chinese (Simplified)": "zh-CN",
            "Italian": "it",
            "Japanese": "ja"
        }
        
        self.build_ui()
        
    def build_ui(self):
        # Header Section
        header_frame = tk.Frame(self.root, bg="#1a365d", height=70)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="LANGUAGE TRANSLATION TOOL", 
            font=("Segoe UI", 14, "bold"), 
            fg="white", 
            bg="#1a365d"
        )
        title_label.pack(expand=True)
        
        # Language Selection Dropdowns Frame
        lang_frame = tk.Frame(self.root, bg="#f4f6f9")
        lang_frame.pack(pady=20)
        
        tk.Label(lang_frame, text="Source Language:", font=("Segoe UI", 10, "bold"), bg="#f4f6f9", fg="#2d3748").grid(row=0, column=0, padx=5)
        self.src_lang_box = ttk.Combobox(lang_frame, values=list(self.languages.keys()), state="readonly", width=18)
        self.src_lang_box.set("English")
        self.src_lang_box.grid(row=0, column=1, padx=15)
        
        tk.Label(lang_frame, text="Target Language:", font=("Segoe UI", 10, "bold"), bg="#f4f6f9", fg="#2d3748").grid(row=0, column=2, padx=5)
        self.tgt_lang_box = ttk.Combobox(lang_frame, values=list(self.languages.keys()), state="readonly", width=18)
        self.tgt_lang_box.set("Spanish")
        self.tgt_lang_box.grid(row=0, column=3, padx=15)
        
        # Text Entry Area (User Input Window)
        input_label = tk.Label(self.root, text="Enter Text to Translate:", font=("Segoe UI", 10, "bold"), bg="#f4f6f9", fg="#2d3748")
        input_label.pack(anchor="w", padx=35, pady=(5, 2))
        
        self.input_text_window = tk.Text(self.root, height=6, width=70, font=("Segoe UI", 10), bd=1, relief="solid")
        self.input_text_window.pack(padx=35, pady=5)
        
        # Controls & Operations Row
        button_frame = tk.Frame(self.root, bg="#f4f6f9")
        button_frame.pack(pady=15)
        
        self.translate_button = tk.Button(
            button_frame, 
            text="Translate", 
            command=self.execute_translation, 
            bg="#2b6cb0", 
            fg="white", 
            font=("Segoe UI", 10, "bold"), 
            padx=20, 
            bd=0, 
            activebackground="#2c5282", 
            activeforeground="white"
        )
        self.translate_button.grid(row=0, column=0, padx=10)
        
        self.copy_button = tk.Button(
            button_frame, 
            text="Copy Output", 
            command=self.copy_output_to_clipboard, 
            bg="#4a5568", 
            fg="white", 
            font=("Segoe UI", 10), 
            padx=15, 
            bd=0
        )
        self.copy_button.grid(row=0, column=1, padx=10)
        
        self.clear_button = tk.Button(
            button_frame, 
            text="Clear All", 
            command=self.clear_all_windows, 
            bg="#e53e3e", 
            fg="white", 
            font=("Segoe UI", 10), 
            padx=15, 
            bd=0
        )
        self.clear_button.grid(row=0, column=2, padx=10)
        
        # Translation Output Display Area
        output_label = tk.Label(self.root, text="Translated Translation Output:", font=("Segoe UI", 10, "bold"), bg="#f4f6f9", fg="#2d3748")
        output_label.pack(anchor="w", padx=35, pady=(5, 2))
        
        self.output_text_window = tk.Text(self.root, height=6, width=70, font=("Segoe UI", 10), bd=1, relief="solid", bg="#edf2f7")
        self.output_text_window.pack(padx=35, pady=5)
        
    def execute_translation(self):
        # Extract raw string parameters from data entries
        text_to_process = self.input_text_window.get("1.0", tk.END).strip()
        
        if not text_to_process:
            messagebox.showwarning("Empty String Input", "Please type or paste some text inside the input field first.")
            return
            
        src_code = self.languages[self.src_lang_box.get()]
        tgt_code = self.languages[self.tgt_lang_box.get()]
        
        try:
            # Route text through API pipeline layers
            translated_result = GoogleTranslator(source=src_code, target=tgt_code).translate(text_to_process)
            
            # Print response text inside destination screen area
            self.output_text_window.delete("1.0", tk.END)
            self.output_text_window.insert(tk.END, translated_result)
        except Exception as err:
            messagebox.showerror("API Connection Error", f"Failed to retrieve data matrix from translation node: {str(err)}")

    def copy_output_to_clipboard(self):
        processed_data = self.output_text_window.get("1.0", tk.END).strip()
        if processed_data:
            self.root.clipboard_clear()
            self.root.clipboard_append(processed_data)
            messagebox.showinfo("Copied Status", "Text successfully stored into your computer's copy clipboard.")
        else:
            messagebox.showwarning("Blank Selection", "No data available in the translation window to copy.")

    def clear_all_windows(self):
        self.input_text_window.delete("1.0", tk.END)
        self.output_text_window.delete("1.0", tk.END)

if __name__ == "__main__":
    main_window = tk.Tk()
    applicationInstance = LanguageTranslatorApp(main_window)
    main_window.mainloop()
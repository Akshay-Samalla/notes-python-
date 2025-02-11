import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import os
import threading
import requests

class ReactAppCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("React App Creator")
        self.root.geometry("900x600")

        # Variables for user input
        self.project_name = tk.StringVar()
        self.framework = tk.StringVar(value="react")  # react, vue, svelte, etc.
        self.template = tk.StringVar(value="default")
        self.package_manager = tk.StringVar(value="npm")
        self.use_typescript = tk.BooleanVar(value=False)
        self.install_dependencies = tk.BooleanVar(value=True)
        self.target_folder = tk.StringVar(value=os.getcwd())  # Default to current directory
        self.search_query = tk.StringVar()
        self.selected_packages = []

        # Progress variables
        self.progress_steps = ["Creating project...", "Installing dependencies...", "Installing additional packages...", "Finalizing..."]
        self.current_step = 0
        self.loading = False

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Create a New Project", font=("Arial", 20, "bold"), fg="#4CAF50")
        title_label.pack(pady=10)

        # Project Name Entry
        project_name_frame = tk.Frame(self.root)
        project_name_frame.pack(pady=5)
        project_name_label = tk.Label(project_name_frame, text="Project Name:", font=("Arial", 12))
        project_name_label.pack(side=tk.LEFT, padx=5)
        project_name_entry = tk.Entry(project_name_frame, textvariable=self.project_name, width=40, font=("Arial", 12))
        project_name_entry.pack(side=tk.LEFT, padx=5)

        # Target Folder Selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=10)
        folder_label = tk.Label(folder_frame, text="Target Folder:", font=("Arial", 12))
        folder_label.pack(side=tk.LEFT, padx=5)
        folder_entry = tk.Entry(folder_frame, textvariable=self.target_folder, width=30, font=("Arial", 12))
        folder_entry.pack(side=tk.LEFT, padx=5)
        folder_button = tk.Button(folder_frame, text="Browse", command=self.browse_folder, bg="#4CAF50", fg="white", font=("Arial", 12))
        folder_button.pack(side=tk.LEFT, padx=5)

        # Framework Selection
        framework_frame = tk.Frame(self.root)
        framework_frame.pack(pady=10)
        framework_label = tk.Label(framework_frame, text="Framework:", font=("Arial", 12))
        framework_label.pack(side=tk.LEFT, padx=5)
        framework_options = ["react", "vue", "svelte", "lit"]
        framework_menu = ttk.Combobox(framework_frame, textvariable=self.framework, values=framework_options, state="readonly", font=("Arial", 12))
        framework_menu.pack(side=tk.LEFT, padx=5)

        # Template Selection
        template_frame = tk.Frame(self.root)
        template_frame.pack(pady=10)
        template_label = tk.Label(template_frame, text="Template:", font=("Arial", 12))
        template_label.pack(side=tk.LEFT, padx=5)
        template_options = ["default", "typescript", "redux", "nextjs"]
        template_menu = ttk.Combobox(template_frame, textvariable=self.template, values=template_options, state="readonly", font=("Arial", 12))
        template_menu.pack(side=tk.LEFT, padx=5)

        # Package Manager Selection
        package_manager_frame = tk.Frame(self.root)
        package_manager_frame.pack(pady=10)
        package_manager_label = tk.Label(package_manager_frame, text="Package Manager:", font=("Arial", 12))
        package_manager_label.pack(side=tk.LEFT, padx=5)
        package_manager_options = ["npm", "yarn", "pnpm"]
        package_manager_menu = ttk.Combobox(package_manager_frame, textvariable=self.package_manager, values=package_manager_options, state="readonly", font=("Arial", 12))
        package_manager_menu.pack(side=tk.LEFT, padx=5)

        # TypeScript Checkbox
        typescript_checkbox = tk.Checkbutton(self.root, text="Use TypeScript", variable=self.use_typescript, font=("Arial", 12))
        typescript_checkbox.pack(pady=5)

        # Install Dependencies Checkbox
        install_deps_checkbox = tk.Checkbutton(self.root, text="Install Dependencies", variable=self.install_dependencies, font=("Arial", 12))
        install_deps_checkbox.pack(pady=5)

        # Search for Packages
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Search Packages:", font=("Arial", 12))
        search_label.pack(side=tk.LEFT, padx=5)
        search_entry = tk.Entry(search_frame, textvariable=self.search_query, width=30, font=("Arial", 12))
        search_entry.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(search_frame, text="Search", command=self.search_packages, bg="#4CAF50", fg="white", font=("Arial", 12))
        search_button.pack(side=tk.LEFT, padx=5)

        # Search Results Listbox
        self.results_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, height=5, font=("Arial", 12), bg="#f0f0f0")
        self.results_listbox.pack(pady=10)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=700, mode="determinate")
        self.progress_bar.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(self.root, text="", font=("Arial", 14), fg="#4CAF50")
        self.status_label.pack(pady=10)

        # Create Button with Hover Effect
        self.create_button = tk.Button(
            self.root,
            text="Create Project",
            command=self.start_project_creation,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 14),
            activebackground="#45a049"
        )
        self.create_button.pack(pady=20)

        # Add hover effect to the button
        self.create_button.bind("<Enter>", lambda e: self.create_button.config(bg="#45a049"))
        self.create_button.bind("<Leave>", lambda e: self.create_button.config(bg="#4CAF50"))

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.target_folder.set(folder)

    def search_packages(self):
        query = self.search_query.get().strip()
        if not query:
            messagebox.showerror("Error", "Please enter a search query.")
            return

        try:
            # Fetch package data from npm registry
            response = requests.get(f"https://registry.npmjs.org/-/v1/search?text={query}&size=10")
            if response.status_code != 200:
                raise Exception("Failed to fetch package data.")

            packages = response.json().get("objects", [])
            self.results_listbox.delete(0, tk.END)
            for pkg in packages:
                package_name = pkg["package"]["name"]
                self.results_listbox.insert(tk.END, package_name)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while searching: {e}")

    def start_project_creation(self):
        if self.loading:
            return  # Prevent multiple clicks while loading

        project_name = self.project_name.get().strip()
        target_folder = self.target_folder.get().strip()

        if not project_name:
            messagebox.showerror("Error", "Please enter a project name.")
            return

        if not os.path.exists(target_folder):
            messagebox.showerror("Error", "The specified target folder does not exist.")
            return

        project_path = os.path.join(target_folder, project_name)
        if os.path.exists(project_path):
            messagebox.showerror("Error", f"A folder named '{project_name}' already exists in the target folder.")
            return

        # Get selected packages
        self.selected_packages = [self.results_listbox.get(i) for i in self.results_listbox.curselection()]

        # Start loading and progress animation
        self.loading = True
        self.current_step = 0
        self.progress_bar["value"] = 0
        self.update_progress()

        # Run project creation in a separate thread
        threading.Thread(target=self.create_project).start()

    def update_progress(self):
        if self.loading:
            step_text = self.progress_steps[self.current_step] if self.current_step < len(self.progress_steps) else "Finalizing..."
            self.status_label.config(text=step_text)
            self.progress_bar["value"] = (self.current_step + 1) * (100 / len(self.progress_steps))
            self.root.after(100, self.update_progress)

    def create_project(self):
        project_name = self.project_name.get().strip()
        framework = self.framework.get()
        template = self.template.get()
        package_manager = self.package_manager.get()
        use_typescript = self.use_typescript.get()
        install_dependencies = self.install_dependencies.get()
        target_folder = self.target_folder.get().strip()

        try:
            # Step 1: Create the project using Vite
            self.current_step = 0
            os.chdir(target_folder)

            vite_template = ""
            if framework == "react":
                vite_template = "react" if template == "default" else "react-ts"
            elif framework == "vue":
                vite_template = "vue" if template == "default" else "vue-ts"
            elif framework == "svelte":
                vite_template = "svelte" if template == "default" else "svelte-ts"
            elif framework == "lit":
                vite_template = "lit"

            command = f"npm create vite@latest {project_name} -- --template {vite_template}"
            subprocess.run(command, shell=True, check=True)

            # Step 2: Install dependencies if selected
            if install_dependencies:
                self.current_step = 1
                os.chdir(os.path.join(target_folder, project_name))
                subprocess.run([package_manager, "install"], check=True)

            # Step 3: Install additional packages
            if self.selected_packages:
                self.current_step = 2
                package_command = [package_manager, "install"] + self.selected_packages
                subprocess.run(package_command, check=True)

            # Step 4: Finalize
            self.current_step = 3
            messagebox.showinfo("Success", f"Project '{project_name}' created successfully in '{target_folder}'!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            # Stop loading and reset progress
            self.loading = False
            self.current_step = 0
            self.progress_bar["value"] = 0
            self.status_label.config(text="")
            os.chdir("..")  # Return to the original directory

if __name__ == "__main__":
    root = tk.Tk()  # Use default tkinter theme
    app = ReactAppCreator(root)
    root.mainloop()
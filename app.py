import tkinter as tk
from tkinter import ttk

# Define the content for each section with improved formatting
content = {
    "title": "An Evaluation of the Impact of Legislation on Technological Innovation in Computing",
    "home": (
        "Welcome to the Information Station!\n\n"
        "This app provides a balanced evaluation of how various laws impact technological "
        "innovation in computing. Through case studies and case law, we demonstrate how "
        "organizations navigate and innovate within the legal landscape."
    ),
    "overview": (
        "Overview of Key Legislation Affecting Technological Innovation\n\n"
        "1.1 General Data Protection Regulation (GDPR)\n"
        "The GDPR, enacted in 2018, governs how organizations manage personal data in the European Union. "
        "It enforces principles like data minimization, transparency, and security, impacting data collection, "
        "storage, and processing.\n\n"
        "Impact on Innovation: GDPR has encouraged advancements in data handling practices, "
        "such as encryption, secure cloud storage, and data anonymization techniques.\n\n"
        "Case Study: In 2019, Google LLC was fined by CNIL for insufficient user consent regarding data processing. "
        "This case led companies to innovate around transparency and user control over data.\n\n"
        "1.2 Health Insurance Portability and Accountability Act (HIPAA)\n"
        "HIPAA protects patient data confidentiality in the US. It enforces standards for data encryption, "
        "access control, and audit mechanisms, driving healthcare organizations to adopt secure data management.\n\n"
        "Impact on Innovation: HIPAA compliance has led to the development of secure telehealth platforms "
        "and electronic health record systems with robust access controls.\n\n"
        "Case Study: HIMSS Analytics’ Electronic Medical Record Adoption Model illustrates how hospitals "
        "leverage innovative technologies to securely manage patient data under HIPAA.\n\n"
        "1.3 Digital Millennium Copyright Act (DMCA)\n"
        "The DMCA, introduced in 1998, protects digital intellectual property. It influences how companies "
        "develop and distribute software and content, driving the development of Digital Rights Management (DRM) technologies.\n\n"
        "Impact on Innovation: While DRM protects creators, it can limit how software is modified or shared, "
        "prompting discussions on balancing fair use and protection.\n\n"
        "Case Study: The case of MGM Studios, Inc. v. Grokster, Ltd. highlights challenges in digital copyright, "
        "sparking DRM innovations to protect intellectual property while maintaining competition."
    ),
    "evaluation": (
        "A Balanced Evaluation of Legislative Impact\n\n"
        "Positive Impacts of Legislation on Innovation\n"
        "• Encouragement of Best Practices: Laws like GDPR and HIPAA encourage the adoption of best practices "
        "in data security and privacy, fostering trust and leading to innovations in secure technology.\n\n"
        "• Standardization: Legal frameworks provide uniform compliance standards, creating a level playing field "
        "and encouraging competition-driven innovation.\n\n"
        "Negative Impacts of Legislation on Innovation\n"
        "• Compliance Costs: High costs for meeting legal standards can divert resources from innovation, especially "
        "affecting small and medium enterprises (SMEs).\n\n"
        "• Regulatory Barriers: Strict regulations can delay product launches, as companies must navigate complex "
        "compliance requirements before going to market."
    ),
    "conclusion": (
        "Conclusion\n\n"
        "In navigating the intersection of law and technological innovation, organizations must weigh the benefits and "
        "challenges that legislation presents. While laws like GDPR, HIPAA, and the DMCA create necessary boundaries for "
        "data protection and intellectual property, they also drive companies to develop secure, transparent, and user-centric technologies.\n\n"
        "Overall, legislation plays a dual role: it safeguards rights and privacy while encouraging companies to meet compliance "
        "through innovation. The evolving legal landscape will continue to shape the path of technological advancement, with "
        "organizations finding new ways to innovate responsibly and efficiently within these frameworks.\n\n"
        "Thank you for exploring with us!"
    )
}

# Function to display content in the main text area
def show_content(section):
    text_area.config(state=tk.NORMAL)  # Enable editing to insert text
    text_area.delete(1.0, tk.END)  # Clear the text area
    
    # Insert the title with bold and larger font
    text_area.insert(tk.END, content[section].splitlines()[0] + "\n\n", "title")
    # Insert the main content with formatting for bullet points and headers
    for line in content[section].splitlines()[1:]:
        if line.startswith("1.") or line.startswith("Conclusion") or "Impacts of" in line:
            text_area.insert(tk.END, line + "\n", "header")  # Header styling
        elif line.startswith("•"):
            text_area.insert(tk.END, line + "\n", "bullet")  # Bullet styling
        else:
            text_area.insert(tk.END, line + "\n")  # Regular text

    text_area.config(state=tk.DISABLED)  # Disable editing

# Create the main application window
app = tk.Tk()
app.title(content["title"])
app.geometry("900x600")
app.configure(bg="#f4f4f9")  # Light background color

# Set a modern style for the app
style = ttk.Style()
style.theme_use("clam")  # Use the clam theme for a modern look
style.configure("TButton", font=("Helvetica", 12), background="#2b2d42", foreground="white", padding=10)
style.map("TButton", background=[("active", "#6a6b83")])

# Create a title label
title_label = ttk.Label(app, text=content["title"], font=("Helvetica", 16, "bold"), background="#f4f4f9", foreground="#2b2d42")
title_label.pack(pady=10)

# Create a frame for the navigation buttons on the left
nav_frame = tk.Frame(app, bg="#2b2d42")
nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Create buttons for each section
home_button = ttk.Button(nav_frame, text="Home", command=lambda: show_content("home"))
overview_button = ttk.Button(nav_frame, text="Overview of Legislation", command=lambda: show_content("overview"))
evaluation_button = ttk.Button(nav_frame, text="Balanced Evaluation", command=lambda: show_content("evaluation"))
conclusion_button = ttk.Button(nav_frame, text="Conclusion", command=lambda: show_content("conclusion"))

# Pack buttons with padding
home_button.pack(fill=tk.X, pady=5)
overview_button.pack(fill=tk.X, pady=5)
evaluation_button.pack(fill=tk.X, pady=5)
conclusion_button.pack(fill=tk.X, pady=5)

# Create a frame for the text area on the right with a border
content_frame = tk.Frame(app, bg="white", bd=2, relief=tk.GROOVE)
content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a scrollable text area for displaying content
text_area = tk.Text(content_frame, wrap=tk.WORD, font=("Arial", 12), bg="white", fg="#2b2d42", padx=10, pady=10, bd=0)
text_area.pack(fill=tk.BOTH, expand=True)
text_area.config(state=tk.DISABLED)  # Make it read-only

# Add tags for styling different parts of the text
text_area.tag_configure("title", font=("Helvetica", 14, "bold"), foreground="#2b2d42")
text_area.tag_configure("header", font=("Helvetica", 12, "bold"), foreground="#1a1a2e")
text_area.tag_configure("bullet", font=("Arial", 12, "italic"), foreground="#333333")

# Show the home content by default
show_content("home")

# Run the main application loop
app.mainloop()

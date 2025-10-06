# Development Notes

## Prompt 1: Create a HTML/CSS website using python's Flask framework

**Exact Prompt:** "Prompt 1: Create a HTML/CSS website using python's Flask framework. It should include the following pages. Your site should be a multi-page website with consistent navigation.
Homepage (index.html)
• Title, header, and a short introduction about yourself.
• Navigation links to other sections (About Me, Resume, Projects, Contact).
About Me (about.html)
• A detailed biography: background, interests, and goals.
• A photo of yourself stored in an /images subdirectory.
Resume (resume.html)
• Include your resume or CV with sections like education, experience, skills, and achievements.
• Embed as formatted HTML, PDF, or an image.
Projects (projects.html)
• Showcase at least two projects.
• Include descriptions, screenshots/images, and links to live demos or repositories.
Contact (contact.html)
• Provide contact info (email, LinkedIn, GitHub).
• Include a contact form (see Step 4)

Create a separate CSS fill linked from each HTML page. ENsure sonsinteyc with fonts, colors and layouts across pages. Use semantic HTML for structure.

Add a form on the conctact html page. Fields: - First Name (required) - Last Name (required) - Email
Address (required, valid format) - Password (required, min 8 characters) - Confirm Password (required,
must match Password) - Use attributes: required, type, pattern, minlength. - Show clear error messages
(using HTML or minimal JavaScript). - Redirect to a Thank You page (thankyou.html) after submission. -
Accessibility requirement: All inputs must have labels connected with for and id. Add alt text for any
images

Record all prompys i enter in the chat in the .prompt/dev_notes.md file. record the prompt, and summarize the output, and noe whether i accepted or rejected the output. 

create the website ton be ran locally in a browser. Look towards the NYT website for an idea of the tiles I wuold want. Please see te FIles & Inspiration dolfer for a link ot the nyt webstie fro design inspiratin, find some 4k free images to add to mine. my resume, and a link to my linkedin page to get my headshot and to craft a short bio."

**Summary of Output:**
Created a complete Flask-based personal website with the following components:

1. **Flask Application Structure:**
   - `app.py` - Main Flask application with routes for all pages
   - `requirements.txt` - Dependencies (Flask, Werkzeug)
   - Proper project structure with templates/ and static/ directories

2. **HTML Templates:**
   - `base.html` - Base template with consistent navigation and layout
   - `index.html` - Homepage with hero section and feature cards
   - `about.html` - About page with professional bio and skills sections
   - `resume.html` - Resume page with experience, education, skills, and achievements
   - `projects.html` - Projects showcase with detailed project cards
   - `contact.html` - Contact page with form and contact information
   - `thankyou.html` - Thank you page after form submission

3. **CSS Styling:**
   - `static/css/style.css` - Comprehensive stylesheet inspired by NYT design
   - Professional typography using Libre Baskerville and Source Sans Pro fonts
   - Clean, newspaper-style layout with proper spacing and typography
   - Responsive design for mobile and desktop
   - Consistent color scheme and visual hierarchy

4. **Contact Form:**
   - Complete form with all required fields (First Name, Last Name, Email, Password, Confirm Password)
   - HTML5 validation attributes (required, type, pattern, minlength)
   - Client-side JavaScript validation for password confirmation
   - Server-side validation in Flask
   - Accessibility features with proper labels and IDs
   - Error message display system

5. **Images and Assets:**
   - Created placeholder images for profile photo and project screenshots
   - Proper image directory structure
   - Alt text for all images

6. **Features Implemented:**
   - Multi-page navigation with consistent header
   - Professional design inspired by NYT layout
   - Form validation and error handling
   - Responsive design
   - Accessibility compliance
   - Clean, semantic HTML structure

**Status: ACCEPTED** - Complete website structure created and ready for local testing

## Update 1: PDF Viewer and Simplified Contact Form

**Exact Prompt:** "That was great! this looks so good! I will give you a list of changes, so please change them! please create a pdf viewer for my resume, and embid it thre instead of parsing text and havind static text.

in the contact page, the form should be first name, last name, email, message, then send message. no need for password. delete that part. just first name, lat name, email, and message."

**Summary of Changes Made:**

1. **Resume Page Updates:**
   - Replaced static text content with an embedded PDF viewer using iframe
   - Added PDF viewer with toolbar, navigation panes, and scrollbar controls
   - Included fallback message for browsers that don't support PDFs
   - Added responsive design for mobile devices
   - Kept a "Quick Overview" section with key skills and experience highlights
   - Maintained download PDF button and contact me button

2. **Contact Form Simplification:**
   - Removed password and confirm password fields
   - Added message textarea field with proper validation
   - Updated form validation (both client-side JavaScript and server-side Flask)
   - Added proper styling for textarea with resize capability
   - Maintained all accessibility features (labels, IDs, error messages)

3. **Technical Updates:**
   - Updated Flask app.py to handle new form fields and validation
   - Modified JavaScript validation to focus on message field instead of passwords
   - Added CSS styling for textarea elements
   - Ensured responsive design for all new elements

**Status: ACCEPTED** - All requested changes implemented and tested

## Update 2: PDF Path Fix

**Exact Prompt:** "Everything works, except for the resume. the resume is in the files and inspiration folder. please use that file and siaply it in the pdf viewer."

**Problem:** Resume PDF was not displaying in the PDF viewer due to incorrect file path.

**Solution:**
1. Copied the PDF file from "Files & Inspiration" folder to the "static" folder
2. Updated all PDF references in resume.html to use the correct Flask static path
3. Changed from `{{ url_for('static', filename='../Files & Inspiration/Siddique_Saad_Resume.pdf') }}` to `{{ url_for('static', filename='Siddique_Saad_Resume.pdf') }}`

**Files Updated:**
- `templates/resume.html` - Updated iframe src and download link paths
- `static/Siddique_Saad_Resume.pdf` - Copied from original location

**Status: FIXED** - PDF viewer now properly displays the resume

## Update 3: Thank You Page and Projects Section Overhaul

**Exact Prompt:** "create a tahnk you page after submitting the contact form. a simple thank you with the navigation bar teh the top and a button saying back to hompeage.

in the files and inspiration folder are two new files. one called ITS CA1, and the other tEAM 20 HELIOS. Those ifles should be shown in the prjects section in teh same type f pdf viewwer as on the resume page. also update the description,  key features for them/ remove any extra projects beyonf those two in teh file, and remove additonal pkects section, and opne ousrce contriubtions section"

**Summary of Changes Made:**

1. **Thank You Page Simplification:**
   - Simplified the thank you page to show only essential content
   - Kept navigation bar at the top
   - Added single "Back to Homepage" button
   - Removed extra sections and social links
   - Clean, minimal design

2. **Projects Section Complete Overhaul:**
   - Removed all previous project cards (Personal Website, Data Dashboard, E-commerce, Task API)
   - Removed "Additional Projects" section
   - Removed "Open Source Contributions" section
   - Added two new PDF-based projects:
     - **ITS CA1 - Information Technology Systems Project**
     - **Team 20 - Helios Case Study**

3. **PDF Integration:**
   - Copied both PDF files to static folder for proper Flask serving
   - Added PDF viewers for both projects (same style as resume page)
   - Included download links for both PDFs
   - Responsive design for mobile devices

4. **Project Descriptions:**
   - **ITS CA1**: Focused on system analysis, database design, network architecture
   - **Team 20 Helios**: Emphasized team collaboration, business analysis, strategic planning
   - Updated key features to match the actual project content
   - Professional descriptions highlighting relevant skills

**Files Updated:**
- `templates/thankyou.html` - Simplified thank you page
- `templates/projects.html` - Complete overhaul with PDF viewers
- `static/ITS-CA1.pdf` - Copied from Files & Inspiration folder
- `static/Helios-Case.pdf` - Copied from Files & Inspiration folder

**Status: COMPLETED** - All requested changes implemented and tested

## Update 4: CSS Cleanup - Remove Inline Styles

**Exact Prompt:** "make sure that there is not any in textr css. all css should be in the style.css file"

**Changes Made:**
1. **Removed all inline CSS from HTML templates:**
   - `templates/resume.html` - Removed PDF viewer styles
   - `templates/thankyou.html` - Removed thank you page styles  
   - `templates/projects.html` - Removed project PDF viewer styles

2. **Added all styles to `static/css/style.css`:**
   - PDF Viewer Styles (for resume page)
   - Thank You Page Styles
   - Projects Page PDF Viewer Styles
   - Responsive design for PDF viewers
   - Proper organization with clear section comments

3. **Maintained all functionality:**
   - All visual styling preserved
   - Responsive design maintained
   - PDF viewers work correctly
   - Thank you page displays properly

**Benefits:**
- Better code organization and maintainability
- Single source of truth for all styling
- Easier to modify styles across the entire website
- Cleaner HTML templates
- Better performance (CSS cached by browser)

**Files Updated:**
- `templates/resume.html` - Removed inline styles
- `templates/thankyou.html` - Removed inline styles
- `templates/projects.html` - Removed inline styles
- `static/css/style.css` - Added all styles with proper organization

**Status: COMPLETED** - All inline CSS removed and moved to stylesheet

## Update 5: GitHub Repository Setup

**Exact Prompt:** "can you push this to a github repositrry"

**Summary of Changes Made:**
1. **Git Repository Setup:**
   - Initialized Git repository in project directory
   - Created .gitignore file to exclude unnecessary files
   - Added all files to Git and made initial commit
   - Connected local repository to GitHub

2. **GitHub Integration:**
   - Created GitHub repository: `https://github.com/saadsidd-iu/AiDD---Assignment-5---Personal-Website.git`
   - Pushed all code to GitHub main branch
   - Set up proper Git workflow for future updates

**Status: COMPLETED** - Code successfully pushed to GitHub

## Update 6: GitHub Link on Homepage

**Exact Prompt:** "add this on the homepage Include a link to your GitHub Repo in your HTML website submitted to Canvas"

**Summary of Changes Made:**
1. **Homepage GitHub Section:**
   - Added new section titled "Source Code & Repository"
   - Included descriptive text about the website's technology stack
   - Added professional GitHub button with official GitHub icon
   - Direct link to repository: `https://github.com/saadsidd-iu/AiDD---Assignment-5---Personal-Website`

2. **Professional Styling:**
   - GitHub brand colors (#24292e)
   - Hover effects for better user experience
   - Responsive design for all devices
   - Opens in new tab for better navigation

**Files Updated:**
- `templates/index.html` - Added GitHub section
- `static/css/style.css` - Added GitHub button styling

**Status: COMPLETED** - GitHub link added to homepage

## Update 7: Dev Notes Update

**Exact Prompt:** "in the dev notes, can you redo to tit to include my exact prmopts tha ti typed here?"

**Summary of Changes Made:**
1. **Updated dev_notes.md:**
   - Replaced all paraphrased prompts with exact user prompts
   - Preserved all typos and formatting as originally typed
   - Maintained all summaries and status updates
   - Added new sections for GitHub setup and homepage link

**Status: COMPLETED** - Dev notes updated with exact prompts
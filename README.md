# Saad Siddique - Personal Website

A professional personal website built with Python Flask, featuring a clean design inspired by the New York Times layout.

## Features

- **Multi-page Navigation**: Home, About Me, Resume, Projects, and Contact pages
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Contact Form**: Full-featured contact form with validation and accessibility features
- **Professional Layout**: Clean, newspaper-style design with professional typography
- **Accessibility Compliant**: Proper labels, alt text, and semantic HTML structure

## Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── about.html        # About Me page
│   ├── resume.html       # Resume page
│   ├── projects.html     # Projects showcase
│   ├── contact.html      # Contact page with form
│   └── thankyou.html     # Thank you page
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── images/           # Images and photos
└── README.md             # This file
```

## Installation & Setup

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

## Pages Overview

### Homepage (`/`)
- Welcome message and introduction
- Quick navigation to all sections
- Professional highlights and key features

### About Me (`/about`)
- Detailed professional biography
- Skills and competencies
- Personal interests and career goals

### Resume (`/resume`)
- Professional experience and education
- Technical skills and certifications
- Key achievements and accomplishments
- Download link for PDF resume

### Projects (`/projects`)
- Showcase of key projects
- Detailed descriptions and technologies used
- Links to live demos and source code
- Professional portfolio presentation

### Contact (`/contact`)
- Contact information and social links
- Interactive contact form with validation
- Professional networking opportunities

## Contact Form Features

The contact form includes:
- **Required Fields**: First Name, Last Name, Email, Password, Confirm Password
- **Validation**: HTML5 and JavaScript validation
- **Accessibility**: Proper labels and error messages
- **Security**: Server-side validation and error handling

## Design Features

- **Typography**: Professional fonts (Libre Baskerville for headings, Source Sans Pro for body text)
- **Layout**: Clean, newspaper-inspired design with proper spacing
- **Colors**: Professional color scheme with high contrast
- **Responsive**: Mobile-first design that works on all devices
- **Accessibility**: WCAG compliant with proper semantic structure

## Customization

To customize the website for your own use:

1. **Update Personal Information**: Edit the content in each HTML template
2. **Replace Images**: Add your own photos to the `static/images/` directory
3. **Update Resume**: Replace the resume content in `resume.html` or update the PDF link
4. **Modify Contact Info**: Update email addresses and social media links
5. **Customize Styling**: Modify `static/css/style.css` for different colors or layouts

## Technical Requirements

- Python 3.7+
- Flask 2.3.3
- Modern web browser with JavaScript enabled

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This project is for personal use. Feel free to use it as a template for your own personal website.

---

**Contact**: For questions or feedback, please use the contact form on the website or reach out via the provided contact information.

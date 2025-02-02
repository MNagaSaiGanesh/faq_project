# FAQ Project

This is a Django-based FAQ management system that supports multiple languages and provides a REST API for managing FAQs.

## Features
- **WYSIWYG Editor**: Supports rich text formatting using `django-ckeditor`
- **Multilingual Support**: Automatically translates FAQs into different languages using `googletrans`
- **API Endpoints**: Retrieve FAQs with language selection (`?lang=hi`, `?lang=bn`)
- **Caching with Redis**: Improves performance by caching translated FAQs
- **Admin Panel**: Easy FAQ management via Django Admin
- **Docker Support** (optional)

## Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/MNagaSaiGanesh/faq_project.git
cd faq_project

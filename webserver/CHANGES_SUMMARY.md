# zcPLC Web GUI Changes Summary

## Overview
This document summarizes the changes made to convert the OpenPLC web GUI to zcPLC with internationalization support for English and Chinese.

## Changes Made

### 1. Branding Changes (OpenPLC → zcPLC)
- **Logo files**: Copied OpenPLC logos to zcPLC versions
  - `static/logo-openplc.png` → `static/logo-zcplc.png`
  - `static/openplc_logo.gif` → `static/zcplc_logo.gif`

- **Text replacements in web interface**:
  - Page titles: "OpenPLC Webserver" → "zcPLC Webserver"
  - Welcome message: "Welcome to OpenPLC" → "Welcome to zcPLC"
  - Program upload description references
  - Hardware layer descriptions
  - Python SubModule (PSM) references
  - Settings and runtime references

### 2. Internationalization (i18n) Implementation

#### New Files Created:
- **`translations.py`**: Core translation system
  - Supports English ('en') and Chinese ('zh') languages
  - Translation dictionary with all UI text
  - Helper functions for getting translations

#### Modified Files:
- **`webserver.py`**: 
  - Added translation import and helper functions
  - Implemented language session management
  - Added `/set_language/<lang>` route for language switching
  - Created `generate_login_page()` function with localized login page
  - Updated `draw_top_div()` function with language selector and translated status text
  - Modified login route to use new localized login page

- **`pages.py`**: 
  - Updated static text to use zcPLC branding

### 3. Features Added

#### Language Support:
- **English** (default): All existing functionality
- **Chinese**: Full Chinese translation of the interface
- **Language Selector**: Top-right corner of all pages
- **Session Persistence**: Language choice is remembered across sessions

#### Key Translated Elements:
- Login page (welcome message, form placeholders, buttons)
- Navigation menu items
- Page headers and descriptions
- Status indicators (Running, Stopped, Compiling)
- Form labels and buttons
- Table headers

### 4. Technical Implementation Details

#### Translation System:
- Dictionary-based translations in `translations.py`
- Helper function `t(key)` for easy translation in templates
- Language detection from Flask session
- Fallback to English if translation not found

#### User Experience:
- Language selector visible on all pages
- Current language highlighted in selector
- Clicking language switches interface immediately
- No page refresh required for language changes

## Usage

### For Users:
1. Access the web interface at the usual URL
2. Use the language selector in the top-right corner to switch between English and Chinese
3. All interface text will be updated immediately

### For Developers:
1. Add new translations to the `TRANSLATIONS` dictionary in `translations.py`
2. Use `t('key')` function in f-strings to make text translatable
3. Add new language codes to the system by extending the translations dictionary

## Files Modified:
- `webserver.py` - Main web server with i18n support
- `pages.py` - Static page templates with zcPLC branding
- `static/logo-zcplc.png` - New zcPLC logo (copy of OpenPLC logo)
- `static/zcplc_logo.gif` - New zcPLC animated logo

## Files Created:
- `translations.py` - Translation system
- `CHANGES_SUMMARY.md` - This documentation file

## Testing
- Translation system tested and working
- Both language files compile without syntax errors
- Logo files successfully created and accessible
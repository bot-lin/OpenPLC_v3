# -*- coding: utf-8 -*-
"""
zcPLC Internationalization Support
Supports Chinese (Simplified) and English
"""

import json
import os
from flask import session, request

class I18n:
    def __init__(self):
        self.translations = {}
        self.current_language = 'en'
        self.supported_languages = ['en', 'zh']
        self.load_translations()
    
    def load_translations(self):
        """Load translation files"""
        base_path = os.path.dirname(os.path.abspath(__file__))
        for lang in self.supported_languages:
            try:
                with open(os.path.join(base_path, 'translations', f'{lang}.json'), 'r', encoding='utf-8') as f:
                    self.translations[lang] = json.load(f)
            except FileNotFoundError:
                print(f"Warning: Translation file for {lang} not found")
                self.translations[lang] = {}
    
    def set_language(self, language):
        """Set current language"""
        if language in self.supported_languages:
            self.current_language = language
            session['language'] = language
    
    def get_language(self):
        """Get current language from session or default"""
        if 'language' in session:
            return session['language']
        # Try to detect from browser
        if request and hasattr(request, 'accept_languages'):
            for lang in request.accept_languages:
                if lang.language in self.supported_languages:
                    return lang.language
        return 'en'  # Default to English
    
    def translate(self, key, **kwargs):
        """Translate a key to current language"""
        current_lang = self.get_language()
        
        # Get translation from current language
        if current_lang in self.translations and key in self.translations[current_lang]:
            text = self.translations[current_lang][key]
        # Fallback to English
        elif 'en' in self.translations and key in self.translations['en']:
            text = self.translations['en'][key]
        # Return key if no translation found
        else:
            text = key
        
        # Format with kwargs if provided
        if kwargs:
            try:
                text = text.format(**kwargs)
            except KeyError:
                pass
        
        return text
    
    def get_available_languages(self):
        """Get list of available languages"""
        return [
            {'code': 'en', 'name': 'English', 'native': 'English'},
            {'code': 'zh', 'name': 'Chinese (Simplified)', 'native': '简体中文'}
        ]

# Global instance
i18n = I18n()

def _(key, **kwargs):
    """Shorthand function for translation"""
    return i18n.translate(key, **kwargs)

def init_i18n(app):
    """Initialize i18n with Flask app"""
    @app.before_request
    def before_request():
        # Set language from session or detect from browser
        i18n.current_language = i18n.get_language()
    
    # Make translation functions available in templates
    app.jinja_env.globals['_'] = _
    app.jinja_env.globals['get_available_languages'] = i18n.get_available_languages
    app.jinja_env.globals['current_language'] = lambda: i18n.get_language()
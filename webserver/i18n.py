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
        translations_path = os.path.join(base_path, 'translations')
        
        # Create translations directory if it doesn't exist
        if not os.path.exists(translations_path):
            print(f"Warning: Translations directory not found: {translations_path}")
            os.makedirs(translations_path, exist_ok=True)
        
        for lang in self.supported_languages:
            translation_file = os.path.join(translations_path, f'{lang}.json')
            try:
                with open(translation_file, 'r', encoding='utf-8') as f:
                    self.translations[lang] = json.load(f)
                print(f"Loaded translations for {lang} from {translation_file}")
            except FileNotFoundError:
                print(f"Warning: Translation file not found: {translation_file}")
                self.translations[lang] = {}
            except json.JSONDecodeError as e:
                print(f"Warning: Invalid JSON in {translation_file}: {e}")
                self.translations[lang] = {}
    
    def set_language(self, language):
        """Set current language"""
        if language in self.supported_languages:
            self.current_language = language
            try:
                session['language'] = language
            except RuntimeError:
                # Session not available outside request context
                pass
    
    def get_language(self):
        """Get current language from session or default"""
        try:
            if 'language' in session:
                return session['language']
        except RuntimeError:
            # Session not available outside request context
            pass
        # Try to detect from browser
        if request and hasattr(request, 'accept_languages'):
            try:
                for lang in request.accept_languages:
                    # Handle both tuple and LanguageTag objects
                    lang_code = lang[0] if isinstance(lang, tuple) else getattr(lang, 'language', str(lang))
                    # Extract just the language part (e.g., 'zh-CN' -> 'zh')
                    lang_code = lang_code.split('-')[0].lower()
                    if lang_code in self.supported_languages:
                        return lang_code
            except (AttributeError, IndexError, TypeError):
                pass  # Fallback to default
        return 'en'  # Default to English
    
    def translate(self, key, **kwargs):
        """Translate a key to current language"""
        try:
            current_lang = self.get_language()
            
            # Handle nested keys like 'navigation.dashboard'
            def get_nested_value(data, key_path):
                keys = key_path.split('.')
                value = data
                for k in keys:
                    if isinstance(value, dict) and k in value:
                        value = value[k]
                    else:
                        return None
                return value
            
            text = None
            
            # Get translation from current language
            if current_lang in self.translations:
                text = get_nested_value(self.translations[current_lang], key)
            
            # Fallback to English
            if text is None and 'en' in self.translations:
                text = get_nested_value(self.translations['en'], key)
            
            # Return key if no translation found
            if text is None:
                text = key
            
            # Format with kwargs if provided
            if kwargs and isinstance(text, str):
                try:
                    text = text.format(**kwargs)
                except (KeyError, ValueError):
                    pass
            
            return str(text)
            
        except Exception as e:
            print(f"Translation error for key '{key}': {e}")
            return key
    
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
        try:
            i18n.current_language = i18n.get_language()
        except Exception as e:
            # Fallback to English if any error occurs
            i18n.current_language = 'en'
            print(f"Warning: i18n language detection failed: {e}")
    
    # Make translation functions available in templates
    app.jinja_env.globals['_'] = _
    app.jinja_env.globals['get_available_languages'] = i18n.get_available_languages
    app.jinja_env.globals['current_language'] = lambda: i18n.get_language()
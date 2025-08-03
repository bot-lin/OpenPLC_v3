# -*- coding: utf-8 -*-
"""
Internationalization support for zcPLC webserver
Supports English and Chinese languages
"""

TRANSLATIONS = {
    'en': {
        'welcome_to_zcplc': 'Welcome to zcPLC',
        'zcplc_webserver': 'zcPLC Webserver',
        'username': 'Username',
        'password': 'Password',
        'login': 'Login',
        'dashboard': 'Dashboard',
        'programs': 'Programs',
        'monitoring': 'Monitoring',
        'slave_devices': 'Slave Devices',
        'modbus': 'Modbus',
        'hardware': 'Hardware',
        'settings': 'Settings',
        'users': 'Users',
        'logout': 'Logout',
        'running': 'Running',
        'stopped': 'Stopped',
        'compiling': 'Compiling',
        'upload_program': 'Here you can upload a new program to zcPLC or revert back to a previous uploaded program shown on the table.',
        'slave_devices_description': 'List of Slave devices attached to zcPLC.',
        'hardware_description': 'zcPLC controls inputs and outputs through a piece of code called hardware layer (also known as driver). Therefore, to properly handle the inputs and outputs of your board, you must select the appropriate hardware layer for it. The Blank hardware layer is the default option on zcPLC, which provides no support for native inputs and outputs.',
        'hardware_layer': 'zcPLC Hardware Layer',
        'python_submodule': 'zcPLC Python SubModule (PSM)',
        'psm_description': 'PSM is a powerful bridge that connects zcPLC core to Python. You can use PSM to write your own zcPLC driver in pure Python. See below for a sample driver that switches %IX0.0 every second',
        'hostname_description': 'Hostname allows you to access the zcPLC Runtime dashboard from another computer on the same network using',
        'start_run_mode': 'Start zcPLC in RUN mode',
        'program_name': 'Program Name',
        'file': 'File',
        'date_uploaded': 'Date Uploaded',
        'device_name': 'Device Name',
        'device_type': 'Device Type'
    },
    'zh': {
        'welcome_to_zcplc': '欢迎使用 zcPLC',
        'zcplc_webserver': 'zcPLC 网页服务器',
        'username': '用户名',
        'password': '密码',
        'login': '登录',
        'dashboard': '仪表盘',
        'programs': '程序',
        'monitoring': '监控',
        'slave_devices': '从设备',
        'modbus': 'Modbus',
        'hardware': '硬件',
        'settings': '设置',
        'users': '用户',
        'logout': '退出',
        'running': '运行中',
        'stopped': '已停止',
        'compiling': '编译中',
        'upload_program': '您可以在这里上传新的程序到 zcPLC 或回退到表格中显示的先前上传的程序。',
        'slave_devices_description': '连接到 zcPLC 的从设备列表。',
        'hardware_description': 'zcPLC 通过一段称为硬件层（也称为驱动程序）的代码来控制输入和输出。因此，要正确处理您板子的输入和输出，您必须为其选择合适的硬件层。空白硬件层是 zcPLC 的默认选项，它不提供对本机输入和输出的支持。',
        'hardware_layer': 'zcPLC 硬件层',
        'python_submodule': 'zcPLC Python 子模块 (PSM)',
        'psm_description': 'PSM 是连接 zcPLC 核心与 Python 的强大桥梁。您可以使用 PSM 用纯 Python 编写自己的 zcPLC 驱动程序。下面是一个每秒切换 %IX0.0 的示例驱动程序',
        'hostname_description': '主机名允许您使用以下地址从同一网络上的另一台计算机访问 zcPLC 运行时仪表盘',
        'start_run_mode': '以运行模式启动 zcPLC',
        'program_name': '程序名称',
        'file': '文件',
        'date_uploaded': '上传日期',
        'device_name': '设备名称',
        'device_type': '设备类型'
    }
}

def get_translation(key, lang='en'):
    """
    Get translation for a given key and language
    Args:
        key: Translation key
        lang: Language code ('en' or 'zh')
    Returns:
        Translated string or the key if translation not found
    """
    if lang not in TRANSLATIONS:
        lang = 'en'  # Default to English
    
    return TRANSLATIONS[lang].get(key, key)

def get_supported_languages():
    """
    Get list of supported language codes
    Returns:
        List of supported language codes
    """
    return list(TRANSLATIONS.keys())

def get_language_names():
    """
    Get dictionary of language codes to display names
    Returns:
        Dictionary mapping language codes to display names
    """
    return {
        'en': 'English',
        'zh': '中文'
    }
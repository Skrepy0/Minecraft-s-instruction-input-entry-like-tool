
class SLanguage:
    def __init__(self,_options):
        self.options = _options
        if _options['language'] == 'chinese':
            self.select_directory_title = "选择文本文件"
            self.filetypes_1 = "文本文件"
            self.filetypes_2 = "所有文件"
            self.save_l = '已保存'
            self.open_l = "打开"
            self.save_ = "保存"
            self.quit_ = "退出"
            self.del_ = "删除"
            self.copy_path = "复制路径"
            self.copy_web_path = '复制网址'
            self.file_ = "文件"
            self.edit = "编辑"
            self.add = '添加'
            self.screenshot_settings = "截图设置"
            self.open_folder_s = "截屏后打开保存文件夹:"
            self.screenshot_path_l = "选择截图保存路径"
            self.theme_l = "主题设置"
            self.choose_color = "选择命令框颜色"
            self.apply_l = '应用'
            self.slider_l = "命令框不透明度"
            self.language = '语言:简体中文'
            self.language_l = '语言设置'
        else:
            self.select_directory_title = "Select text file"
            self.filetypes_1 = "Text file"
            self.filetypes_2 = "All files"
            self.save_l = 'Saved'
            self.open_l = "open"
            self.save_ = "save"
            self.quit_ = "quit"
            self.del_ = "delete"
            self.copy_path = "copy path"
            self.copy_web_path = 'copy url'
            self.file_ = "file"
            self.edit = "edit"
            self.add = 'add'
            self.screenshot_settings = "Screenshot settings"
            self.open_folder_s = "Open the save folder after taking a screenshot:"
            self.screenshot_path_l = "Select screenshot save path"
            self.theme_l = "Theme settings"
            self.choose_color = "Select command box color"
            self.apply_l = 'Apply'
            self.slider_l = "Command box opacity"
            self.language = 'Language:English'
            self.language_l = 'Language settings'










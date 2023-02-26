import configparser


class ConfigTools(object):
    """
    配置读取，文件类，字符串读取。
    """

    def __init__(self, file_name: str = "", file_str: str = ""):
        self.config = configparser.ConfigParser(allow_no_value=True)
        if file_name:
            self.config.read(file_name, encoding='utf8')
        elif file_str:
            self.config.read_string(file_str)
        else:
            raise RuntimeError(
                f"无配置"
            )


if __name__ == '__main__':
    res = ConfigTools(file_name=r"D:\test\record\utils\test.ini")
    print(res.config.get("test","port"))

def my_config_log():
    logger = logging.getLogger()
    for handler in logger.handlers:
        # 默认有一个 StreamHandler 需要在上面作修改 该handler 可以打印到控制台
        if isinstance(handler, logging.StreamHandler):
            console_formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(console_formatter)
    logger.setLevel(logging.INFO)
    # 创建一个文件处理器  when='H': 这行代码设置了日志轮换的条件。
    # 'H'表示小时，这意味着每隔24小时，就会创建一个新的日志文件，并将旧的日志文件重命名。
    #backupCount = 20: 这行代码设置了最多保留的日志文件数量。在这里，最多会保留20个日志文件。当超过这个数量时，最旧的日志文件将被删除。
    file_handler = ConcurrentTimedRotatingFileHandler(filename=config.get("log", "path"), when='H', interval=24,
                                                      backupCount=20, encoding='utf8')
    file_handler.setLevel(logging.INFO)
    # 创建一个格式化器 将格式化器添加到处理器
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    # 将处理器添加到logger对象
    logger.addHandler(file_handler)
def my_config_log_win():
    import colorlog  # 对于打印台中的log 可以显现不同的颜色
    logger = logging.getLogger()
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            handler.setFormatter(colorlog.ColoredFormatter(
                '%(log_color)s %(asctime)s %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                log_colors={
                    'DEBUG': 'green',
                    'INFO': 'bold_white',
                }
            ))

    logger.setLevel(logging.INFO)
    # 创建一个文件处理器
    file_handler = ConcurrentTimedRotatingFileHandler(filename=config.get("log", "path"), when='H', interval=24,
                                                     backupCount=20, encoding='utf8')
    file_handler.setLevel(logging.INFO)
    # 创建一个格式化器
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # 将格式化器添加到处理器
    file_handler.setFormatter(file_formatter)
    # 将处理器添加到logger对象
    logger.addHandler(file_handler)

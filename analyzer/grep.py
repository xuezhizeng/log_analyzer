import os
import re


def grep(path, keyword):
    """
    Choose comman 'cat & grep' for the linux support and speed.
    :param path: path of the file.
    :param keyword: can be date, time, action,
                    path or file in log.
    :return: an generator ogf the result which should be printed
            in terminal.
    """
    if os.path.exists(path):
        for log in os.popen("cat {path} | grep {keyword}"
                            .format(path=path, keyword=keyword)):
            yield log
    else:
        raise ValueError("Can't find corresponding log!")


def result_parser(regex, label, result):
    """
    use regex to parse the result according to customed pattern
    :param regex: regex expression
    :prarm lable_name: lables in regex expression
    :param result: generator, result provided by grep
    :return: generator, result match the pattern
    """
    pattern = re.compile(regex)
    for log in result:
        yield pattern.match(log).group(*label)

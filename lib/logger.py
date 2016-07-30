#-*- coding: UTF-8 -*-

import logging
import logging.config
import os
class Logger(object):

    #logging.config.fileConfig("E:/workspace/pycharm/ting/log/logger.conf")
    cfgpath = os.path.split(os.path.realpath(__file__))[0] +"/logger.conf"
    logging.config.fileConfig(cfgpath)
    logger = logging.getLogger('root')  # 生成一个日志对象
    @staticmethod
    def debug(message):
        Logger.logger.debug(message);
    @staticmethod
    def info(message):
        Logger.logger.info(message);
    @staticmethod
    def warn(message):
        Logger.logger.warn(message);
    @staticmethod
    def error(message):
        Logger.logger.error(message);
    @staticmethod
    def critical(message):
        Logger.logger.critical(message);


if __name__ == "__main__":
    Logger.debug("debug");
    Logger.info("info");
    Logger.warn("warn");
    Logger.error("error");
    Logger.critical("critical");

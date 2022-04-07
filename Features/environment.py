# -*- coding: UTF-8 -*-
import configparser
import os
import time
from selenium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from Utilities import loggerutils
from Utilities import deleteOldFiles
from time import strftime
from pageactions.TFN_Library import TFN_Library


# ----------------------------------------------------------------------------
# before_step(context, step), after_step(context, step)
#   * These run before and after every step.
#   * The step passed in is an instance of Step.
# before_scenario(context, scenario), after_scenario(context, scenario)
#   * These run before and after each scenario is run.
#   * The scenario passed in is an instance of Scenario.
# before_feature(context, feature), after_feature(context, feature)
#   * These run before and after each feature file is exercised.
#   * The feature passed in is an instance of Feature.
# before_tag(context, tag), after_tag(context, tag)
#   * These run before and after each tag.
#   * The tag passed in is an instance of Tag
# ----------------------------------------------------------------------------

def before_all(context):
    """Set up test environment
    Create driver based on the desired capabilities provided.
    Valid desired capabilities can be 'firefox', 'chrome' or 'ie'.
    For adding new drivers add a new static method in DriverFactory class.

    :param context: Holds contextual information during the running of tests
    :return: None
    """
    dir_path = os.path.abspath(os.getcwd())

    dirs_to_clean = [dir_path + '/Screenshots',
                     dir_path + '/Logs',
                     dir_path + '/allure_reports',
                     dir_path + '/reports',
                     dir_path + '/Features/steps',
                     dir_path + '/Locators',
                     dir_path + '/pageactions',
                     dir_path + '/Utilities']

    patterns = ['*.png', '*.log', '*.json', '*.xml', '*.pyc']

    days_deletion = 0
    for dirs in dirs_to_clean:
        deleteOldFiles.find_files(dirs, patterns, days_deletion)

    context.props = configparser.RawConfigParser()
    context.props.read('properties/config.properties')
    context.url = context.props.get('config', 'config.URL')
    context.path = dir_path + '/Drivers/chromedriver.exe'

    loggerutils.setup_logging()
    loggerutils.setup_formatted_logging(context)
    context.test_started_milli_time = int(round(time.time() * 1000))
    loggerutils.setup_unformatted_logging(context)

    context.logger.info("\n")
    context.logger.info("=============================================================================================")
    context.logger.info("TESTING STARTED AT : " + strftime("%Y-%m-%d %H:%M:%S"))

    loggerutils.setup_formatted_logging(context)


def before_feature(context, feature):
    """Log starting of execution of feature
   :param context: Holds contextual information during the running of tests
   :param feature: Holds contextual information about the feature during the running of tests
   :return: None
   """

    for scenario in feature.scenarios:
        if "Sanity" in scenario.effective_tags or "Integration" in scenario.effective_tags \
                or "Queue" in scenario.effective_tags or "Sequential" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=1)

    loggerutils.setup_unformatted_logging(context)

    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("STARTED EXECUTION OF FEATURE: " + str(feature.name))
    context.logger.info("Tags: " + str([str(item) for item in feature.tags]))
    context.logger.info("Filename: " + str(feature.filename))
    context.logger.info("Line: " + str(feature.line))
    context.logger.info("---------------------------------------------------------------------------------------------")

    loggerutils.setup_formatted_logging(context)

    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is not None:
            browser = context.config.userdata['BROWSER']
            if browser == 'chrome':
                context.driver = webdriver.Chrome(executable_path=context.path)
            elif browser == 'firefox':
                context.driver = webdriver.Firefox()
            elif browser == 'safari':
                context.driver = webdriver.Safari()
    else:
        if context.props.get('config', 'config.BROWSER') == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument("--window-size=1536,960")
            context.driver = webdriver.Chrome(executable_path=context.path)
    context.driver.delete_all_cookies()
    context.driver.implicitly_wait(1)
    context.driver.maximize_window()
    context.driver.get(context.url)

    # Instantiate Libraries
    context.lib = TFN_Library(context)
    #
    # Namespaces or Variable Controllers
    context.RandomString = context.lib.get_random_alpha_numeric_string(20)
    context.RandomString2 = context.lib.get_random_alpha_numeric_string(25)


def before_scenario(context, scenario):
    """Launch browser and open application
    :param context: Holds contextual information during the running of tests
    :param scenario: Holds contextual information about scenario during the running of tests
    :return: None
    """

    context.driver.get(context.url)

    loggerutils.setup_unformatted_logging(context)

    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("STARTED EXECUTION OF SCENARIO: " + str(scenario.name))
    context.logger.info("Tags: " + str([str(item) for item in scenario.tags]))
    context.logger.info("Filename: " + str(scenario.filename))
    context.logger.info("Line: " + str(scenario.line))
    context.logger.info("---------------------------------------------------------------------------------------------")

    loggerutils.setup_formatted_logging(context)

    context.driver.maximize_window()


def after_step(context, step):
    """Save screenshot in case of test step failure
    This function runs everytime after a step is executed. Check is step passed, then just log it and return
    if step fails and step is a part of portal scenario, take the screenshot of the failure. The screenshot file name
    is scenario_name.png where spaces within step name is replaced by '_'
    example: book_a_roundtrip_ticket_2016-12-01_12-34-32.png
    :param context: Holds contextual information during the running of tests
    :param step: Holds contextual information about step during the running of tests
    :return: None
    """
    if step.status == "failed":
        context.logger.info(step.name + " : FAILED, Line: " + str(step.line))

        try:
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')

            __current_scenario_name = context.scenario.name.split("--")[0]
            __screenshot_file_name = "screenshots" + os.path.sep + __current_scenario_name.replace(" ", "_") + "_" + \
                                     strftime("%Y-%m-%d_%H-%M-%S") + '.png'

            context.driver.save_screenshot(__screenshot_file_name)
            context.logger.info("Screenshot is captured in file '" + __screenshot_file_name + "'")
        except Exception as e:
            context.logger.error("Unable to take screenshot! Error: %s" % e, exc_info=True)

    else:
        context.logger.info(step.name + " : PASSED")


def after_scenario(context, scenario):
    """Close browser and quit driver
    :param context: Holds contextual information during the running of tests
    :param scenario: Holds contextual information about scenario during the running of tests
    :return: None
    """
    loggerutils.setup_unformatted_logging(context)

    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("FINISHED EXECUTION OF SCENARIO: " + str(scenario.name))
    context.logger.info("Result: " + str(scenario.status))
    context.logger.info("Time taken: " + str("{0:.2f}".format(scenario.duration / 60)) + " mins, " +
                        str("{0:.2f}".format(scenario.duration % 60)) + " secs")
    context.logger.info("---------------------------------------------------------------------------------------------")

    loggerutils.setup_formatted_logging(context)


def after_feature(context, feature):
    """Log finished execution of feature
    :param context: Holds contextual information during the running of tests
    :param feature: Holds contextual information about feature during the running of tests
    :return: None
    """
    loggerutils.setup_unformatted_logging(context)

    context.logger.info("---------------------------------------------------------------------------------------------")
    context.logger.info("FINISHED EXECUTION OF FEATURE: " + str(feature.name))
    context.logger.info("Result: " + str(feature.status))
    context.logger.info("Time taken: " + str("{0:.2f}".format(feature.duration / 60)) + " mins, " +
                        str("{0:.2f}".format(feature.duration % 60)) + " secs")
    context.logger.info("---------------------------------------------------------------------------------------------")

    loggerutils.setup_formatted_logging(context)

    if context.driver is not None:
        try:
            context.driver.close()
        except Exception as e:
            context.logger.error("Unable to close browser window! Error: %s" % e, exc_info=True)

        try:
            context.driver.quit()
        except Exception as e:
            context.logger.error("Unable to quit driver! Error: %s" % e, exc_info=True)


def after_all(context):
    """Log test finished
    :param context: Holds contextual information during the running of tests
    :return: None
    """
    loggerutils.setup_unformatted_logging(context)

    context.logger.info("\n")
    context.logger.info("TESTING FINISHED AT : " + strftime("%Y-%m-%d %H:%M:%S"))
    context.logger.info("=============================================================================================")

    loggerutils.setup_formatted_logging(context)

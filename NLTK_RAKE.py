from rake_nltk import Rake
import SSGLog
import winsound
import traceback

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

if __name__ == '__main__':
    try:
        logger = SSGLog.setup_custom_logger('TagTest1Logger')
        with open('Textfilter.log', "r") as myfile:
                data = myfile.read().replace('\n', '')
                r.extract_keywords_from_text(data)

                logger.info("Rank of phrases : %s", r.get_ranked_phrases(),'\n') # To get keyword phrases ranked highest to lowest.
    except Exception:
        logger.info("Something is wrong! Error logged to log file!")
        logger.exception("Something is wrong!")
        traceback.print_exc()
        winsound.Beep(5000, 200)
    finally:
        logger.info("Done!")